<template>
  <q-page style="padding: 1rem">
    <div class="text-h6" style="padding-bottom: 1rem">
      비교과 프로그램 출석 확인
    </div>

    <q-separator color="gray" size="2px" inset></q-separator>

    <div class="column">
      <div class="col" style="text-align: center; padding: 1rem">
        <div class="row justify-around">
          <q-card style="width: 95%">
            <q-card-section>
              <p style="padding-top: 0.8rem; font-size: 1.1rem">현재</p>
              <div class="text-h6" style="padding-bottom: 1.5rem">
                <strong>"{{program.name}}" <br /> </strong>
              </div>
              <p style="font-size: 1.1rem">
                {{currentState}}.<br />
                진행자가 공지한 번호를 확인해 주세요.
              </p>
            </q-card-section>
          </q-card>
        </div>
      </div>

      <div class="col">
        <div class="row justify-around" style="padding: 1rem">
          <q-card style="width: 45%">
            <q-card-section>
              <div
                class="text-h6"
                style="text-align: center; padding-bottom: 1rem"
              >
                <strong> 참여 시작 인증 번호 </strong>
              </div>
              <div class="row justify-around" v-if="start_not_validated">
                <div class="col-7">
                  <q-input outlined v-model="ph1" label="시작인증코드" />
                </div>
                <div class="col-3">
                  <q-btn push size="21px" @click="startValidateCode"
                    >제출</q-btn
                  >
                </div>
              </div>
              <div class="row justify-around" v-else>
                <q-img
                  :src="check_url"
                  spinner-color="white"
                  style="height: 6rem; width: 6rem"
                ></q-img>
              </div>
              <p
                style="text-align: center; padding-top: 2rem"
                v-if="start_not_validated"
              >
                프로그램이 시작되면 인증번호를 제출해주세요.
              </p>
              <p style="text-align: center; padding-top: 2rem" v-else>
                {{koreanDate(new Date())}} 참여시작이 인증되었습니다.
              </p>
            </q-card-section>
          </q-card>

          <q-card style="width: 45%">
            <q-card-section>
              <div
                class="text-h6"
                style="text-align: center; padding-bottom: 1rem"
              >
                <strong> 참여 종료 인증 번호 </strong>
              </div>
              <div class="row justify-around" v-if="end_not_validated">
                <div class="col-7">
                  <q-input outlined v-model="ph2" label="종료인증코드" />
                </div>
                <div class="col-3">
                  <q-btn push size="21px" @click="endValidateCode">제출</q-btn>
                </div>
              </div>
              <div class="row justify-around" v-else>
                <q-img
                  :src="check_url"
                  spinner-color="white"
                  style="height: 6rem; width: 6rem"
                ></q-img>
              </div>
              <p
                style="text-align: center; padding-top: 2rem"
                v-if="end_not_validated"
              >
                프로그램이 종료되면 인증번호를 제출해주세요.
              </p>
              <p style="text-align: center; padding-top: 2rem" v-else>
                {{koreanDate(new Date())}} 참여 종료가 인증되었습니다.
              </p>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue';
import {useRoute} from 'vue-router';
import {useProgramStore} from 'stores/program.store';
import {api} from "boot/axios";

export default defineComponent({
  name: 'IndexPage',

  setup() {
    const check_url = ref('/src/assets/greencheck.png');
    const ph1 = ref('');
    const ph2 = ref('');
    const start_not_validated = ref(true);
    const router = useRoute();
    const startValidateCode = () => {
      api.post(`/programs/${router.params.program_id}/attendance/code/verify/`, {'type': 0, 'code': ph1.value}, {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}}).then(
        () => {
          start_not_validated.value = false;
        }).catch(
          () => {
            alert('잘못된 코드입니다.');
          }
      )
    };

    const end_not_validated = ref(true);
    const endValidateCode = () => {
      api.post(`/programs/${router.params.program_id}/attendance/code/verify/`, {'type': 1, 'code': ph2.value}, {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}}).then(
        () => {
          end_not_validated.value = false;
        }).catch(
        () => {
          alert('잘못된 코드입니다.');
        }
      )
    };

    const programStore = useProgramStore();
    const program = ref(programStore.program);
    const route = useRoute();
    const currentState = ref('');
    const zero = num => num < 10 && num >= 0 ? '0' + num : num;
    const koreanDate = date => `${date.getFullYear()}년 ${zero(date.getMonth() + 1)}월 ${zero(date.getDate())}일 ${zero(date.getHours())}:${zero(date.getMinutes())}`;

    programStore.fetchProgram(route.params.program_id.toString());
    programStore.$subscribe(() => {
      program.value = programStore.program;
      const now = new Date();
      if(now.getTime() < programStore.program.program_start_at){
        currentState.value = '프로그램 시작 전입니다';
      } else if(now.getTime() > programStore.program.program_end_at){
        currentState.value = '프로그램 종료 전입니다';
      } else {
        currentState.value = '프로그램 종료 후 입니다';
      }
    });

    return {
      program,
      currentState,
      koreanDate,
      ph1,
      ph2,
      check_url,
      startValidateCode,
      start_not_validated,
      endValidateCode,
      end_not_validated,
    };
  },
});
</script>
