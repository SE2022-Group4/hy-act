import {defineStore} from 'pinia';
import {api} from 'boot/axios';
import {DepartmentItem} from 'src/models/department.item';

export type DepartmentState = {
  departmentList: DepartmentItem[];
}

export const useProgramDepartmentStore = defineStore({
  id: 'programDepartmentStore',
  state: () => ({departmentList: []} as DepartmentState),
  actions: {
    async fetchDepartmentList() {
      const response = await api.get('/programs/department', {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}})
      this.departmentList = response.data;
    }
  }
})
