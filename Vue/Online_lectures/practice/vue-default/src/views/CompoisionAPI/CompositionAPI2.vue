<!-- CompositionAPI.vue를 추가 개선한 파일 -->
<template lang="">
  <div>
    <h1>CompositionAPI2</h1>
    <h2>Calculator</h2>
    <input type="number" v-model="state.num1" />
    <span>+</span>
    <input type="number" v-model="state.num2" />
    <span>=</span>
    <span>{{ state.result }}</span>
  </div>
</template>
<script>
// reactive를 이용해 감싸면 num1,numㅠ2,result에 대한 실시간 변경사항에 대해 적용할 수 있도록 해줌
import { computed, reactive } from 'vue';
export default {
  setup() {
    let state = reactive({
      num1: 0,
      num2: 0,
      result: computed(() => state.num1 + state.num2),
    });

    return {
      state,
    };
  },
};
</script>
<style lang=""></style>
