<template>
  <div class="container contact-container">
    <div class="contact-card">
      <h2 class="text-center mb-4">Contact Us</h2>
      <form @submit.prevent="handleSubmit" role="form" aria-label="Contact form">
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input id="name" type="text" class="form-control" v-model="form.name" required />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input id="email" type="email" class="form-control" v-model="form.email" required />
        </div>
        <div class="mb-3">
          <label for="subject" class="form-label">Subject</label>
          <input id="subject" type="text" class="form-control" v-model="form.subject" required />
        </div>
        <div class="mb-4">
          <label for="message" class="form-label">Message</label>
          <textarea id="message" class="form-control" rows="4" v-model="form.message" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary w-100" aria-label="Send contact message">Send Message</button>
      </form>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: '',
})

const handleSubmit = () => {
  console.log('Sending message:', form.value)
}
</script>

<style scoped>
.contact-container {
  min-height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f8f9fa;
}

.contact-card {
  background-color: white;
  padding: 30px;
  border-radius: 12px;
  width: 100%;
  max-width: 500px;
  margin-bottom: 15px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}


button {
  background: #0D7BA6;
}
</style>
