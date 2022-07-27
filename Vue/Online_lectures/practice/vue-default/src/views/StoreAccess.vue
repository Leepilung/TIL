<!-- VueX 실습 관련 페이지 -->
<template lang="">
  <div>
    <h1>Cart : {{ cartCount }}</h1>
    <h2>Count : {{ count }}</h2>
    <h2>ProductA : {{ productACount }}</h2>
    <button @click="increment">테스트 버튼</button>
  </div>
</template>
<script>
export default {
  computed: {
    count() {
      return this.$store.state.count;
    },
    cartCount() {
      return this.$store.getters.cartCount;
    },
    productACount() {
      return this.$store.getters.productACount;
    },
  },
  methods: {
    increment() {
      // store안의 함수를 호출하려면 commit() 메소드를 무조건 사용해야 하고 매개변수로 함수명을 넣어야 함
      this.$store.commit('increment');
    },
  },
};
</script>
<style lang=""></style>
