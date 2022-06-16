import {defineStore} from 'pinia';
import {api} from 'boot/axios';
import {DepartmentItem} from 'src/models/department.item';
import {LecturerItem} from "src/models/lecturer.item";

export type LecturerStore = {
  lecturerList: LecturerItem[];
}

export const useLecturerStore = defineStore({
  id: 'lecturerStore',
  state: () => ({lecturerList: []} as LecturerStore),
  actions: {
    async fetchLectureList(search: string) {
      const response = await api.get(`/programs/lecturer?name=${search}`, {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}})
      this.lecturerList = response.data;
    }
  }
})
