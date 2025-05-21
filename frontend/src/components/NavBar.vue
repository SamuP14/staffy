<template>
  <nav class="navbar bg fixed-top border-bottom border-dark" role="navigation" aria-label="Main navigation">
    <div class="container-fluid">
      <a class="navbar-brand d-flex align-items-center gap-2 pt-2" href="" id="logo" @click.prevent>
        <img src="../assets/logo.png" alt="logo.png | Staffy" class="logo">
      </a>
      <div class="d-flex align-items-center flex-grow-1 justify-content-start gap-3">
        <div class="navbar-nav d-flex flex-row gap-3" id="navbar-nav">
          <router-link class="nav-link d-flex align-items-center gap-2 ms-3 .no-hover-bg" to="/employees"
            exact-active-class="active">
            <BIconPersonVcard /> Workers' Profiles
          </router-link>
          <router-link class="nav-link d-flex align-items-center gap-2 ms-3 .no-hover-bg" to="/tasks"
            exact-active-class="active">
            <BIconListTask /> Tasks
          </router-link>
          <router-link class="nav-link d-flex align-items-center gap-2 ms-3 .no-hover-bg" to="/roles"
            exact-active-class="active">
            <BIconPersonBadge /> Roles
          </router-link>
        </div>
      </div>
      <div>
        <router-link v-if="route.path === '/employees'" to="/employees/add"
          class="btn custom-add-btn text-white fw-bold ms-3 d-flex align-items-center gap-2 me-5">
          <BIconPlusSquare /> Add Employee
        </router-link>

        <router-link v-if="route.path === '/roles'" to="/roles/add"
          class="btn custom-add-btn text-white fw-bold ms-3 d-flex align-items-center gap-2 me-5">
          <BIconPlusSquare /> Add Role
        </router-link>
        <router-link v-if="route.path === '/tasks'" to="/tasks/add"
          class="btn custom-add-btn text-white fw-bold ms-3 d-flex align-items-center gap-2 me-5">
          <BIconPlusSquare /> Add Task
        </router-link>
      </div>
      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar"
        aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="offcanvas offcanvas-end" aria-label="Offcanvas navigation" tabindex="-1" id="offcanvasNavbar"
        aria-labelledby="offcanvasNavbarLabel">
        <div class="offcanvas-header">
          <div class="d-flex align-items-center">
            <img src="../assets/logo_bg_2.png" alt="logo_bg_2.png" id="logo_bg">
            <h4 class="offcanvas-title ms-2" id="offcanvasNavbarLabel"> | Easy Staff Solutions</h4>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
            <li class="nav-item" v-if="auth.isLoggedIn">
              <router-link class="nav-link d-flex align-items-center gap-2 custom-hover"
                :to="`/employees/${auth.username}`" exact-active-class="active">
                <img v-if="auth.avatar" :src="auth.avatar" alt="Avatar" class="navbar-avatar" />
                <span>My Profile</span>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link d-flex align-items-center gap-2 custom-hover" to="/contact"
                exact-active-class="active">
                <BIconInfoSquare /> Contact Us
              </router-link>
            </li>
            <li>
              <hr>
            </li>
            <li class="nav-item" v-if="auth.isLoggedIn">
              <button class="nav-link btn custom-hover" @click="handleLogout">
                <BIconBoxArrowInLeft /> Logout
              </button>
            </li>
            <li class="nav-item" v-else>
              <router-link class="nav-link d-flex align-items-center gap-2 custom-hover" to="/login"
                exact-active-class="active">
                <BIconBoxArrowInRight /> Login
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script lang="ts" setup>
import { BIconPersonVcard, BIconListTask, BIconPersonBadge, BIconBoxArrowInRight, BIconBoxArrowInLeft, BIconInfoSquare, BIconPlusSquare } from 'bootstrap-icons-vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const route = useRoute()
const auth = useAuthStore()

const handleLogout = async () => {
  await auth.logout()
}

console.log('Avatar in navbar:', auth.avatar)

</script>

<style scoped>
router-link {
  cursor: pointer;
}

#logo {
  cursor: default;
  text-decoration: none;
  pointer-events: none;
}

#logo_bg {
  width: 100px;
  margin-top: 5px;
}

.logo {
  width: 100px;
}

#navbar-nav .nav-link,
#navbar-nav .nav-link:visited,
#navbar-nav .nav-link:active {
  color: white !important;
}

#navbar-nav .nav-link:hover {
  color: black !important;
  background-color: transparent;
}

.navbar-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  object-fit: cover;
}

.bg {
  background-color: #0D7BA6;
}

.custom-add-btn {
  background-color: #0D7BA6 !important;
  border: none;
}

.custom-add-btn:hover {
  background-color: #095c77 !important;
}
</style>
