<!-- CompositionAPI2.vue를 추가 개선한 파일 -->
<template lang="">
  <div>
    <h1>CompositionAPI3</h1>
    <h2>Calculator</h2>
    <input type="number" v-model="num1" />
    <span>+</span>
    <input type="number" v-model="num2" />
    <span>=</span>
    <span>{{ result }}</span>
  </div>
</template>
<script>
// reactive를 이용해 감싸면 num1,numㅠ2,result에 대한 실시간 변경사항에 대해 적용할 수 있도록 해줌
import { computed, reactive, toRefs } from 'vue';

const plusCalculator = () => {
  let state = reactive({
    num1: 0,
    num2: 0,
    result: computed(() => state.num1 + state.num2),
  });

  return toRefs(state);
};

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
