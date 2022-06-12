import {defineStore} from 'pinia';
import {api} from 'boot/axios';
import {ProgramCategoryItem} from 'src/models/program.category.item';

export type ProgramCategoryState = {
  categoryList: ProgramCategoryItem[];
}

export const useProgramCategoryStore = defineStore({
  id: 'programCategoryStore',
  state: () => ({categoryList: []} as ProgramCategoryState),
  actions: {
    async fetchProgramCategoryList() {
      const response = await api.get('/programs/category', {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}})
      this.categoryList = response.data;
    }
  }
})
