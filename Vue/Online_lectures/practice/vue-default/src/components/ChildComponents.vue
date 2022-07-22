<template lang="">
  <div>likes : {{ likes }}</div>
  <div>isOk : {{ isOk }}</div>
  <div>isArray : {{ isArray }}</div>
  <div>isObject : {{ isObject }}</div>
  <div>isObject.Author : {{ isObject.Author }}</div>
  <div>isObject.title : {{ isObject.title }}</div>
</template>
<script>
export default {
  props: {
    likes: {
      type: Number,
      default: 0,
    },
    isOk: {
      type: Boolean,
      default: false,
    },
    isArray: {
      type: Array,
    },
    isObject: {
      type: Object,
    },
  },
};
</script>
<style lang=""></style>
