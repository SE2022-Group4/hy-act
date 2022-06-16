<template>bind
  <q-layout view="lHr LpR lFr">
    <q-drawer show-if-above bordered side="left">
      <!-- 네비게이션 링크 -->
      <q-list>
        <q-item-label header>한양대학교 비교과 플랫폼</q-item-label>
        <q-item v-if="group === '학생'" to="/">비교과 프로그램 신청</q-item>
        <q-item v-if="group === '학생'" to="/program/my">비교과 프로그램 출석 확인</q-item>
<!--        <q-item v-if="group === '학생'">수강 이력 및 인증서 발급</q-item>-->
        <q-item v-if="group === '학생'">마일리지 확인 및 사용</q-item>
        <q-item v-if="group === '상점 관리자'">마일리지 사용 처리</q-item>
        <q-item v-if="group === '관리자'" to="/program/create">비교과 프로그램 생성/수정</q-item>
        <q-item v-if="group === '선생님'" to="/lecturer">비교과 프로그램 출석 관리</q-item>
      </q-list>

      <div class="fixed-bottom">
        <q-list>
          <q-item-label header>지원</q-item-label>
          <q-item>유지보수팀(031-400-1111)</q-item>
          <q-item>학사팀(031-400-2222)</q-item>
          <q-item>전산실(031-400-3333)</q-item>
        </q-list>
        <div id="language-dialog" style="background-color: #23272B">
          <q-slide-transition>
            <q-list
              v-show="languageListOpened" style="margin-top: 20px">
              <q-item-label header>언어</q-item-label>
              <q-item>한국어</q-item>
              <q-item>English</q-item>
              <q-item>汉语</q-item>
            </q-list>
          </q-slide-transition>
          <q-btn
            flat
            label="언어 설정"
            :icon-right="languageListOpened ? 'mdi-menu-down' : 'mdi-menu-up'"
            style="width: 100%; color: #91979b"
            @click="openLanguageList" />
        </div>
      </div>
    </q-drawer>

    <q-drawer show-if-above bordered side="right" style="padding-top: 20px">
      <q-list dense style="margin-bottom: 20%">
        <q-item class="items-center">
          <q-avatar size="56px" icon="mdi-account" style="background-color: #E2E6EA"/>
        </q-item>
        <q-item class="text-weight-bold items-center" style="color: #91979b" >{{user.real_name}} {{group}}</q-item>
        <q-item class="items-center">{{user.email}}</q-item>
      </q-list>


      <q-list v-if="group==='학생'">
        <q-item class="items-center" to="/program/my">
          <div class="col-8">예약한 프로그램</div>
          <div class="col-4" style="text-align: end">{{myPrograms}} 건</div>
        </q-item>
        <q-item class="items-center">
          <div class="col-8">마일리지</div>
          <div class="col-4" style="text-align: end">0 포인트</div>
        </q-item>
        <q-item href="https://portal.hanyang.ac.kr">
          <div class="col-11" style="display: flex; align-items: center">한양대학교 포털</div>
          <q-icon class="col-1" size="20px" name="mdi-open-in-new"></q-icon>
        </q-item>
      </q-list>

      <q-list style="background-color: #b0b6ba" separator v-if="group==='student'">
        <q-item-label header style="color: black; text-align: center">인기 비교과 프로그램</q-item-label>
        <q-item style="color: black">하루 1시간 꿀잠 자기</q-item>
        <q-item style="color: black">팀프로젝트에 유용한 GitHub 사용법</q-item>
        <q-item style="color: black">학술정보관 출입 방법</q-item>
        <q-item><q-btn flat label="더보기" style="color: black; width: 100%"/></q-item>
      </q-list>

      <div class="fixed-bottom items-center">
        <q-btn
          icon="mdi-cog"
          label="설정"
          flat
          style="width: 100%; color: #91979b" />
        <q-btn
          icon="mdi-logout"
          label="로그아웃"
          flat
          style="width: 100%; color: #91979b"
          @click="logout" />
        />
      </div>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<style scoped>
  .q-item__label--header {
    color: #9994a3;
  }
  .q-item {
    color: #91979b;
    display: flex;
    align-items: center;
  }

  #language-dialog {
    border-top: solid #5B5D60;
  }

  div .items-center {
    display: flex;
    justify-content: center;
  }
</style>
<script lang="ts">
import {defineComponent, ref} from 'vue';
import {useUserStore} from 'stores/user.store';
import {useMyProgramListStore} from 'stores/my.program.list.store';

export default defineComponent({
  name: 'MainLayout',
  setup: function () {
    const languageListOpened = ref(false)

    const userStore = useUserStore()
    userStore.fetchUser()
    const group = ref('')
    const user = ref(userStore.user)
    const myPrograms = ref(0)
    const myProgramStore = useMyProgramListStore()
    userStore.$subscribe(() => {
      user.value = userStore.user
      if (user.value.groups.filter(group => group.name === 'student').length > 0) {
        myProgramStore.fetchMyProgramListLecturer()
        group.value = '학생'
      } else if (user.value.groups.filter(group => group.name === 'lecturer').length > 0) {
        myProgramStore.fetchMyProgramListLecturer()
        group.value = '선생님'
      } else if (user.value.groups.filter(group => group.name === 'admin').length > 0) {
        myProgramStore.fetchMyProgramListAdmin()
        group.value = '관리자'
      } else {
        group.value = '상점 관리자'
      }
    })

    myProgramStore.$subscribe(() => {
      myPrograms.value = myProgramStore.programList.length
    })

    function logout() {
      userStore.logout()
    }

    function openPortal(){
      window.location.href = 'www.hanyang.ac.kr'
    }

    return {
      user,
      group,
      logout,
      languageListOpened,
      myPrograms,
      openPortal,
      openLanguageList() {
        languageListOpened.value = !languageListOpened.value
      }
    }
  }
});
</script>
