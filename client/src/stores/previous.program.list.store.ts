import {ProgramItem} from 'src/models/program.item';
import {api} from 'boot/axios';
import {defineStore} from 'pinia';

export type PreviousProgramListStore = {
  previousProgramList: ProgramItem[];
}

export const usePreviousProgramListStore = defineStore({
  id: 'previousProgramListStore',
  state: () => ({previousProgramList: []} as PreviousProgramListStore),
  actions: {
    async fetchPreviousProgramList() {
      const response = await api.get('/program/previous');
      this.previousProgramList = response.data;
    }
  }
})
