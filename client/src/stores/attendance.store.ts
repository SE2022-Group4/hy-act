import {defineStore} from 'pinia';
import {api} from 'boot/axios';
import {AttendanceItem} from 'src/models/attendance.item';

export type AttendanceState = {
  attendance: AttendanceItem;
}

export const useAttendanceStore = defineStore({
  id: 'attendanceStore',
  state: () => ({attendance: {}} as AttendanceState),
  actions: {
    async fetchAttendance(id: string) {
      const response = await api.get(`/programs/${id}/attendance/`, {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}})
      this.attendance = response.data;
    }
  }
})
