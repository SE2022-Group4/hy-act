<template>
  <q-card class="full-width">
    <q-card-section>
      <div class="row">
        <div class="text-h6 col-11" style="text-align: center">
          {{program.title}}
        </div>
        <q-btn icon="mdi-magnify" style="background-color: #343a40; color: #E2E6EA" @click="infoDialogOpen"/>
      </div>
    </q-card-section>
    <q-separator />
    <div class="row">
      <q-card-section class="col-3">
        <q-img src="icons/favicon-128x128.png" ratio="1" />
      </q-card-section>
      <q-card-section class="col-9">
        <q-list>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">모집 대상</q-item-section>
            <q-item-section class="col-8">{{program.target_people}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">학년 / 성별</q-item-section>
            <q-item-section class="col-8">{{program.target_grade}} / {{program.target_gender}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">학과</q-item-section>
            <q-item-section class="col-8">{{program.target_major}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">마일리지</q-item-section>
            <q-item-section class="col-8">{{program.mileage}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">날짜</q-item-section>
            <q-item-section class="col-8">{{targetDate}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">장소</q-item-section>
            <q-item-section class="col-8">{{program.place}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">상태</q-item-section>
            <q-item-section class="col-8">{{program.current_people}} / {{program.max_people}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-12">
              <q-btn rounded style="background-color: #5B5D60; color: white; padding: 15px" @click="dialogOpen">
                신청하기
              </q-btn>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </div>
  </q-card>
</template>

<script>
export default {
  name: 'ProgramCard',
  emits: ['dialog-open', 'info-open'],
  props: {
    program: {
      type: Object,
      required: true
    }
  },
  setup(props, {emit}) {
    const zero = num => num < 10 && num >= 0 ? '0' + num : num;
    const koreanDate = date => `${date.getFullYear()}년 ${zero(date.getMonth() + 1)}월 ${zero(date.getDate())}일 ${zero(date.getHours())}:${zero(date.getMinutes())}`;
    const targetDate = `${koreanDate(props.program.start_date)} ~ ${koreanDate(props.program.end_date)}`
    function dialogOpen() {
      emit('dialog-open', props.program);
    }
    function infoDialogOpen() {
      emit('info-open', props.program);
    }
    return {targetDate, dialogOpen, infoDialogOpen}
  }
}
</script>

<style scoped>
div .text-h6 {
  margin: 10px;
}
div .q-item__section {
  text-align: center;
}
</style>
