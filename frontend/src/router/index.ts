import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '../stores/auth'
import WorkerList from '../components/WorkerList.vue';
import RoleList from '../components/RoleList.vue';
import TaskList from '../components/TaskList.vue';
import Profile from '../components/ProfileDetail.vue';
import Contact from '../components/ContactForm.vue';
import Login from '../components/LoginForm.vue';
import AddEmployee from '../components/AddEmployeeForm.vue';
import EditEmployee from '../components/EditEmployeeForm.vue';
import AddRole from '../components/AddRoleForm.vue';
import AddTask from '../components/AddTaskForm.vue';
import EditTask from '../components/EditTaskForm.vue';
import Task from '../components/TaskDetails.vue'

const routes = [
  { path: '/', redirect: '/employees' },
  { path: '/login', name: 'Login', component: Login },

  { path: '/employees', name: 'WorkerList', component: WorkerList, meta: { requiresAuth: true } },
  { path: '/employees/:username', name: 'Profile', component: Profile, meta: { requiresAuth: true } },
  { path: '/employees/add', name: 'AddEmployee', component: AddEmployee, meta: { requiresAuth: true } },
  { path: '/employees/:username/edit', name: 'EditEmployee', component: EditEmployee, meta: { requiresAuth: true } },

  { path: '/roles', name: 'RoleList', component: RoleList, meta: { requiresAuth: true } },
  { path: '/roles/add', name: 'AddRole', component: AddRole, meta: { requiresAuth: true } },

  { path: '/tasks', name: 'TaskList', component: TaskList, meta: { requiresAuth: true } },
  { path: '/tasks/:id', name: 'TaskDetail', component: Task, meta: { requiresAuth: true } },
  { path: '/tasks/add', name: 'AddTask', component: AddTask, meta: { requiresAuth: true } },
  { path: '/tasks/:id/edit', name: 'EditTask', component: EditTask, meta: { requiresAuth: true } },

  { path: '/contact', name: 'Contact', component: Contact, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  auth.init()

  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)

  if (requiresAuth && !auth.isLoggedIn) {
    next({ name: 'Login' })
  } else if (to.name === 'Login' && auth.isLoggedIn) {
    next({ name: 'WorkerList' })
  } else {
    next()
  }
})

export default router
