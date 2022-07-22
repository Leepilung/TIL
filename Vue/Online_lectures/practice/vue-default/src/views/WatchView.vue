<template lang="">
  <div>
    <!-- input type을 바꿔도되고 v-model에 .number 추가해도 됨 -->
    <input type="number" v-model="x1" />
    <input type="text" v-model.number="x2" />
    <button type="button" @click="plusNumber">계산</button>
    <input type="text" v-model="y" />
  </div>
</template>
<script>
export default {
  data() {
    return {
      x1: 0,
      x2: 0,
      // y: 0, computed 사용할 시에는 함수명과 중복 안됨.
    };
  },
  // watch는 입력한 데이터 값의 변수를 계속해서 참조하기 떄문에 코스트가 꽤 큰 기능이라
  // 꼭 필요한 부분에서만 사용해야 한다.
  // watch: {
  // 	x1() {
  // 		this.y = this.x1 + this.x2;
  // 	},
  // 	x2() {
  // 		this.y = this.x1 + this.x2;
  // 	},
  // },
  computed: {
    y() {
      return this.x1 + this.x2;
    },
  },
  methods: {
    plusNumber() {
      this.y = this.x1 + this.x2;
    },
  },
};
</script>
<style lang=""></style>
