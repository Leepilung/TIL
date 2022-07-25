<!-- 통상적으로 사용한 optionAPI -->
<template lang="">
  <div>
    <h1>CalculatorView</h1>
    <h2>Calculator</h2>
    <input type="number" v-model="num1" @keyup="plusNumbers" />
    <span>+</span>
    <input type="number" v-model="num2" @keyup="plusNumbers" />
    <span>=</span>
    <span>{{ result }}</span>
  </div>
</template>
<script>
export default {
  data() {
    return {
      num1: 0,
      num2: 0,
      result: 0,
    };
  },
  methods: {
    plusNumbers() {
      this.result = this.num1 + this.num2;
    },
  },
};
</script>
<style lang=""></style>
