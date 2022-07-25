<template lang="">
  <div>{{ title }}</div>
</template>
<script>
import { inject } from 'vue';
export default {
  setup() {
    const title = inject('title');

    return { title };
  },
};
</script>
<style lang=""></style>
