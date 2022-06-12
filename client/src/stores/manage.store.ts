import {ProgramItem} from 'src/models/program.item';
import {defineStore} from 'pinia';
import {api} from 'boot/axios';

export type ManageProgramStore = {
  programList: ProgramItem[];
}

export const useManageProgramStore = defineStore({
  id: 'manageProgramStore',
  state: () => ({programList: []} as ManageProgramStore),
  actions: {
    async fetchProgramList() {
      const response = await api.get('/manage');
      this.programList = response.data;
    }
  }
});
