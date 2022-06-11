<template>
  <q-page>
    <div class="column" style="margin: 10px">
      <div class="text-h4 text-weight-bold q-mb-xl" style="text-align: center; margin: 15px">
        신규 비교과 프로그램 등록
      </div>
      <q-form @submit="onSubmit" @reset="onReset" class="col-12">
        <div class="row">
          <q-uploader class="full-width" url="http://localhost:4444/upload" color="teal" filled accept=".jpg, image/*"/>
        </div>
        <div class="row" style="margin-top: 20px">
          <div class="text-h6 text-weight-bold col-4 q-mt-xs q-pr-xs q-mb-md" style="text-align: center">
            강의명
          </div>
          <div class="col-8">
            <q-input outlined dense v-model="name"  />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 q-mt-xs q-pr-xs q-mb-md" style="text-align: center">
            모집 대상
          </div>
          <div class="q-mb-xs col-8">
            <q-select
              dense
              outlined
              v-model="group"
              :options="groups"
              option-value="id"
              option-label="name"
              label="모집 대상"
              multiple/>
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 q-mt-xs q-pr-xs q-mb-md" style="text-align: center">
            대상 학년
          </div>
          <div class="q-mb-xs col-8">
            <q-select
              dense
              outlined
              v-model="grade"
              :options="grades"
              option-value="id"
              option-label="name"
              label="대상 학년"
              emit-value
              map-options
              multiple/>
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 q-mt-xs q-pr-xs q-mb-md" style="text-align: center">
            대상 성별
          </div>
          <div class="q-mb-xs col-8">
            <q-select
              dense
              outlined
              v-model="gender"
              :options="genders"
              option-value="id"
              option-label="name"
              label="대상 성별"
              emit-value
              map-options
            />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 q-mt-xs q-pr-xs q-mb-md" style="text-align: center">
            대상 학과
          </div>
          <div class="q-mb-xs col-8">
            <q-select
              dense
              outlined
              v-model="major"
              :options="majors"
              option-value="id"
              option-label="name"
              label="대상 학과"
              emit-value
              map-options
              multiple
            />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            시작 일시
          </div>
          <div class="col-4">
            <q-input dense v-model="startDate" filled type="date" name="시작 날짜" />
          </div>
          <div class="col-4" style="padding-inline-start: 5px">
            <q-input dense v-model="startTime" filled type="time" name="시작 시간" />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            종료 일시
          </div>
          <div class="col-4">
            <q-input dense v-model="endDate" filled type="date" name="종료 날짜" />
          </div>
          <div class="col-4" style="padding-inline-start: 5px">
            <q-input dense v-model="endTime" filled type="time" name="종료 시간" />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            신청 시작 일시
          </div>
          <div class="col-4">
            <q-input dense v-model="applyStartDate" filled type="date" name="시작 날짜" />
          </div>
          <div class="col-4" style="padding-inline-start: 5px">
            <q-input dense v-model="applyStartTime" filled type="time" name="시작 시간" />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            신청 종료 일시
          </div>
          <div class="col-4">
            <q-input dense v-model="applyEndDate" filled type="date" name="종료 날짜" />
          </div>
          <div class="col-4" style="padding-inline-start: 5px">
            <q-input dense v-model="applyEndTime" filled type="time" name="종료 시간" />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            진행 장소
          </div>
          <div class="col-8">
            <q-input
              dense
              outlined
              v-model="place"
              label="진행 장소"
            />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            진행 개요
          </div>
          <div class="col-8">
            <q-input dense outlined label="진행 개요" v-model="description" />
          </div>
        </div>

        <q-separator color="black" />

        <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md" style="text-align: center; margin-top: 10px">
          강사/주관기관 정보 등록
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            이름
          </div>
          <div class="col-8">
            <q-input dense outlined label="강사/주관 기관명" v-model="teacher" />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            이메일
          </div>
          <div class="col-8">
            <q-input dense outlined label="강사/주관 기관 이메일" v-model="teacherEmail" />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            전화번호
          </div>
          <div class="col-8">
            <q-input dense outlined label="강사/주관 기관 전화번호" v-model="teacherPhone" />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            신분
          </div>
          <div class="col-8">
            <q-input dense outlined label="강사/주관 기관 신분" v-model="teacherGroup" />
          </div>
        </div>

        <q-separator color="black" inset />

        <div class="row margin-auto" style="margin-top: 10px">
          <div class="text-h6 text-weight-bold col-4 q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            참여 포인트 :
          </div>
          <div class="col-8" style="max-height: 300px; text-align: left">
            <q-input dense outlined v-model.number="mileage" type="number"/>
          </div>
        </div>

        <div class="row">
          <q-btn
            class="col-12"
            padding="xs 100px"
            size="25px"
            label="등록하기"
            type="submit"
            color="dark"
          />
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<script>
import { useQuasar } from 'quasar';
import {ref} from 'vue';
import {api} from "../boot/axios";

export default {
  name: 'CreateProgramPage',
  setup() {
    const groups = ['무관', '재학생', '졸업생', '교직원'];
    const grades = ['무관', '1학년', '2학년', '3학년', '4학년 이상'];
    const genders = ['무관', '남성', '여성'];
    const majors = [
      { name: '기계공학과' },
      { name: '로봇공학과' },
      { name: '산업경영공학과' },
      { name: '전자공학부' },
      { name: '재료화학공학과' },
      { name: '생명나노공학과' },
      { name: '건축학부' },
      { name: '건설환경플랜트공학과' },
      { name: '교통물류공학과' },
      { name: '국방정보공학과' },
      { name: '융합공학과' },
      { name: '스마트융합공학부' },
      { name: '소프트웨어학부' },
      { name: 'ICT융합학부' },
      { name: '인공지능학과' },
      { name: '약학과' },
      { name: '응용수학과' },
      { name: '응용물리학과' },
      { name: '화학분자공학과' },
      { name: '분자생명과학과' },
      { name: '해양융합공학과' },
      { name: '나노광전자학과' },
      { name: '한국언어문학과' },
      { name: '문화인류학과' },
      { name: '문화콘텐츠학과' },
      { name: '중국학과' },
      { name: '일본학과' },
      { name: '영미언어문화학과' },
      { name: '프랑스학과' },
      { name: '정보사회미디어학과' },
      { name: '광고홍보학과' },
      { name: '신문방송학과' },
      { name: '정보사회학과' },
      { name: '경제학부' },
      { name: '경영학부' },
      { name: '보험계리학과' },
      { name: '회계세무학과' },
      { name: '주얼리·패션디자인학과' },
      { name: '산업디자인학과' },
      { name: '커뮤니케이션디자인학과' },
      { name: '영상디자인학과' },
      { name: '스포츠과학부' },
      { name: '무용예술학과' },
      { name: '실용음악학과' },
    ]

    const $q = useQuasar();
    const name = ref('');
    const group = ref([]);
    const grade = ref([]);
    const gender = ref('무관');
    const major = ref([]);

    const startDate = ref(null);
    const startTime = ref(null);
    const endDate = ref(null);
    const endTime = ref(null);

    const applyStartDate = ref(null);
    const applyStartTime = ref(null);
    const applyEndDate = ref(null);
    const applyEndTime = ref(null);

    const place = ref('');
    const description = ref('');

    const teacher = ref('');
    const teacherEmail = ref('');
    const teacherPhone = ref('');
    const teacherGroup = ref('');

    const mileage = ref(-1);

    return {
      name, group, grade, gender, major, startDate, startTime, endDate, endTime,
      applyStartDate, applyStartTime, applyEndDate, applyEndTime,
      place, description, teacher, teacherEmail, teacherPhone, teacherGroup, mileage,
      groups, genders, grades, majors,
      onSubmit() {
        if(name.value.length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '강의 이름이 비어있습니다.',
          });
        }

        if(group.value.length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '모집 대상이 비어있습니다.',
          });
        }

        if (grade.value.length === 0) {
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '모집 학년이 비어있습니다.',
          });
        }

        if (major.value.length === 0) {
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '모집 전공이 비어있습니다.',
          });
        }

        if(startDate.value === null || startTime.value === null){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '시작 일시가 비어있습니다.',
          });
        }

        if(endDate.value === null || endTime.value === null){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '종료 일시가 비어있습니다.',
          });
        }

        if(`${startDate.value} ${startTime.value}` > `${endDate.value} ${endTime.value}`){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '시작 일시가 종료 일시보다 빠릅니다.',
          });
        }

        if(applyStartDate.value === null || applyStartTime.value === null){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '신청 시작 일시가 비어있습니다.',
          });
        }


        if(applyEndDate.value === null || applyEndTime.value === null){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '신청 종료 일시가 비어있습니다.',
          });
        }

        if(`${applyStartDate.value} ${applyStartTime.value}` > `${applyEndDate.value} ${applyEndTime.value}`){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '신청 시작 일시가 종료 일시보다 빠릅니다.',
          });
        }

        if(place.value.length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '진행 장소가 비어있습니다.',
          });
        }

        if(teacher.value.length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '강사 이름이 비어있습니다.',
          });
        }

        if(teacherEmail.value.length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '강사 이메일이 비어있습니다.',
          });
        }

        if(teacherPhone.value.length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '강사 연락처가 비어있습니다.',
          });
        }

        if(mileage.value < 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '마일리지가 비어있습니다.',
          });
        }

        const data = {
          name: name.value,
          group: group.value,
          grade: grade.value,
          gender: gender.value,
          major: major.value,
          startDate: startDate.value,
          startTime: startTime.value,
          endDate: endDate.value,
          endTime: endTime.value,
          applyStartDate: applyStartDate.value,
          applyStartTime: applyStartTime.value,
          applyEndDate: applyEndDate.value,
          applyEndTime: applyEndTime.value,
          place: place.value,
          description: description.value,
          teacherName: teacher.value,
          teacherEmail: teacherEmail.value,
          teacherPhone: teacherPhone.value,
          teacherGroup: teacherGroup.value,
          mileage: mileage.value
        };

        api.post("/program", JSON.stringify(data)).then(
          () => {
            $q.notify({
              color: 'green-5',
              textColor: 'white',
              message: '정상적으로 저장되었습니다.',
            });
          }
        )
      },

      onReset() {
        name.value = null;
        age.value = null;
        accept.value = false;
      },
    };
  },
};
</script>

<style>
.margin-auto {
  margin-left: auto;
  margin-right: auto;
}
</style>
