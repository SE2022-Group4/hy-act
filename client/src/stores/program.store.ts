import {ProgramItem} from 'src/models/program.item';
import {defineStore} from 'pinia';
import {api} from 'boot/axios';

export type ProgramState = {
  programList: ProgramItem[];
}

export const useProgramStore = defineStore({
  id: 'programStore',
  state: () => ({programList: []} as ProgramState),
  actions: {
    async fetchProgramList() {
      const response = await api.get('/programs', {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}})
      this.programList = response.data;
    }
  }
})
