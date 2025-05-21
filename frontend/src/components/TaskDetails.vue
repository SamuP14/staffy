<template>
  <div class="task-detail-container" v-if="task" role="region" aria-label="Task details">
    <div class="task-detail-card">
      <p><strong>Title: </strong> {{ task.title }}</p>
      <p><strong>Description: </strong> {{ task.description }}</p>
      <p><strong>Due Date: </strong> {{ formatDate(task.due_date) }}</p>
      <p><strong>Status: </strong> {{ capitalize(task.status) }}</p>
      <p><strong>Priority: </strong> {{ capitalize(task.priority) }}</p>
      <p><strong>Employees: </strong>
        <span v-if="task.employees.length">
          <span v-for="(emp, index) in task.employees" :key="emp.id">
            {{ emp.user.first_name }} {{ emp.user.last_name }}<span v-if="index < task.employees.length - 1">, </span>
          </span>
        </span>
        <span v-else class="text-muted">Not assigned</span>
      </p>
      <p><strong>Created at: </strong> {{ formatDate(task.created_at) }}</p>
      <p><strong>Updated at: </strong> {{ formatDate(task.updated_at) }}</p>
      <button class="btn btn-secondary mt-3" @click="goBack" aria-label="Go back to task list">← Back</button>
    </div>
  </div>
  <div v-else>
    <p class="text-center" aria-live="polite">Loading task...</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

interface Task {
  id: number;
  title: string;
  description: string;
  due_date: string;
  status: string;
  priority: string;
  employees: {
    id: number;
    user: {
      username: string;
      first_name: string;
      last_name: string;
      email: string;
    };
    id_number: string;
    phone: string;
    profession: string;
    experience: number;
    avatar: string;
    role: string[];
  }[];
  created_at: string;
  updated_at: string;
}

const task = ref<Task | null>(null);
const route = useRoute();
const router = useRouter();
const taskId = route.params.id;

const fetchTask = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/tasks/${taskId}/`);
    task.value = response.data;
  } catch (error) {
    console.error('Error fetching task:', error);
  }
};

onMounted(fetchTask);

const formatDate = (date: string) => new Date(date).toLocaleDateString('es-ES');
const capitalize = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);
const goBack = () => {
  router.push('/tasks');
};
</script>

<style scoped>
.task-detail-container {
  width: 100vw;
  margin: 80px auto;
  padding: 20px;
}

.task-detail-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 65px;
}
</style>
