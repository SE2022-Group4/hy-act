import {MileageUsageItem} from 'src/models/mileage.usage.item';
import {defineStore} from 'pinia';
import {api} from 'boot/axios';

export type MileageUsageListStore = {
  mileageUsageList: MileageUsageItem[];
}

export const useMileageUsageListStore = defineStore({
  id: 'mileageUsageListStore',
  state: () => ({mileageUsageList: []} as MileageUsageListStore),
  actions: {
    async fetchMileageUsageList() {
      const response = await api.get('/mileage/usage');
      this.mileageUsageList = response.data;
    }
  }
})
