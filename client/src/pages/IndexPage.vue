<template>
  <q-header elevated style="background-color: #343a40">
    <q-toolbar>
      <q-toolbar-title>비교과 프로그램 신청</q-toolbar-title>
      <q-input v-model="searchKeyword" dense  standout="bg-teal text-white" color="white" style="color: white">
        <template v-slot:prepend>
          <q-icon name="mdi-magnify" color="white" />
        </template>
      </q-input>
    </q-toolbar>
    <q-toolbar>
      <div class="row full-width">
        <div class="col-6 items-center">모집 분야</div>
        <div class="col-6">
          <q-select
            dense
            label="분야 선택"
            label-color="white"
            dark
            v-model="searchTargetCategory"
            :options="categoryList.map(category => category.name)"
            dropdown-icon="mdi-menu-down"/>
        </div>
      </div>
    </q-toolbar>
  </q-header>
  <q-page class="column items-center justify-start" style="margin-left: 10px; margin-right: 10px; margin-top: 10px">
    <ProgramCard
      v-for="item in programItemList"
      v-show="(searchTargetCategory === '' || item.category === categoryList.filter(category => category.name === searchTargetCategory)[0].id) && (searchKeyword === '' || item.name.includes(searchKeyword))"
      :program="item" style="margin-bottom: 10px"
      @dialog-open="openDialog"
    />
    <div>
      <q-dialog v-model="dialogOpened" class="full-width">
        <ProgramApplyDialog :program="programItem" :user="user" @close="closeDialog"/>
      </q-dialog>
    </div>
  </q-page>
  <div>
    <q-dialog v-model="infoDialogOpened" class="full-width">
      <ProgramInfoDialog :program="programItem"/>
    </q-dialog>
  </div>
</template>
<style scoped>
div .items-center {
  display: flex;
  justify-content: center;
}

</style>
<script lang="ts">
import {defineComponent, ref} from 'vue';
import ProgramCard from 'components/ProgramCard.vue';
import {useProgramStore} from 'stores/program.store';
import ProgramApplyDialog from 'components/ProgramApplyDialog.vue';
import {useQuasar} from 'quasar';
import {ProgramItem} from 'src/models/program.item';
import {useUserStore} from 'stores/user.store';
import {useProgramCategoryStore} from 'stores/program.category.store';

export default defineComponent({
  name: 'IndexPage',
  components: { ProgramCard, ProgramApplyDialog },
  inheritAttrs: false,
  setup () {
    const $q = useQuasar();

    const programStore = useProgramStore();
    programStore.fetchProgramList();
    const dialogOpened = ref(false);
    const programItem = ref({});

    const userStore = useUserStore();
    const user = ref(userStore.user);
    userStore.$subscribe(() => {
      user.value = userStore.user;
      if(user.value.groups.filter(item => item.name === 'admin').length > 0) {
        window.location.href = '/admin';
      } else if (user.value.groups.filter(group => group.name === 'lecturer').length > 0) {
        window.location.href = '/lecturer';
      }
    });

    const programItemList = ref(programStore.programList);
    programStore.$subscribe(() => {
      programItemList.value = programStore.programList
    })

    const programCategoryListStore = useProgramCategoryStore();
    programCategoryListStore.fetchProgramCategoryList();
    const categoryList = ref(programCategoryListStore.categoryList);
    programCategoryListStore.$subscribe(() => {
      categoryList.value = programCategoryListStore.categoryList
    })

    const searchTargetCategory = ref('');
    function openDialog (program: ProgramItem) {
      if(program.max_applicant_count > 0 && program.max_applicant_count <= program.recent_applicant_count) {
        $q.dialog({
          title: '신청 제한',
          message: '제한 인원을 초과하였습니다.',
          color: 'negative'
        })
        return
      }

      const now = new Date();
      if(now.getTime() < program.apply_start_at * 1000 || now.getTime() > program.apply_end_at * 1000) {
        $q.dialog({
          title: '신청 제한',
          message: '신청 기간이 아닙니다.',
          color: 'negative'
        })
        return
      }

      dialogOpened.value = true;
      programItem.value = program;
    }

    function closeDialog () {
      dialogOpened.value = false;
      programStore.fetchProgramList()
    }

    return {
      user,
      programItem,
      dialogOpened,
      openDialog,
      closeDialog,
      programItemList,
      searchTargetCategory,
      categoryList,
      searchKeyword: ref(''),
      searchTargetMajor: ref('전체'),
      searchTargetGender: ref('전체'),
      searchTargetGrade: ref('전체')
    };
  }
});
</script>
