<!-- Vue : 랜더링 문법 -->
<template lang="">
  <div>
    <h1 v-if="bRender">bRender의 값이 true이면 , h1 블록이 화면에 보여진다.</h1>
    <h1 v-if="type === 'A'">A</h1>
    <h1 v-else-if="type === 'B'">B</h1>
    <h1 v-else-if="type === 'C'">C</h1>
    <h1 v-else>위의 v-if값들이 전부 false일때 나오는 default같은 녀석</h1>
    <hr />
    <!-- v-show는 else구문이 없음. -->
    <!-- v-if는 조건을 만족하면 그 순간 블록이 생성 아니면 삭제
		또한 아예 렌더링 자체가 안됨-->
    <h1 v-show="bRender">bRender가 참</h1>
    <!-- 그러나 v-show의 경우 렌더링은 되나 표기만 안됨.(display : none과 같이) -->
  </div>
</template>
<script>
export default {
  data() {
    return {
      bRender: true,
      type: 'A',
    };
  },
};
</script>
<style lang=""></style>
