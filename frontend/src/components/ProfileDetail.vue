<template>
  <div class="profile-container" role="main" aria-label="User profile">
    <div v-if="profile" class="profile-card">
      <div class="profile-header">
        <div class="profile-avatar-wrapper" @click="triggerAvatarUpload">
          <img :src="profile.avatar" alt="Avatar" class="profile-avatar" />
        </div>
        <input type="file" ref="avatarInput" @change="handleAvatarChange" accept="image/*" style="display: none" />
        <h2>@{{ profile.user.username }}</h2>
        <h3>{{ profile.user.first_name }} {{ profile.user.last_name }}</h3>
      </div>

      <button @click="showRoleForm = !showRoleForm" class="btn btn-primary mt-4"
        aria-label="Toggle role form visibility">
        {{ showRoleForm ? 'Cancel' : 'Add roles' }}
      </button>

      <div class="profile-details">
        <p><strong>ID Number:</strong> {{ profile.id_number }}</p>
        <p><strong>Phone:</strong> {{ profile.phone }}</p>
        <p><strong>Profession:</strong> {{ profile.profession || 'Not specified' }}</p>
        <p><strong>Experience:</strong> {{ profile.experience || 'No experience provided' }}</p>

        <RoleList :profileId="profile.user.username" :filteredRoles="userRoles" @role-deleted="fetchProfile"
          class="mt-4 full-width-role-list" />

        <div v-if="showRoleForm" class="mt-3 show-form" style="background: #f0f0f0; padding: 15px; border-radius: 8px;">
          <label for="multi-role-select" class="form-label"><strong>Select one or more roles:</strong></label>
          <select id="multi-role-select" v-model="selectedRoles" multiple size="5" class="form-control"
            aria-label="Multiple role selector">
            <option v-for="role in availableRoles" :key="role.id" :value="role.code">
              {{ role.name }}
            </option>
          </select>
          <button @click="addRoles" class="btn btn-success mt-3" aria-label="Confirm selected roles">Confirm</button>
        </div>
      </div>
    </div>

    <div v-else>
      <p>Loading profile...</p>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import RoleList from './RoleList.vue';

interface Profile {
  user: { username: string; first_name: string; last_name: string };
  id_number: string;
  phone: string;
  profession: string;
  experience: string;
  avatar: string;
  role: string[];
}

interface Role {
  id: string;
  code: string;
  name: string;
}

export default {
  components: { RoleList },
  setup() {
    const profile = ref<Profile | null>(null);
    const allRoles = ref<Role[]>([]);
    const avatarInput = ref<HTMLInputElement | null>(null);
    const selectedRoles = ref<string[]>([]);
    const showRoleForm = ref(false);

    const route = useRoute();
    const username = route.params.username as string;

    const fetchProfile = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/accounts/profile/${username}/`);
        profile.value = response.data;
      } catch (error) {
        console.error('Error al obtener el perfil:', error);
      }
    };

    const fetchAllRoles = async () => {
      try {
        const response = await axios.get<Role[]>('http://127.0.0.1:8000/api/accounts/role/');
        allRoles.value = response.data;
      } catch (error) {
        console.error('Error al obtener los roles:', error);
      }
    };

    const triggerAvatarUpload = () => {
      avatarInput.value?.click();
    };

    const handleAvatarChange = async (event: Event) => {
      const input = event.target as HTMLInputElement;
      if (input.files?.[0]) {
        const resizedFile = await resizeImage(input.files[0]);
        const avatarBase64 = await toBase64(resizedFile);
        await updateAvatar(avatarBase64);
        fetchProfile();
      }
    };

    const resizeImage = (file: File): Promise<File> => {
      return new Promise((resolve, reject) => {
        const img = new Image();
        const reader = new FileReader();
        reader.onload = (e) => (img.src = e.target?.result as string);
        reader.onerror = reject;

        img.onload = () => {
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          const max = 500;
          let { width, height } = img;

          if (width > height && width > max) {
            height *= max / width;
            width = max;
          } else if (height > max) {
            width *= max / height;
            height = max;
          }

          canvas.width = width;
          canvas.height = height;
          ctx?.drawImage(img, 0, 0, width, height);
          canvas.toBlob(blob => {
            const resizedFile = new File([blob!], file.name, { type: file.type });
            resolve(resizedFile);
          }, file.type);
        };

        img.src = URL.createObjectURL(file);
      });
    };

    const toBase64 = (file: File): Promise<string> =>
      new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result as string);
        reader.onerror = reject;
      });

    const updateAvatar = async (avatarBase64: string) => {
      try {
        await axios.post(`http://127.0.0.1:8000/api/accounts/profile/${username}/edit/`, {
          avatar: avatarBase64,
        }, {
          headers: { 'Content-Type': 'application/json' },
        });
      } catch (error) {
        console.error('Error al actualizar el avatar:', error);
      }
    };

    const userRoles = computed(() => {
      if (!profile.value) return [];
      return allRoles.value.filter(role =>
        profile.value!.role.includes(role.name)
      );
    });

    const availableRoles = computed(() => {
      if (!profile.value) return [];
      return allRoles.value.filter(role =>
        !profile.value!.role.includes(role.name)
      );
    });

    const addRoles = async () => {
      if (selectedRoles.value.length === 0) return;

      try {
        await axios.post(`http://127.0.0.1:8000/api/accounts/profile/${username}/role/add/`, {
          role_codes: selectedRoles.value,
        });
        selectedRoles.value = [];
        showRoleForm.value = false;
        await fetchProfile();
      } catch (error: unknown) {
        console.error('Error al agregar roles:', error);
        if (axios.isAxiosError(error)) {
          console.error('Detalle del error:', error.response?.data);
        } else {
          console.error('Error desconocido:', error);
        }
      }
    };

    onMounted(async () => {
      await fetchAllRoles();
      await fetchProfile();
    });

    return {
      profile,
      avatarInput,
      triggerAvatarUpload,
      handleAvatarChange,
      userRoles,
      selectedRoles,
      availableRoles,
      allRoles,
      fetchProfile,
      addRoles,
      showRoleForm,
    };
  },
};
</script>

<style scoped>
.profile-container {
  width: 100vw;
  margin: 65px auto 0;
  overflow-x: hidden;
  text-align: center;
  margin-bottom: 150px;
}

.profile-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background-color: #f9f9f9;
}

.profile-header {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.profile-avatar-wrapper {
  cursor: pointer;
}

.profile-avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 20px;
}

.profile-details p {
  margin: 10px 0;
}

.profile-details select {
  margin: 10px;
  width: 100%;
}

.show-form {
  background: #f0f0f0;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 100px;
}

.full-width-role-list {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  margin-right: calc(-50vw + 50%);
  padding: 0 20px;
}
</style>
