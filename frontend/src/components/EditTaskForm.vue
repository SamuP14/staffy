<template>
  <div class="profile-edit-container">
    <div v-if="task" class="profile-card">
      <div class="profile-header">
        <h2>Edit Task: {{ task.title }}</h2>
        <div class="profile-form mt-4" role="form" aria-label="Edit Task Form">
          <div class="mb-3"><label for="title" class="form-label">Title</label><input type="text" id="title" v-model="task.title" class="form-control" required /></div>

          <label for="description">Description:</label>
          <div class="mb-3"><label for="description" class="form-label">Description</label><textarea id="description" v-model="task.description" class="form-control" rows="4" required></textarea></div>

          <label for="due_date">Due Date:</label>
          <div class="mb-3"><label for="due_date" class="form-label">Due Date</label><input type="date" id="due_date" v-model="task.due_date" class="form-control" required /></div>

          <label for="status">Status:</label>
          <div class="mb-3"><label for="status" class="form-label">Status</label><select id="status" v-model="task.status" class="form-control" required>
            <option value="pending">Pending</option>
            <option value="in_progress">In Progress</option>
            <option value="completed">Completed</option>
          </select></div></div>

          <label for="priority">Priority:</label>
          <div class="mb-3"><label for="priority" class="form-label">Priority</label><select id="priority" v-model="task.priority" class="form-control" required>
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>

          <div class="mb-3"><label for="employees" class="form-label">Employees (comma separated usernames)</label><input type="text" id="employees" v-model="employeeString" class="form-control" required /></div>

          <button class="btn btn-primary w-100 mt-3" @click="saveTask" aria-label="Save edited task">Save</button>
        </div>
      </div>
    </div>
    <div v-else>
      <p>Loading task...</p>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

interface Task {
  id: number;
  title: string;
  description: string;
  due_date: string;
  status: 'pending' | 'in_progress' | 'completed';
  priority: 'low' | 'medium' | 'high';
  employees: string[];
  created_at: string;
  updated_at: string;
}

export default {
  setup() {
    const route = useRoute();
    const router = useRouter();
    const taskId = route.params.id as string;
    const task = ref<Task | null>(null);
    const employeeString = ref('');

    const fetchTask = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/tasks/${taskId}/`);
        task.value = response.data;
        employeeString.value = task.value!.employees.join(', ');
      } catch (error) {
        console.error('Error fetching task:', error);
      }
    };

    const saveTask = async () => {
      try {
        const updated = {
          ...task.value,
          employees: employeeString.value.split(',').map(e => e.trim()).filter(e => e),
        };

        await axios.post(`http://127.0.0.1:8000/api/tasks/${taskId}/edit/`, updated, {
          headers: { 'Content-Type': 'application/json' },
        });

        alert('Task saved successfully');
        router.push('/tasks/');
      } catch (error) {
        console.error('Error saving task:', error);
        alert('Error saving task');
      }
    };

    onMounted(fetchTask);

    return { task, employeeString, saveTask };
  },
};
</script>

<style scoped>
.profile-edit-container {
  width: 100vw;
  margin: 65px auto 0;
  padding: 20px;
  padding-bottom: 120px;
}

.profile-card {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #ddd;
}

.profile-header {
  text-align: center;
}

.profile-form label {
  display: block;
  margin: 10px 0 5px;
}

.profile-form input,
.profile-form textarea,
.profile-form select {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.profile-form button {
  padding: 10px 20px;
  background-color: #0D7BA6;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.profile-form button:hover {
  background-color: #0A6E92;
}
</style>
