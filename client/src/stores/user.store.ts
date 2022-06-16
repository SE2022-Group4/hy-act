import {UserItem} from 'src/models/user.item';
import {defineStore} from 'pinia';
import {api} from 'boot/axios';

export type UserState = {
  user: UserItem;
  success: boolean;
}

export const useUserStore = defineStore({
  id: 'userStore',
  state: () => ({user: {
    username: '', email: '', real_name: '', groups: [], telephone: '', departments: [], majors: []
  }, success: true} as UserState),
  actions: {
    async fetchUser() {
      try{
        const response = await api.get('/user/info', {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}})
        console.log(response.data)
        this.user = response.data
      } catch (e) {
        console.log(e);
        this.success = false;
        window.location.href = '/login'
      }
    },
    async logout() {
      this.user = {
        username: '', email: '', real_name: '', groups: [], telephone: '', departments: [], majors: []
      } as UserItem;
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
  },
})
