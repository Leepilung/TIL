<template>
  <div v-click-away="onClickAway" @click="onClick">.zcxvz..</div>
</template>

<script>
import { directive } from 'vue3-click-away';
export default {
  directives: {
    ClickAway: directive,
  },
  methods: {
    onClickAway(event) {
      console.log('바깥쪽 클릭', event);
    },
    onClick() {
      console.log('클릭');
    },
  },
};
</script>
