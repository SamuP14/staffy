<template>
  <div class="full-width-container">
    <table class="table table-striped table-hover" role="table" aria-label="Task list">
      <colgroup>
        <col style="width: 12%;" />
        <col style="width: 20%;" />
        <col style="width: 10%;" />
        <col style="width: 10%;" />
        <col style="width: 10%;" />
        <col style="width: 12%;" />
        <col style="width: 10%;" />
        <col style="width: 14%;" />
      </colgroup>
      <thead>
        <tr>
          <th class="tb-bg text-white">Title</th>
          <th class="tb-bg text-white">Description</th>
          <th class="tb-bg text-white">Due Date</th>
          <th class="tb-bg text-white">Status</th>
          <th class="tb-bg text-white">Priority</th>
          <th class="tb-bg text-white">Created at</th>
          <th class="tb-bg text-white">Employees</th>
          <th class="tb-bg text-white">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in tasks" :key="task.id">
          <td>{{ task.title }}</td>
          <td>{{ truncate(task.description, 25) }}</td>
          <td>{{ formatDate(task.due_date) }}</td>
          <td>{{ capitalize(task.status) }}</td>
          <td>{{ capitalize(task.priority) }}</td>
          <td>{{ formatDate(task.created_at) }}</td>
          <td>
            <span v-if="task.employees.length">
              <span v-for="(emp, index) in task.employees" :key="emp.id">
                {{ emp.user.first_name }} {{ emp.user.last_name }}<span v-if="index < task.employees.length - 1">,
                </span>
              </span>
            </span>
            <span v-else class="text-muted" aria-live="polite">Not assigned</span>
          </td>
          <td>
            <button class="btn btn-warning btn-sm ms-2" @click="viewTask(task.id)" aria-label="View task details">
              <router-link :to="`/tasks/${task.id}`" class="unstyled-link">
                <BIconEye />
              </router-link>
            </button>
            <button class="btn btn-primary btn-sm ms-2" aria-label="Edit task">
              <router-link :to="`/tasks/${task.id}/edit`" class="unstyled-link">
                <BIconPencilSquare />
              </router-link>
            </button>
            <button class="btn btn-danger btn-sm ms-2" @click="deleteTask(task.id)" aria-label="Delete task">
              <BIconTrash />
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import {
  BIconPencilSquare,
  BIconTrash,
  BIconEye,
} from 'bootstrap-icons-vue';

interface TaskPayload {
  id: number;
  title: string;
  description: string;
  due_date: string;
  status: 'pending' | 'in_progress' | 'completed';
  priority: 'low' | 'medium' | 'high';
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


const tasks = ref<TaskPayload[]>([]);
const loading = ref(false);
const error = ref<string | null>(null);

const fetchTasks = async () => {
  loading.value = true;
  try {
    const res = await axios.get<TaskPayload[]>('http://127.0.0.1:8000/api/tasks/');
    tasks.value = res.data;
  } catch (e) {
    error.value = 'Error al cargar tareas';
    console.error(e);
  } finally {
    loading.value = false;
  }
};

onMounted(fetchTasks);

const formatDate = (d: string) => {
  return new Date(d).toLocaleDateString('es-ES');
};

const capitalize = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);

const truncate = (text: string, length: number) => {
  return text.length > length ? text.slice(0, length) + '...' : text;
};

const viewTask = (id: number) => {
  window.location.href = `/tasks/${id}/`;
};

const deleteTask = async (id: number) => {
  if (!confirm('Are you sure you want to delete this task?')) return;
  try {
    await axios.post(`http://127.0.0.1:8000/api/tasks/${id}/delete/`);
    tasks.value = tasks.value.filter(t => t.id !== id);
  } catch (e) {
    alert('Error al eliminar la tarea' + ' || ' + e);
  }
};
</script>

<style scoped>
.full-width-container {
  width: 100vw;
  margin: 0 auto;
  padding: 0;
  margin-top: 65px;
  padding-bottom: 70px;
  box-sizing: border-box;
  overflow-x: hidden;
}

.table th,
.table td {
  text-align: center;
  vertical-align: middle;
}

.tb-bg {
  background-color: #0D7BA6;
}

#btn-add {
  background-color: #0D7BA6;
  border-color: #0D7BA6;
}

#btn-add:hover {
  background-color: #0A6E92;
}

.unstyled-link {
  all: unset;
  cursor: pointer;
  display: inline-block;
  width: 100%;
  height: 100%;
}
</style>
