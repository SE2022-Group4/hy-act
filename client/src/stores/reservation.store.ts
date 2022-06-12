import {ProgramItem} from 'src/models/program.item';
import {defineStore} from 'pinia';
import {api} from 'boot/axios';

export type ReservationStore = {
  reservationList: ProgramItem[];
}

export const useReservationStore = defineStore({
  id: 'reservationStore',
  state: () => ({reservationList: []} as ReservationStore),
  actions: {
    async fetchReservationList() {
      const response = await api.get('/reservations');
      this.reservationList = response.data;
    }
  }
})
