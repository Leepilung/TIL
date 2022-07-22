<template lang="">
  <div>
    <button type="button" @click="callChildFunc">부모에 있는 클릭</button>
    <!-- html에서 id와 동일한 기능을 하는 ref가 있다. -->
    <ChildEvent ref="child_component" />
    <hr />
    <MsgComponents ref="ChildComponents" />
  </div>
</template>
<script>
import ChildEvent from '../components/ChildEvent.vue';
import MsgComponents from '../components/MsgComponents.vue';

export default {
  name: 'comPo',
  components: { ChildEvent, MsgComponents },
  data() {
    return {};
  },
  methods: {
    callChildFunc() {
      // 부모 컴포넌트에서 자식 컴포넌트 이벤트 실행
      // this.$refs.child_component.$refs.child_btn.click();
      // 부모 컴포넌트에서 자식 컴포넌트 메소드 실행
      // this.$refs.child_component.childFunc();
      // $refs -> 객체로 접근할 때 사용

      this.$refs.ChildComponents.msg = '부모 컴포넌트에서 바꾼 메세지';
    },
  },
};
</script>
<style lang=""></style>
