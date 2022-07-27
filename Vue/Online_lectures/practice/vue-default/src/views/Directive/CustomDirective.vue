<!-- Directive란 v-if, v-for등과 같은 녀석들을 말한다 -->
<template lang="">
  <div><input type="text" v-focus /></div>
</template>
<script>
export default {
  // 커스텀 디렉티브를 만들기 위한 구문
  directives: {
    focus: {
      mounted(el) {
        el.focus();
      },
    },
  },
};
</script>
<style lang=""></style>
