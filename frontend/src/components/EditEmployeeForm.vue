<template>
  <div class="profile-edit-container">
    <div v-if="profile" class="profile-card">
      <div class="profile-header">
        <div class="d-flex flex-row align-items-center justify-content-center">
          <div class="profile-avatar-wrapper">
            <img :src="profile.avatar" alt="Avatar" class="profile-avatar" />
          </div>
          <h2>@{{ profile.user.username }}</h2>
        </div>
        <div class="profile-form mt-4" role="form" aria-label="Edit Employee Profile Form">
          <div class="mb-3">
            <label for="first_name" class="form-label">First Name:</label><input type="text" id="first_name"
              v-model="profile.user.first_name" class="form-control" required />
          </div>

          <div class="mb-3">
            <label for="last_name" class="form-label">Last Name:</label><input type="text" id="last_name"
              v-model="profile.user.last_name" class="form-control" required />
          </div>

          <div class="mb-3">
            <label for="id_number" class="form-label">ID Number:</label><input type="text" id="id_number"
              v-model="profile.id_number" class="form-control" required />
          </div>

          <div class="mb-3">
            <label for="phone" class="form-label">Phone:</label><input type="text" id="phone" v-model="profile.phone"
              class="form-control" required />
          </div>

          <div class="mb-3">
            <label for="profession" class="form-label">Profession:</label><input type="text" id="profession"
              v-model="profile.profession" class="form-control" required />
          </div>

          <div class="mb-3">
            <label for="experience" class="form-label">Experience</label><textarea id="experience"
              v-model="profile.experience" class="form-control" rows="4" required></textarea>
          </div>

          <button class="btn btn-primary w-100 mt-3" @click="saveProfile" aria-label="Save edited employee profile">
            Save
          </button>
        </div>
      </div>
    </div>
    <div v-else>
      <p>Loading profile...</p>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

interface Profile {
  user: { username: string; first_name: string; last_name: string }
  id_number: string
  phone: string
  profession: string
  experience: string
  avatar: string
}

export default {
  setup() {
    const profile = ref<Profile | null>(null)
    const route = useRoute()
    const username = route.params.username as string

    const fetchProfile = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/accounts/profile/${username}/`)
        profile.value = response.data
      } catch (error) {
        console.error('Error al obtener el perfil:', error)
      }
    }

    const saveProfile = async () => {
      try {
        await axios.post(
          `http://127.0.0.1:8000/api/accounts/profile/${username}/edit/`,
          {
            first_name: profile.value?.user.first_name,
            last_name: profile.value?.user.last_name,
            id_number: profile.value?.id_number,
            phone: profile.value?.phone,
            profession: profile.value?.profession,
            experience: profile.value?.experience,
          },
          {
            headers: { 'Content-Type': 'application/json' },
          },
        )
        alert('Profile saved successfully')
      } catch (error) {
        console.error('Error saving profile:', error)
        alert('Error saving profile')
      }
    }

    onMounted(fetchProfile)

    return { profile, saveProfile }
  },
}
</script>

<style scoped>
.profile-edit-container {
  width: 100vw;
  margin: 65px auto 0;
  padding: 20px;
  padding-bottom: 100px;
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

.profile-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}

.profile-form label {
  display: block;
  margin: 10px 0 5px;
}

.profile-form input,
.profile-form textarea {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.profile-form button {
  padding: 10px 20px;
  background-color: #0d7ba6;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.profile-form button:hover {
  background-color: #0a6e92;
}
</style>
