<template lang="">
  <div>
    <button type="button" @click="callChildFunc">부모에 있는 클릭</button>
    <!-- html에서 id와 동일한 기능을 하는 ref가 있다. -->
    <ChildEvent ref="child_component" />
  </div>
</template>
<script>
import ChildEvent from '../components/ChildEvent.vue';
export default {
  name: 'comPo',
  components: { ChildEvent },
  data() {
    return {};
  },
  methods: {
    callChildFunc() {
      this.$refs.child_component.$refs.child_btn.click();
    },
  },
};
</script>
<style lang=""></style>
