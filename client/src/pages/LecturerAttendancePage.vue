<template>
  <q-page style="padding: 1rem">
    <div class="text-h6" style="padding-bottom: 1rem">
      출석 인증 / 관리 프로그램
    </div>

    <q-separator color="gray" size="2px" inset></q-separator>

    <div class="column">
      <div class="col" style="padding: 1rem">
        <div class="row justify-around">
          <q-card style="width: 95%">
            <q-card-section>
              <div class="column" style="font-size: 1.2rem">
                <div class="col" style="padding: 0.5rem">
                  <div class="row">
                    <div class="col-2">강의명</div>
                    <div class="col-10">
                      {{program.name}}
                    </div>
                  </div>
                </div>
                <div class="col" style="padding: 0.5rem">
                  <div class="row">
                    <div class="col-2">강사</div>
                    <div class="col-10">{{ lecturerName }}</div>
                  </div>
                </div>
                <div class="col" style="padding: 0.5rem">
                  <div class="row">
                    <div class="col-2">시간</div>
                    <div class="col-10">
                      {{ targetDate }}
                    </div>
                  </div>
                </div>
              </div>
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
                <strong> 시작 인증 번호 발급 </strong>
              </div>

              <div class="row justify-center">
                <q-btn
                  v-if="start_not_exist"
                  push
                  color="grey-8"
                  text-color="white"
                  size="1.4rem"
                  @click="clickStartButton"
                  >발급하기
                </q-btn>
                <div
                  class="col"
                  style="text-align: center; font-size: 2.5rem"
                  v-else
                >
                  <strong>{{startAttendanceCode}}</strong>
                </div>
              </div>

              <p
                style="text-align: center; padding-top: 2rem"
                v-if="start_not_exist"
              >
                발급하면 자동으로 시작시간이 기록됩니다.
              </p>
              <p style="text-align: center; padding-top: 2rem" v-else>
                {{ koreanDate(new Date()) }} 시작 시간이 기록되었습니다.
              </p>
            </q-card-section>
          </q-card>

          <q-card style="width: 45%">
            <q-card-section>
              <div
                class="text-h6"
                style="text-align: center; padding-bottom: 1rem"
              >
                <strong> 종료 인증 번호 발급 </strong>
              </div>
              <div class="row justify-center">
                <q-btn
                  v-if="end_not_exist"
                  push
                  color="grey-8"
                  text-color="white"
                  size="1.4rem"
                  @click="clickEndButton"
                  >발급하기
                </q-btn>
                <div
                  class="col"
                  style="text-align: center; font-size: 2.5rem"
                  v-else
                >
                  <strong>{{ endAttendanceCode }}</strong>
                </div>
              </div>
              <p
                style="text-align: center; padding-top: 2rem"
                v-if="end_not_exist"
              >
                발급하면 자동으로 종료시간이 기록됩니다.
              </p>
              <p style="text-align: center; padding-top: 2rem" v-else>
                {{ koreanDate(new Date()) }} 종료 시간이 기록되었습니다.
              </p>
            </q-card-section>
          </q-card>
        </div>
      </div>
      <div class="col">
        <div class="row justify-end" style="padding: 2rem">
          <q-btn
            push
            color="white"
            text-color="grey-8"
            size="1rem"
            @click="refreshButton"
          >
            현황판 새로고침
          </q-btn>
        </div>
      </div>
      <div class="col">
        <div class="row justify-around" style="padding: 1rem">
          <q-table
            style="height: 700px; width: 95%"
            title="참여자 출석 현황"
            :rows="attendanceState"
            :columns="columns"
            row-key="index"
            virtual-scroll
            v-model:pagination="pagination"
            :rows-per-page-options="[0]"
          >
            <template v-slot:body="props">
              <q-tr :props="props">
                <q-td v-for="col in props.cols" :key="col.name" :props="props">
                  <span v-if="col.name !== 'start' && col.name !== 'end'">
                    {{ col.value }}</span
                  >
                  <q-avatar v-if="col.name === 'start'" size="20px">
                    <img v-if="col.value === true" src="/src/assets/greencheck.png"/>
                    <img v-if="col.value === false" src="/src/assets/red_x.png"/>
                  </q-avatar>
                  <q-avatar v-if="col.name === 'end'" size="20px">
                    <img v-if="col.value === true" src="/src/assets/greencheck.png"/>
                    <img v-if="col.value === false" src="/src/assets/red_x.png"/>
                  </q-avatar>
                </q-td>
              </q-tr>
            </template>
          </q-table>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue';
import {useUserStore} from '../stores/user.store';
import {useQuasar} from 'quasar';
import {useProgramStore} from '../stores/program.store';
import {useRoute} from 'vue-router';
import {api} from '../boot/axios';
import {useAttendanceStore} from '../stores/attendance.store';

export default defineComponent({
  name: 'IndexPage',

  setup() {
    const $q = useQuasar();
    const userStore = useUserStore();
    userStore.$subscribe(() => {
      if(userStore.user.groups.filter(group => group.name === 'lecturer').length === 0) {
        $q.dialog({
          title: '오류',
          message: '관리자 권한이 필요합니다.',
          ok: true,
        }).onOk(() => {
          window.location.href = '/';
        });
      }
    });

    const programStore = useProgramStore();
    const program = ref(programStore.program);
    const lecturerName = ref('')
    const route = useRoute();
    const zero = num => num < 10 && num >= 0 ? '0' + num : num;
    const koreanDate = date => `${date.getFullYear()}년 ${zero(date.getMonth() + 1)}월 ${zero(date.getDate())}일 ${zero(date.getHours())}:${zero(date.getMinutes())}`;
    const targetDate = ref('')

    programStore.fetchProgram(route.params.program_id.toString());
    programStore.$subscribe(() => {
      program.value = programStore.program;
      lecturerName.value = programStore.program.lecturer.real_name;
      targetDate.value = `${koreanDate(new Date(programStore.program.program_start_at * 1000))} ~ ${koreanDate(new Date(programStore.program.program_end_at * 1000))}`
    });

    const attendanceStore = useAttendanceStore();
    const attendanceState = ref(attendanceStore.attendance.applications);
    attendanceStore.fetchAttendance(route.params.program_id.toString());
    attendanceStore.$subscribe(() => {
      attendanceState.value = attendanceStore.attendance.applications;
    });

    const columns = [
      {
        name: 'name',
        required: true,
        label: '이름',
        align: 'center',
        field: row => row.student.username,
      },
      {
        name: 'major',
        required: true,
        label: '전공',
        align: 'center',
        field: row => row.student.majors[0].name,
      },
      {
        name: 'start',
        required: true,
        label: '출석 시작',
        align: 'center',
        field: row => row.attendance_start_at !== null,
      },
      {
        name: 'end',
        required: true,
        label: '출석 종료',
        align: 'center',
        field: row => row.attendance_end_at !== null,
      },
    ]


    let start_not_exist = ref(true);
    const startAttendanceCode = ref(0);
    function clickStartButton() {
      if (start_not_exist.value) {
        api.post(`/programs/${route.params.program_id}/attendance/code/create/`, {'type': 0}, {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}}).then(res => {
          startAttendanceCode.value = res.data.code;
          start_not_exist.value = false;
        });
      }
    }

    let end_not_exist = ref(true);
    const endAttendanceCode = ref(0);
    const clickEndButton = () => {
      if (end_not_exist.value) {
        api.post(`/programs/${route.params.program_id}/attendance/code/create/`, {'type': 1}, {headers: {'Authorization': `Token ${localStorage.getItem('token')}`}}).then(res => {
          endAttendanceCode.value = res.data.code;
          end_not_exist.value = false;
        });
      }
    };

    let refresh = ref(true);
    const refreshButton = () => {
      attendanceStore.fetchAttendance(route.params.program_id.toString());
    };

    return {
      program,
      koreanDate,
      targetDate,
      attendanceState,
      columns,
      pagination: ref({
        rowsPerPage: 0,
      }),
      clickStartButton,
      startAttendanceCode,
      start_not_exist,
      endAttendanceCode,
      clickEndButton,
      end_not_exist,
      refreshButton,
      refresh,
      lecturerName,
    };
  },
});
</script>
