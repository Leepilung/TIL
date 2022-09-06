<template lang="">
  <div v-click-out-side="customMethod" @click="clickInside" class="box">
    BOX
  </div>
  <br />
  <p>Outside of the box</p>
</template>
<script>
import clickOutSide from '@mahdikhashan/vue3-click-outside';

export default {
  directives: {
    clickOutSide,
  },
  methods: {
    customMethod() {
      alert('You clicked outside the box!');
    },
    clickInside() {
      alert('You clicked inside the box!');
    },
  },
};
</script>
<style lang=""></style>
