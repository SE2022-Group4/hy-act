<template>
  <div class="q-mb-xs col-11">
    <q-select
      dense
      outlined
      v-model="model"
      :options="options"
      option-value="id"
      option-label="desc"
      name="모집 대상"
      emit-value
      map-options
    />
  </div>
</template>

<script>
import { useQuasar } from 'quasar';
import { ref } from 'vue';
export default {
  data() {
    return {
      model: null,
      options: [
        {
          id: 'goog',
          desc: 'Google',
        },
        {
          id: 'fb',
          desc: 'Facebook',
        },
        {
          id: 'twt',
          desc: 'Twitter',
        },
        {
          id: 'app',
          desc: 'Apple',
        },
        {
          id: 'ora',
          desc: 'Oracle',
          inactive: true,
        },
      ],
    };
  },
};
</script>
