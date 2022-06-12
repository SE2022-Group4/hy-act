<template>
  <q-card style="width: 700px; max-width: 80vw">
    <q-card-section>
      <div class="text-h5" style="text-align: center">
        <strong>세부 정보</strong>
      </div>
    </q-card-section>
    <q-separator color="gray" size="2px" inset></q-separator>
    <q-card-section style="max-height: 60vh; padding: 0px" class="scroll">
      <div class="row">
        <div class="col-2">
          <p style="font-size: 1em; margin: 0px">
            <strong> 일시 </strong>
          </p>
        </div>
        <div class="col-10" style="font-size: 1em">
          <p style="margin: 0px">{{ startDate }} ~ {{ endDate }}</p>
        </div>
      </div>

      <q-separator color="gray" size="2px" inset></q-separator>

      <div class="row">
        <div class="col-2">
          <p style="font-size: 1em; margin: 0px">
            <strong> 장소 </strong>
          </p>
        </div>
        <div class="col-10" style="font-size: 1em">
          <p style="margin: 0px">{{ program.place }}</p>
        </div>
      </div>

      <q-separator color="gray" size="2px" inset></q-separator>
      <div class="row">
        <div class="col-2">
          <p style="font-size: 1em; margin: 0px">
            <strong> 신청기간 </strong>
          </p>
        </div>
        <div class="col-10" style="font-size: 1em">
          <p style="margin: 0px">2022. 3.30(수) ~ 4.15(금) 16:00</p>
        </div>
      </div>

      <q-separator color="gray" size="2px" inset></q-separator>

      <div class="row">
        <div class="col-2">
          <p style="font-size: 1em; margin: 0px">
            <strong> 신청대상 </strong>
          </p>
        </div>
        <div class="col-10" style="font-size: 1em">
          <p style="margin: 0px">
            {{ program.target_people }}
          </p>
        </div>
      </div>

      <q-separator color="gray" size="2px" inset></q-separator>

      <div class="row">
        <div class="col-2">
          <p style="font-size: 1em; margin: 0px">
            <strong> 내용 </strong>
          </p>
        </div>
        <div class="col-10" style="font-size: 1em">
          <p style="margin: 0px">
            {{ program.content }}
          </p>
        </div>
      </div>
    </q-card-section>
    <q-separator inset></q-separator>
    <q-card-actions align="right">
      <q-btn flat label="닫기" color="primary" v-close-popup></q-btn>
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  name: 'ProgramInfoDialog',
  props: {
    program: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const zero = num => num < 10 && num >= 0 ? '0' + num : num;
    const koreanDate = date => `${date.getFullYear()}년 ${zero(date.getMonth() + 1)}월 ${zero(date.getDate())}일 ${zero(date.getHours())}:${zero(date.getMinutes())}`;
    const startDate = koreanDate(props.program.start_date);
    const endDate = koreanDate(props.program.end_date);
    return {
      startDate,
      endDate,
    };
  },
}
</script>

<style scoped>

</style>
