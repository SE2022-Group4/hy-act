import {ProgramItem} from 'src/models/program.item';
import {api} from 'boot/axios';
import {defineStore} from 'pinia';

export type MyProgramListStore = {
  programList: ProgramItem[];
}

export const useMyProgramListStore = defineStore({
  id: 'previousProgramListStore',
  state: () => ({programList: []} as MyProgramListStore),
  actions: {
    async fetchMyProgramListStudent() {
      const response = await api.get('/programs/my/applications/', {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}});
      this.programList = response.data;
    },

    async fetchMyProgramListLecturer() {
      const response = await api.get('/programs/my/instructing-programs/', {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}});
      this.programList = response.data;
    },

    async fetchMyProgramListAdmin() {
      const response = await api.get('/programs/my/managing-programs/', {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}});
      this.programList = response.data;
    }
  }
})
