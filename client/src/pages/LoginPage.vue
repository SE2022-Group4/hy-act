<template>
  <q-layout>
    <q-page class="window-height window-width row justify-center items-center">
      <div class="column">
        <div class="row">
          <h6 class="text-h6 q-my-md">한양대 비교과 프로그램 로그인</h6>
        </div>
        <div class="row">
          <q-card bordered class="shadow-1">
            <q-card-section>
              <q-form>
                <q-input v-model="userId" label="아이디" type="text" class="col-12" />
                <q-input v-model="userPw" label="비밀번호" type="password" class="col-12" />
              </q-form>
            </q-card-section>
            <q-card-actions>
              <q-btn
                label="로그인"
                flat
                color="primary"
                class="col-12"
                @click="login" />
            </q-card-actions>
            <q-card-section>
              <p class="text-grey-6">가입하지 않으셨나요? 회원가입을 해주세요</p>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </q-page>
  </q-layout>
</template>

<script>
import {ref} from 'vue';
import {useQuasar} from 'quasar';
import {api} from 'boot/axios';

export default {
  name: 'LoginPage',
  setup(){
    const $q = useQuasar()

    const userId = ref('')
    const userPw = ref('')
    const login = () => {
      if(userId.value.length === 0){
        $q.dialog({
          title: '아이디를 입력해주세요',
          message: '아이디를 입력해주세요',
          ok: '확인'
        })
        return
      }
      if(userPw.value.length === 0) {
        $q.dialog({
          title: '비밀번호를 입력해주세요',
          message: '비밀번호를 입력해주세요',
          ok: '확인'
        })
      }

      api.post('/user/signin/', JSON.stringify({'username': userId.value, 'password': userPw.value}), {
        headers: {'Content-Type': 'application/json'},
        }).then((res) => {
          console.log(res.status)
          localStorage.setItem('token', res.data.token.toString())
          window.location.href = '/'
        }).catch((error) => {
          console.log(error)
          $q.dialog({
            title: '로그인 실패',
            message: '아이디 또는 비밀번호가 잘못되었습니다.',
            ok: '확인'
          })
        })
    }
    return {userId, userPw, login}
  }
}
</script>

<style scoped>

</style>
