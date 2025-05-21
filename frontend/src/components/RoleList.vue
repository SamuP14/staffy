<template>
  <div class="full-width-container">
    <table class="table table-striped table-hover" role="table" aria-label="Roles table">
      <colgroup>
        <col style="width: 25%;" />
        <col style="width: 50%;" />
        <col style="width: 25%;" />
      </colgroup>
      <thead>
        <tr>
          <th class="tb-bg text-white">Code</th>
          <th class="tb-bg text-white">Name</th>
          <th v-if="!hideActions" class="tb-bg text-white">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="role in filteredRoles || roles" :key="role.code">
          <td>{{ role.code }}</td>
          <td>{{ role.name }}</td>
          <td v-if="!hideActions">
            <button class="btn btn-danger btn-sm" @click="deleteRole(role)" aria-label="Delete role">
              <BIconTrash />
            </button>
          </td>
        </tr>
        <tr v-if="filteredRoles && filteredRoles.length === 0">
          <td colspan="3" class="text-center text-muted" aria-live="polite">No roles assigned</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { BIconTrash } from 'bootstrap-icons-vue';

export interface RolePayload {
  id: string;
  code: string;
  name: string;
}

const props = defineProps<{
  profileId?: string;
  filteredRoles?: RolePayload[];
  hideActions?: boolean;
}>();

const emit = defineEmits<{
  (event: 'update:filteredRoles', roles: RolePayload[]): void;
  (event: 'role-deleted'): void;
}>();

const roles = ref<RolePayload[]>([]);

const fetchRoles = async () => {
  try {
    const response = await axios.get<RolePayload[]>('http://127.0.0.1:8000/api/accounts/role/');
    roles.value = response.data;
  } catch (error) {
    console.error('Error al obtener roles:', error);
  }
};

onMounted(() => {
  if (!props.filteredRoles) {
    fetchRoles();
  }
});

watch(() => props.filteredRoles, (newVal) => {
  if (newVal && newVal.length > 0) {
    roles.value = newVal;
  } else {
    fetchRoles();
  }
});

const deleteRole = async (role: RolePayload) => {
  if (!confirm('Are you sure you want to delete this role?')) return;

  try {
    if (props.profileId) {
      await axios.post(`http://127.0.0.1:8000/api/accounts/profile/${props.profileId}/role/${role.id}/delete/`);

      if (props.filteredRoles) {
        props.filteredRoles.filter(r => r.id !== role.id);
        emit('role-deleted');
      }
    } else {
      await axios.post(`http://127.0.0.1:8000/api/accounts/role/${role.id}/delete/`);

      roles.value = roles.value.filter(r => r.id !== role.id);

      if (props.filteredRoles) {
        const updatedRoles = props.filteredRoles.filter(r => r.id !== role.id);
        emit('update:filteredRoles', updatedRoles);
      }
    }
  } catch (error) {
    console.error('Error al eliminar rol:', error);
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
}

.tb-bg {
  background-color: #0D7BA6;
}

.table th,
.table td {
  border: none;
  padding: 6px 0px;
  font-size: 14px;
  word-wrap: break-word;
  white-space: normal;
  text-align: center;
}

.btn-sm {
  padding: 5px 10px;
}

#btn-add {
  color: white;
}

#btn-add:hover {
  background-color: #0A6E92;
}
</style>
