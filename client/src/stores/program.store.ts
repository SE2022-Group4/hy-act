import {ProgramItem} from 'src/models/program.item';
import {defineStore} from 'pinia';
import {api} from 'boot/axios';

export type ProgramState = {
  programList: ProgramItem[];
  program: ProgramItem;
}

export const useProgramStore = defineStore({
  id: 'programStore',
  state: () => ({programList: [], program: {}} as ProgramState),
  actions: {
    async fetchProgramList() {
      const response = await api.get('/programs', {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}})
      console.log(response.data)
      this.programList = response.data;
    },
    async fetchProgram(id: string) {
      const response = await api.get(`/programs/${id}`, {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}})
      this.program = response.data;
    }
  }
})
