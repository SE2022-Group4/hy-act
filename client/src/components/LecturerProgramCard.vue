<template>
  <q-card class="full-width">
    <q-card-section>
      <div class="row">
        <div class="text-h6 col-11" style="text-align: center">
          {{program.name}}
        </div>
      </div>
    </q-card-section>
    <q-separator />
    <div class="row">
      <q-card-section class="col-3">
        <q-img :src="program.thumbnail_url" ratio="1" />
      </q-card-section>
      <q-card-section class="col-9">
        <q-list>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">모집 학년</q-item-section>
            <q-item-section class="col-8">{{program.target_grade !== "0" ? `${program.target_grade}학년` : '전체'}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">모집 성별</q-item-section>
            <q-item-section class="col-8">{{sexDict[program.sex]}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">신청 날짜</q-item-section>
            <q-item-section class="col-8">{{applyDate}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">진행 날짜</q-item-section>
            <q-item-section class="col-8">{{targetDate}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">진행 장소</q-item-section>
            <q-item-section class="col-8">{{program.location}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-4" style="font-weight: bold">모집 상태</q-item-section>
            <q-item-section class="col-8">{{program.recent_applicant_count}} / {{program.max_applicant_count}}</q-item-section>
          </q-item>
          <q-item>
            <q-item-section class="col-12">
              <q-btn rounded style="background-color: #5B5D60; color: white; padding: 15px" @click="goToAttendancePage">
                출석 관리하기
              </q-btn>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </div>
  </q-card>
</template>

<script>

import {api} from 'boot/axios';

export default {
  name: 'LecturerProgramCard',
  props: {
    program: {
      type: Object,
      required: true
    }
  },
  setup(props, {emit}) {
    const zero = num => num < 10 && num >= 0 ? '0' + num : num;
    const sexDict = {0: '전체', 1: '남자', 2: '여자'};
    const koreanDate = date => `${date.getFullYear()}년 ${zero(date.getMonth() + 1)}월 ${zero(date.getDate())}일 ${zero(date.getHours())}:${zero(date.getMinutes())}`;
    const targetDate = `${koreanDate(new Date(props.program.program_start_at * 1000))} ~ ${koreanDate(new Date(props.program.program_end_at * 1000))}`
    const applyDate = `${koreanDate(new Date(props.program.apply_start_at * 1000))} ~ ${koreanDate(new Date(props.program.apply_end_at * 1000))}`
    function goToAttendancePage() {
      window.location.href = `/program/${props.program.id}/attendance/manage`;
    }

    return {sexDict, applyDate, targetDate, goToAttendancePage}
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
