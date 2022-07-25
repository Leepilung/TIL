<!-- CompositionAPI3.vue를 추가 개선한 파일 -->
<template lang="">
  <div>
    <h1>CompositionAPI4</h1>
    <h2>Calculator</h2>
    <input type="number" v-model="num1" />
    <span>+</span>
    <input type="number" v-model="num2" />
    <span>=</span>
    <span>{{ result }}</span>
  </div>
</template>
<script>
import { plusCalculator } from './common.js';

export default {
  setup() {
    let { num1, num2, result } = plusCalculator();

    return {
      num1,
      num2,
      result,
    };
  },
};
</script>
<style lang=""></style>
