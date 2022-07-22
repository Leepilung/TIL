<template lang="">
  <div>
    <input type="text" v-model="lastName" />
    <input type="text" v-model="firstName" />
    <h1>Hello, {{ fullName }}</h1>
    <h1>Hello, {{ fullName }}</h1>
    <h1>Hello, {{ fullName }}</h1>
    <h1>Hello, {{ fullName }}</h1>
    <h1>Hello, {{ fullName }}</h1>
    <h1>Hello, {{ fullName }}</h1>
  </div>
</template>
<script>
export default {
  data() {
    return {
      firstName: '재석',
      lastName: '유',
    };
  },
  // computed의 경우 연산 자체를 단 한번만 한다.
  // 또한 computed는 안에 사용된 데이터 필드의 변경사항을 항상 감시하고 반영한다.
  computed: {
    fullName() {
      return this.lastName + this.firstName;
    },
  },
  // 그러나 getFullname()으로 매번 호출하면 매번 연산을 반복
  methods: {
    getFullName() {
      return this.lastName + this.firstName;
    },
  },
};
</script>
<style lang=""></style>
