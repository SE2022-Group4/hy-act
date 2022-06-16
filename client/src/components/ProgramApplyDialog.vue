<template>
  <q-card style="width: 1000px; max-width: 100vw">
    <q-card-section>
      <div class="text-h5" style="text-align: center">
        <strong>신청 정보</strong>
      </div>
    </q-card-section>

    <q-separator color="gray" size="2px" inset></q-separator>
    <q-card-section style="padding: 0; max-height: 65vh" class="scroll">
      <div class="row">
        <!--Program Image-->
        <div class="col-6">
          <q-img :src="program.thumbnail_url" spinner-color="white" style="max-height: 300px; max-width: 350px"></q-img>
        </div>
        <!-- Program Info -->
        <div class="col-6">
          <div class="text-h8" style="text-align: center; font-size: 16px"><strong>{{ program.title }}</strong></div>
          <div class="text-h8" style="
              text-align: center;
              font-size: 16px;
              padding: 12px;
              line-height: 25px;
            "><strong>날짜</strong></div>
          <p style="text-align: center; line-height: 15px">시작 : {{ startDate }}</p>
          <p style="text-align: center; line-height: 15px">종료 : {{ endDate }}</p>
          <div class="text-h8" style="
              text-align: center;
              font-size: 16px;
              padding: 12px;
              line-height: 25px;
            "><strong>장소</strong></div>
          <p style="text-align: center; line-height: 15px">
            {{ program.location }}
          </p>
        </div>
      </div>

      <q-separator color="gray" size="2px" inset></q-separator>

      <!--Applicant Info-->
      <div class="row">
        <div class="col">
          <div
            class="text-h8"
            style="
              text-align: center;
              font-size: 15px;
              padding: 4px;
              line-height: 25px;
            "
          >
            <strong>신청자 정보</strong>
          </div>
          <p style="padding-top: 12px; line-height: 15px">
            <strong>이름 &nbsp;&nbsp; : &nbsp;&nbsp; </strong> {{ user.real_name }}
          </p>
          <p style="line-height: 15px">
            <strong>학과 &nbsp;&nbsp; : &nbsp;&nbsp; </strong>
            {{ user.majors[0].name }}
          </p>
          <p style="line-height: 15px">
            <strong>전화번호 &nbsp;&nbsp; : &nbsp;&nbsp; </strong>
            {{ user.telephone }}
          </p>
        </div>
        <q-separator
          color="gray"
          size="2px"
          spaced="12px"
          inset
          vertical
        ></q-separator>
        <!-- Get Confirm -->
        <div class="col">
          <div
            class="text-h8"
            style="
              text-align: center;
              font-size: 15px;
              padding: 4px;
              line-height: 25px;
            "
          >
            <strong>신청 확인</strong>
          </div>

          <p
            style="padding-top: 12px; text-align: center; line-height: 20px"
          >
            - 비교과 참여인증을 위한 개인정보 제공에 동의합니다.
          </p>
          <p style="text-align: center; line-height: 20px">
            - 개인 정보는 2년 보관 후 파기됩니다.
          </p>
          <p style="text-align: center; line-height: 20px">
            - 참여 완료 시 마일리지 {{ program.mileage }}포인트가 제공됩니다.
          </p>
        </div>
      </div>
    </q-card-section>
    <q-separator inset></q-separator>
    <q-card-actions align="right">
      <div class="row" style="padding: 0">
        <q-btn
          class="items-center"
          unelevated
          rounded
          color="grey-9"
          label="&nbsp;&nbsp;신청하기&nbsp;&nbsp;"
          @click="apply"
        ></q-btn>
      </div>
      <q-btn flat label="닫기" color="primary" v-close-popup></q-btn>
    </q-card-actions>
  </q-card>
</template>

<style scoped>
.row > div {
  padding: 10px 15px;
  background: rgb(255, 255, 255);
  border: 1px solid rgb(255, 255, 255);
}

.row + .row {
  margin-top: 1rem;
}
</style>

<script>
import { defineComponent } from 'vue';
import {api} from 'boot/axios';
import {useQuasar} from 'quasar';

export default defineComponent({
  name: 'ProgramApplyDialog',
  props: {
    user: {
      type: Object,
      required: true,
    },
    program: {
      type: Object,
      required: true,
    },
  },
  emits: ['close'],
  setup(props, {emit}) {
    const $q = useQuasar();
    const zero = num => num < 10 && num >= 0 ? '0' + num : num;
    const koreanDate = date => `${date.getFullYear()}년 ${zero(date.getMonth() + 1)}월 ${zero(date.getDate())}일 ${zero(date.getHours())}:${zero(date.getMinutes())}`;
    const startDate = koreanDate(new Date(props.program.program_start_at * 1000));
    const endDate = koreanDate(new Date(props.program.program_end_at * 1000));
    async function apply () {
      api.post(`/programs/${props.program.id}/apply/`, {},{headers: {'Authorization': `Token ${localStorage.getItem('token')}`}}).then(
        res => {
          if(res.status === 200) {
            $q.notify({
              color: 'green-5',
              textColor: 'white',
              message: '정상적으로 신청되었습니다.',
            });
            emit('close');
          }
        },
        err => {
          if(err.response.status === 400) {
            $q.dialog({
              title: '신청 실패',
              message: '이미 신청한 프로그램입니다.',
              color: 'negative',
              buttons: [
                {
                  label: '확인',
                  color: 'negative',
                  handler: () => {
                    emit('close');
                  },
                },
              ],
            });
          } else {
            $q.notify({
              color: 'red-5',
              textColor: 'white',
              message: '신청에 실패하였습니다.',
            });
          }
        }
      )
    }
    return {
      startDate,
      endDate,
      apply,
    };
  },
});
</script>
