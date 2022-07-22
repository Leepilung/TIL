<template lang="">
  <div><ProvideInjectChild /></div>
</template>
<script>
import ProvideInjectChild from '@/components/ProvideInjectChild.vue';
export default {
  components: { ProvideInjectChild },
  data() {
    return {
      items: ['A', 'B'],
    };
  },
  // Provide로 전송하면됨.
  provide() {
    return {
      itemLength: this.items.length,
      items: this.items,
    };
  },
};
</script>
<style lang=""></style>
