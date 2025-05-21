<template>
  <div class="container mt-5 mb-5" role="form" aria-label="Add New Role Form">
    <h2 class="mb-5 mt-5 text-center">New Role Form</h2>
    <form @submit.prevent="submitForm">
      <div class="row">
        <div class="col-md-6">
          <div class="mb-3">
            <label for="code" class="form-label">Code</label>
            <input type="text" id="code" v-model="employee.code" class="form-control" required />
          </div>
          <div class="mb-3">
            <label for="name" class="form-label">Name</label>
            <input type="text" id="name" v-model="employee.name" class="form-control" required />
          </div>
        </div>
      </div>
      <button type="submit" class="btn btn-primary mt-3 w-100" aria-label="Submit new role form">
        Add Role
      </button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

interface Employee {
  code: string;
  name: string;
}

const router = useRouter();

const employee = ref<Employee>({
  code: '',
  name: '',
});

const submitForm = async () => {
  const payload = {
    code: employee.value.code,
    name: employee.value.name,
  };

  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/api/accounts/role/add/',
      payload,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
    console.log('Rol agregado:', response.data);

    router.push('/roles');
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      console.error('Error al agregar rol:', error);
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
