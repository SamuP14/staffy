import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
    username: '',
    userId: null as number | null,
    avatar: '',
  }),
  actions: {
    init() {
      const saved = localStorage.getItem('auth')
      if (saved) {
        const data = JSON.parse(saved)
        this.username = data.username
        this.userId = data.userId
        this.isLoggedIn = data.isLoggedIn
        this.avatar = data.avatar
      }
    },
    async login(username: string, password: string) {
      try {
        const res = await axios.post('http://localhost:8000/api/accounts/login/', {
          username,
          password,
        }, { withCredentials: true })
        this.isLoggedIn = true
        this.username = res.data.username
        this.userId = res.data.user_id
        this.avatar = res.data.avatar
        localStorage.setItem('auth', JSON.stringify({
          username: this.username,
          userId: this.userId,
          isLoggedIn: this.isLoggedIn,
          avatar: this.avatar,
        }))
        return true
      } catch (e) {
        console.log(e)
        this.isLoggedIn = false
        return false
      }
    },
    async logout() {
      try {
        await axios.post('http://localhost:8000/api/accounts/logout/', {}, { withCredentials: true })
      } catch (e) {
        console.error('Logout error', e)
      } finally {
        this.username = ''
        this.userId = null
        this.isLoggedIn = false
        localStorage.removeItem('auth')
      }
    }
  },
})
