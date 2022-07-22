<template>
  <h1 class="page-title">{{ title }}</h1>
</template>

<script>
export default {
  // Vue에서 자식 컴포넌트에서 props를 사용하는 방법
  props: {
    title: {
      type: String,
      default: '페이지 타이틀',
    },
  },
};
</script>

<style scoped>
.page-title {
  padding-left: 20px;
  border-left: 5px solid red;
  text-align: left;
}
</style>
