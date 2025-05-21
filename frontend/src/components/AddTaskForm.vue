<template>
  <div class="container mt-5 mb-5" role="form" aria-label="Add New Task Form">
    <h2 class="mb-5 mt-5 text-center">New Task Form</h2>
    <form @submit.prevent="submitForm">
      <div class="row">
        <div class="col-md-6">
          <div class="mb-3">
            <label for="title" class="form-label">Title</label>
            <input type="text" id="title" v-model="task.title" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="description" class="form-label">Description</label>
            <textarea id="description" v-model="task.description" class="form-control" required rows="3"></textarea>
          </div>
          <div class="mb-3">
            <label for="dueDate" class="form-label">Due Date</label>
            <input type="date" id="dueDate" v-model="task.due_date" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="priority" class="form-label">Priority</label>
            <select id="priority" v-model="task.priority" class="form-control" required>
              <option value="">Select</option>
              <option value="low">Low</option>
              <option value="medium">Medium</option>
              <option value="high">High</option>
            </select>
          </div>
        </div>

        <div class="col-md-6">
          <div class="mb-3">
            <label for="status" class="form-label">Status</label>
            <select id="status" v-model="task.status" class="form-control" required>
              <option value="">Select</option>
              <option value="pending">Pending</option>
              <option value="in_progress">In Progress</option>
              <option value="completed">Completed</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="employees" class="form-label">Employees</label>
            <select
              id="employees"
              v-model="task.employees"
              class="form-control"
              multiple
              aria-label="Select multiple employees"
            >
              <option
                v-for="employee in employeeOptions"
                :key="employee.user.username"
                :value="employee.user.username"
              >
                {{ employee.user.first_name }} {{ employee.user.last_name }} ({{ employee.user.username }})
              </option>
            </select>
          </div>
        </div>
      </div>
      <button type="submit" class="btn btn-primary mt-4 w-100" aria-label="Submit new task form">
        Add Task
      </button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

interface Task {
  title: string;
  description: string;
  due_date: string;
  status: 'pending' | 'in_progress' | 'completed' | '';
  priority: 'low' | 'medium' | 'high' | '';
  employees: string[];
}

interface EmployeeProfile {
  user: {
    username: string;
    first_name: string;
    last_name: string;
    email: string;
  };
  id: number;
  id_number: string;
  phone: string;
  profession: string;
  experience: string;
  avatar: string;
  role: string[];
}

const router = useRouter();

const task = ref<Task>({
  title: '',
  description: '',
  due_date: '',
  status: '',
  priority: '',
  employees: [],
});

const employeeOptions = ref<EmployeeProfile[]>([]);

const fetchEmployees = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/accounts/profile/');
    employeeOptions.value = response.data;
  } catch (error) {
    console.error('Error fetching employees:', error);
  }
};

onMounted(fetchEmployees);

const submitForm = async () => {
  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/api/tasks/add/',
      task.value,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
    console.log('Tarea creada:', response.data);
    router.push('/tasks');
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      console.error('Error al crear tarea:', error);
      console.log('Respuesta del servidor:', error.response?.data);
    } else {
      console.error('Error desconocido:', error);
    }
  }
};
</script>

<style scoped>
.container {
  width: 100vw;
  margin-top: 75px;
}

.row {
  display: flex;
  flex-wrap: wrap;
}

.col-md-6 {
  flex: 0 0 50%;
  padding: 0 15px;
}

button {
  background-color: #0D7BA6;
  border: #0D7BA6;
}
</style>
