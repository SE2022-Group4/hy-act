<template>
  <q-header elevated style="background-color: #343a40">
    <q-toolbar>
      <q-toolbar-title>비교과 프로그램 신청 목록</q-toolbar-title>
    </q-toolbar>
  </q-header>
  <q-page class="column items-center justify-start" style="margin-left: 10px; margin-right: 10px; margin-top: 10px">
    <MyProgramCard
      v-for="item in programItemList"
      :program="item" style="margin-bottom: 10px"
      @cancel-program="cancelProgram"
    />
  </q-page>
</template>
<style scoped>
div .items-center {
  display: flex;
  justify-content: center;
}

</style>
<script lang="ts">
import {defineComponent, ref} from 'vue';
import {useUserStore} from 'stores/user.store';
import {useMyProgramListStore} from 'stores/my.program.list.store';
import MyProgramCard from 'components/MyProgramCard.vue';
import {ProgramItem} from "src/models/program.item";

export default defineComponent({
  name: 'MyProgramPage',
  components: { MyProgramCard },
  inheritAttrs: false,
  setup () {
    const dialogOpened = ref(false);
    const programItem = ref({});

    const userStore = useUserStore();
    const user = ref(userStore.user);
    userStore.$subscribe(() => {
      user.value = userStore.user;
    });

    const programStore = useMyProgramListStore();
    if(user.value.groups.filter(item => item.name === 'admin').length !== 0) {
      programStore.fetchMyProgramListAdmin();
    } else if(user.value.groups.filter(item => item.name === 'lecturer').length !== 0) {
      programStore.fetchMyProgramListLecturer();
    } else {
      programStore.fetchMyProgramListStudent();
    }
    const programItemList = ref(programStore.programList);
    programStore.$subscribe(() => {
      programItemList.value = programStore.programList
    })

    function cancelProgram() {
      programStore.fetchMyProgramListStudent();
    }

    return {
      user,
      programItem,
      dialogOpened,
      programItemList,
      cancelProgram
    };
  }
});
</script>
