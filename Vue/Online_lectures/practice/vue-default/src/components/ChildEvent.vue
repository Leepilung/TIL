<template lang="">
  <div>
    <button type="button" @click="childFunc" ref="child_btn">
      자식 클릭 이벤트
    </button>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  methods: {
    childFunc() {
      alert('부모 컴포넌트에서 발생한 이벤트??');
    },
  },
};
</script>
<style lang=""></style>
