import './assets/main.css'

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { useAuthStore } from './stores/auth'

const app = createApp(App)
const pinia = createPinia()


app.use(pinia)
app.use(router)

const auth = useAuthStore()
auth.init()

app.mount('#app')
