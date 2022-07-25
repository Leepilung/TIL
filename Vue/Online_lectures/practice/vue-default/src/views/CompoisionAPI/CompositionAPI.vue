<!-- OptionAPI를 CompositionAPI로 1차 개선 -->
<template lang="">
  <div>
    <h1>CompositionAPI</h1>
    <h2>Calculator</h2>
    <input type="number" v-model="state.num1" @keyup="plusNumbers" />
    <span>+</span>
    <input type="number" v-model="state.num2" @keyup="plusNumbers" />
    <span>=</span>
    <span>{{ state.result }}</span>
  </div>
</template>
<script>
// reactive를 이용해 감싸면 num1,num2,result에 대한 실시간 변경사항에 대해 적용할 수 있도록 해줌
import { reactive } from 'vue';
export default {
  setup() {
    let state = reactive({
      num1: 0,
      num2: 0,
      result: 0,
    });

    const plusNumbers = () => {
      state.result = state.num1 + state.num2;
    };

    return {
      state,
      plusNumbers,
    };
  },
};
</script>
<style lang=""></style>
