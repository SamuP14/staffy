<template>
  <div class="container mt-5 mb-5" role="form" aria-label="Add New Employee Form">
    <h2 class="mb-5 mt-5 text-center">New Employee Form</h2>
    <form @submit.prevent="submitForm">
      <div class="row">
        <div class="col-md-6">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" id="username" v-model="employee.username" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="firstName" class="form-label">First Name</label>
            <input type="text" id="firstName" v-model="employee.firstName" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="lastName" class="form-label">Last Name</label>
            <input type="text" id="lastName" v-model="employee.lastName" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="idNumber" class="form-label">ID Number</label>
            <input type="text" id="idNumber" v-model="employee.idNumber" class="form-control" required />
          </div>
        </div>

        <div class="col-md-6">
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" id="email" v-model="employee.email" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" id="password" v-model="employee.password" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="phone" class="form-label">Phone</label>
            <input type="text" id="phone" v-model="employee.phone" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="profession" class="form-label">Profession</label>
            <input type="text" id="profession" v-model="employee.profession" class="form-control" required />
          </div>
        </div>
      </div>
      <button type="submit" class="btn btn-primary mt-4 w-100" aria-label="Submit new employee form">
        Add Employee
      </button>

    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

interface Employee {
  username: string;
  firstName: string;
  lastName: string;
  idNumber: string;
  email: string;
  password: string;
  phone: string;
  profession: string;
  roles: string[];
  avatar: File | string | null;
}

const router = useRouter();

const employee = ref<Employee>({
  username: '',
  firstName: '',
  lastName: '',
  idNumber: '',
  email: '',
  password: '',
  phone: '',
  profession: '',
  roles: [],
  avatar: null as File | null,
});

const submitForm = async () => {
  const payload = {
    username: employee.value.username,
    first_name: employee.value.firstName,
    last_name: employee.value.lastName,
    id_number: employee.value.idNumber,
    email: employee.value.email,
    password: employee.value.password,
    phone: employee.value.phone,
    profession: employee.value.profession,
    avatar: employee.value.avatar,
  };

  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/api/accounts/profile/add/',
      payload,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
    console.log('Empleado agregado:', response.data);

    router.push('/');
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      console.error('Error al agregar empleado:', error);
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
