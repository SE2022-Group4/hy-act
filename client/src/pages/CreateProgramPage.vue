<template>
  <q-page>
    <div class="column" style="margin: 10px">
      <div class="text-h4 text-weight-bold q-mb-xl" style="text-align: center; margin: 15px">
        신규 비교과 프로그램 등록
      </div>
      <q-form @submit="onSubmit" @reset="onReset" class="col-12">
        <div class="row">
          <q-uploader class="full-width" color="teal" filled accept=".jpg, image/*"/>
        </div>
        <div class="row" style="margin-top: 20px">
          <div class="text-h6 text-weight-bold col-4 q-mt-xs q-pr-xs q-mb-md" style="text-align: center">
            강의명
          </div>
          <div class="col-8">
            <q-input outlined dense v-model="title"  />
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
              v-model="targetGrade"
              :options="grades"
              option-value="id"
              option-label="name"
              label="대상 학년"
              emit-value
              map-option />
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
              v-model="targetGender"
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
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            진행 장소
          </div>
          <div class="col-8">
            <q-input
              dense
              outlined
              v-model="location"
              label="진행 장소"
            />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            신청 인원
          </div>
          <div class="col-8">
            <q-input
              dense
              outlined
              type="number"
              v-model="maxApplicantCount"
              label="신청 인원"
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
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            프로그램 분야
          </div>
          <div class="col-8">
            <q-select dense outlined label="분야" v-model="category" :options="categoryList.map(item => item.name)"/>
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            시작 일시
          </div>
          <div class="col-4">
            <q-input dense v-model="programStartDate" filled type="date" name="시작 날짜" />
          </div>
          <div class="col-4" style="padding-inline-start: 5px">
            <q-input dense v-model="programStartTime" filled type="time" name="시작 시간" />
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            종료 일시
          </div>
          <div class="col-4">
            <q-input dense v-model="programEndDate" filled type="date" name="종료 날짜" />
          </div>
          <div class="col-4" style="padding-inline-start: 5px">
            <q-input dense v-model="programEndTime" filled type="time" name="종료 시간" />
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
        <q-separator color="black" />

        <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md" style="text-align: center; margin-top: 10px">
          강사/주관기관 정보 등록
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            주관 기관
          </div>
          <div class="col-8">
            <q-select dense outlined label="기관" v-model="department" :options="departmentList.map(item => item.name)"/>
          </div>
        </div>
        <div class="row">
          <div class="text-h6 text-weight-bold col-4 vertical-middle q-pr-xs q-mb-md q-mt-sm" style="text-align: center">
            강사 검색
          </div>
          <div class="col-8">
            <q-select
              ref="lecturerSearchBar"
              filled
              v-model="lecturer"
              use-input
              hide-selected
              fill-input
              :options="lectureList.map(item => item.real_name)"
              @filter="filter"
              hide-dropdown-icon
              />
          </div>
        </div>
        <div class="row">
          <q-btn
            style="margin-top: 250px"
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
import {ref} from 'vue';
import {api} from '../boot/axios';
import {useUserStore} from '../stores/user.store';
import {useQuasar} from 'quasar';
import {useProgramCategoryStore} from '../stores/program.category.store';
import {useProgramDepartmentStore} from '../stores/department.store';
import {useLecturerStore} from '../stores/lecturer.store';

export default {
  name: 'CreateProgramPage',
  setup() {
    const $q = useQuasar()
    const userStore = useUserStore();
    userStore.$subscribe(() => {
      console.log(userStore.user);
      if(userStore.user.groups.filter(group => group.name === 'admin').length === 0) {
        $q.dialog({
          title: '오류',
          message: '관리자 권한이 필요합니다.',
          ok: true,
        }).onOk(() => {
          window.location.href = '/';
        });
      }
    });

    const now = new Date();
    const zero = num => num < 10 && num >= 0 ? '0' + num : num;

    const title = ref('');
    const description = ref('');
    const location = ref('');
    const applyStartDate = ref(`${now.getFullYear()}-${zero(now.getMonth() + 1)}-${zero(now.getDate())}`);
    const applyStartTime = ref(`${zero(now.getHours())}:${zero(now.getMinutes())}`);
    const applyEndDate = ref(`${now.getFullYear()}-${zero(now.getMonth() + 1)}-${zero(now.getDate() + 3)}`);
    const applyEndTime = ref('23:59');
    const programStartDate = ref(`${now.getFullYear()}-${zero(now.getMonth() + 2)}-${zero(now.getDate())}`);
    const programStartTime = ref('09:00');
    const programEndDate = ref(`${now.getFullYear()}-${zero(now.getMonth() + 2)}-${zero(now.getDate())}`);
    const programEndTime = ref('13:00');
    const thumbnailURL = ref('');
    const targetGrade = ref('전체');
    const targetGender = ref('전체');
    const category = ref('');
    const department = ref('');
    const maxApplicantCount = ref(0);

    const thumbnailURLList = [
      'http://jjal.today/data/file/gallery/1028612757_dJDo9pBV_2bd774f01a7f254ec0c907978f95f52ea1f05ce4.jpg',
      'https://image.newsis.com/2021/07/26/NISI20210726_0000795204_web.jpg?rnd=20210726113530',
      'https://img.etnews.com/news/article/2019/05/31/cms_temp_article_31142124414587.jpg'
    ];
    thumbnailURL.value = thumbnailURLList[Math.floor(Math.random() * thumbnailURLList.length)]

    const categoryStore = useProgramCategoryStore();
    categoryStore.fetchProgramCategoryList();
    const categoryList = ref([]);
    categoryStore.$subscribe(() => {
      categoryList.value = categoryStore.categoryList;
    });

    const departmentStore = useProgramDepartmentStore();
    departmentStore.fetchDepartmentList();
    const departmentList = ref([]);
    departmentStore.$subscribe(() => {
      departmentList.value = departmentStore.departmentList;
    });
    const genders = ['전체', '남성', '여성']

    const lecturer = ref('');
    const lecturerSearchBar = ref(null)

    const lecturerStore = useLecturerStore()
    const lectureList = ref(lecturerStore.lecturerList)
    lecturerStore.$subscribe(() => {
      lectureList.value = lecturerStore.lecturerList;
    })

    function filter(value, update) {
      if (value.length < 2) {
        lectureList.value = []
      }
      else {
        lecturerStore.fetchLectureList(value)
        update()
      }
    }

    return {
      title, description, location, applyStartDate, applyStartTime, applyEndDate, applyEndTime,
      programStartDate, programStartTime, programEndDate, programEndTime, thumbnailURL, targetGrade, targetGender,
      category, department, maxApplicantCount, categoryList, departmentList, lecturer, lectureList, lecturerSearchBar,
      filter,
      grades: ['전체', '1학년', '2학년', '3학년', '4학년 이상'],
      genders,
      onSubmit() {
        if(title.value.trim().length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '제목을 입력해주세요.',
          })
        } else if (description.value.trim().length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '설명을 입력해주세요.',
          })
        } else if (location.value.trim().length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '장소를 입력해주세요.',
          })
        } else if (category.value.trim().length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '카테고리를 입력해주세요.',
          })
        } else if (department.value.trim().length === 0){
          $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: '주관기관을 입력해주세요.',
          })
        }
        else {
          const data = {
            name: title.value,
            description: description.value,
            location: location.value,
            apply_start_at: new Date(`${applyStartDate.value} ${applyStartTime.value}`).getTime() / 1000,
            apply_end_at: new Date(`${applyEndDate.value} ${applyEndTime.value}`).getTime() / 1000,
            program_start_at: new Date(`${programStartDate.value} ${programStartTime.value}`).getTime() / 1000,
            program_end_at: new Date(`${programEndDate.value} ${programEndTime.value}`).getTime() / 1000,
            thumbnail_url: thumbnailURL.value,
            target_grade: parseInt(targetGrade.value.replace('학년', '').replace('전체', '0')),
            max_applicant_count: maxApplicantCount.value,
            sex: genders.indexOf(targetGender.value),
            department: departmentList.value.filter(item => item.name === department.value)[0].id,
            category: categoryList.value.filter(item => item.name === category.value)[0].id,
            lecturer_id: lectureList.value.filter(item => item.real_name === lecturer.value)[0].id,
          };
          console.log(JSON.stringify(data));
          api.post('/programs/', JSON.stringify(data), {headers: {'Authorization': `Token ${localStorage.getItem('token')}`, 'Content-Type': 'application/json'}}).then(
            () => {
              $q.notify({
                color: 'green-5',
                textColor: 'white',
                icon: 'check',
                message: '새로운 프로그램을 생성했습니다.',
              })
              window.location.href = '/admin'
            }
          )
        }
      },
      onReset() {
        title.value = null;
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
