<template lang="">
  <div>Item Length: {{ this.itemLength }}</div>
  <div>Item : {{ this.items }}</div>
</template>
<script>
export default {
  //   props: {
  //     itemLength: {
  //       type: Number,
  //       default: 0,
  //     },
  //   },
  inject: ['itemLength', 'items'],
};
</script>
<style lang=""></style>
