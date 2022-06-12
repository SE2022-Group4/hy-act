<template>
  <q-header elevated style="background-color: #343a40">
    <q-toolbar>
      <q-toolbar-title>비교과 프로그램 신청</q-toolbar-title>
      <q-input v-model="searchKeyword" dense color="white">
        <template v-slot:prepend>
          <q-icon name="mdi-magnify" color="white" />
        </template>
      </q-input>
    </q-toolbar>
    <q-toolbar>
      <div class="row full-width">
        <div class="col-2 items-center">모집 학과</div>
        <div class="col-2">
          <q-select
            dense
            label="학과 선택"
            label-color="white"
            dark
            v-model="searchTargetMajor"
            :options="targetMajorList"
            dropdown-icon="mdi-menu-down"/>
        </div>
        <div class="col-2 items-center">모집 성별</div>
        <div class="col-2">
          <q-select
            dense
            label="성별 선택"
            label-color="white"
            dark
            v-model="searchTargetGender"
            :options="targetGenderList"
            dropdown-icon="mdi-menu-down"/>
        </div>
        <div class="col-2 items-center">모집 학년</div>
        <div class="col-2">
          <q-select
            dense
            label="학년 선택"
            dark
            v-model="searchTargetGrade"
            :options="targetGradeList"
            dropdown-icon="mdi-menu-down"
          />
        </div>
      </div>
    </q-toolbar>
  </q-header>
  <q-page class="column items-center justify-start" style="margin-left: 10px; margin-right: 10px; margin-top: 10px">
    <ProgramCard
      v-for="programItem in programItemList"
      v-show="programItem.title.includes(searchKeyword) &&
              (programItem.target_grade.includes(searchTargetGrade[0]) || searchTargetGrade === '전체') &&
              (programItem.target_gender.includes(searchTargetGender) || searchTargetGender === '전체') &&
              (programItem.target_major.includes(searchTargetMajor) || searchTargetMajor === '전체')"
      :program="programItem" style="margin-bottom: 10px"
      @dialog-open="openDialog"
      @info-open="openInfoDialog"
    />
    <div>
      <q-dialog v-model="dialogOpened" class="full-width">
        <ProgramApplyDialog :program="programItem"/>
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
import ProgramInfoDialog from 'components/ProgramInfoDialog.vue';
import ProgramApplyDialog from 'components/ProgramApplyDialog.vue';

export default defineComponent({
  name: 'IndexPage',
  components: { ProgramInfoDialog, ProgramCard, ProgramApplyDialog },
  inheritAttrs: false,
  setup () {
    const programStore = useProgramStore();
    programStore.fetchProgramList();
    const targetMajorList = Array.from(new Set(programStore.programList.map(item => item.target_major))).filter(item => item !== '전체').sort();
    targetMajorList.unshift('전체')
    const targetGenderList = ['전체', '남성', '여성']
    const targetGradeList = ['전체', '1학년', '2학년', '3학년', '4학년 이상'];
    const dialogOpened = ref(false);
    const infoDialogOpened = ref(false);
    const programItem = ref({});
    function openDialog (program: object) {
      dialogOpened.value = true;
      programItem.value = program;
    }

    function openInfoDialog (program: object) {
      infoDialogOpened.value = true;
      programItem.value = program;
    }
    return {
      programItem,
      openDialog,
      dialogOpened,
      openInfoDialog,
      infoDialogOpened,
      programItemList: programStore.programList,
      targetMajorList,
      targetGenderList,
      targetGradeList,
      searchKeyword: ref(''),
      searchTargetMajor: ref('전체'),
      searchTargetGender: ref('전체'),
      searchTargetGrade: ref('전체')
    };
  }
});
</script>
