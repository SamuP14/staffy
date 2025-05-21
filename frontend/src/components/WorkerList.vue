<template>
  <div class="full-width-container">
    <table class="table table-striped table-hover" role="table" aria-label="Employee list">
      <colgroup>
        <col style="width: 7%;">
        <col style="width: 13%;">
        <col style="width: 13%;">
        <col style="width: 13%;">
        <col style="width: 10%;">
        <col style="width: 20%;">
        <col style="width: 10%;">
      </colgroup>
      <thead>
        <tr>
          <th class="tb-bg text-white">Avatar</th>
          <th class="tb-bg text-white">Name</th>
          <th class="tb-bg text-white">Surname</th>
          <th class="tb-bg text-white">ID Number</th>
          <th class="tb-bg text-white">Phone</th>
          <th class="tb-bg text-white">Email</th>
          <th class="tb-bg text-white">Profession</th>
          <th class="tb-bg text-white">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.user.username">
          <td>
            <img :src="employee.avatar" :alt="`Avatar of ${employee.user.first_name} ${employee.user.last_name}`"
              class="profile-avatar" />
          </td>
          <td>{{ employee.user.first_name }}</td>
          <td>{{ employee.user.last_name }}</td>
          <td>{{ employee.id_number }}</td>
          <td>{{ employee.phone }}</td>
          <td>{{ employee.user.email }}</td>
          <td>{{ employee.profession }}</td>
          <td>
            <button class="btn btn-warning btn-sm ms-2" aria-label="View employee profile">
              <router-link :to="`/employees/${employee.user.username}`" class="unstyled-link">
                <BIconEye class="text-white" />
              </router-link>
            </button>
            <button class="btn btn-primary btn-sm ms-2" aria-label="Edit employee">
              <router-link :to="`/employees/${employee.user.username}/edit`" class="unstyled-link">
                <BIconPencilSquare class="text-white" />
              </router-link>
            </button>
            <button class="btn btn-danger btn-sm ms-2" @click="deleteEmployee(employee.user.username)"
              aria-label="Delete employee">
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
import { BIconPencilSquare, BIconTrash, BIconEye } from 'bootstrap-icons-vue';

export interface ProfilePayload {
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
  experience: string;
  avatar: string;
  role: string[];
}

const employees = ref<ProfilePayload[]>([]);

const fetchEmployees = async () => {
  try {
    const response = await axios.get<ProfilePayload[]>('http://127.0.0.1:8000/api/accounts/profile/');
    console.log('Empleados obtenidos:', response.data);
    employees.value = response.data;
  } catch (error) {
    console.error('Error al obtener empleados:', error);
  }
};

const deleteEmployee = async (username: string) => {
  if (!confirm('Are you sure you want to delete this employee?')) return;

  try {
    const response = await axios.post(`http://127.0.0.1:8000/api/accounts/profile/${username}/delete/`);
    console.log(response.data);
    employees.value = employees.value.filter(emp => emp.user.username !== username);
  } catch (error) {
    console.error('Error al eliminar empleado:', error);
  }
};

onMounted(fetchEmployees);
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

.tb-bg {
  background-color: #0D7BA6;
}

.table {
  table-layout: fixed;
  width: 100%;
  border-spacing: 0;
}

.table th,
.table td {
  border: none;
  padding: 4px 6px;
  font-size: 14px;
  word-wrap: break-word;
  white-space: normal;
  text-align: center;
}

.profile-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  object-fit: cover;
}


#btn-add,
.btn-sm {
  color: white !important;
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
