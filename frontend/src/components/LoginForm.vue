<template>
  <div class="login-container">
    <div class="login-card">
      <h2 class="text-center mb-4">Login</h2>
      <form @submit.prevent="handleLogin" role="form" aria-label="Login form">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input type="text" id="username" class="form-control" v-model="form.username" required />
        </div>
        <div class="mb-4">
          <label for="password" class="form-label">Password</label>
          <input type="password" id="password" class="form-control" v-model="form.password" required />
        </div>
        <button type="submit" class="btn btn-primary w-100" aria-label="Submit login form">Log In</button>
      </form>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const form = ref({ username: '', password: '' })
const auth = useAuthStore()
const router = useRouter()

const handleLogin = async () => {
  const success = await auth.login(form.value.username, form.value.password)
  if (success) {
    router.push('/employees')
  } else {
    alert('Invalid credentials')
  }
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f4f4f4;
}

.login-card {
  background: white;
  padding: 30px;
  border-radius: 10px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

button {
  background: #0D7BA6;
}
</style>
