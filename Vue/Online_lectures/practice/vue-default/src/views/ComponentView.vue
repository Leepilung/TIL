<template lang="">
  <div>
    <h1>부모 컴포넌트 제목 : {{ parentMessage }}</h1>
    <button type="button" @click="callChildFunc">부모에 있는 클릭</button>
    <!-- html에서 id와 동일한 기능을 하는 ref가 있다. -->
    <ChildEvent ref="child_component" />
    <hr />
    <!-- emit 사용시 첫번째 파라미터 아래와 같이 넣어줘야 함 -->
    <MsgComponents @send-message="sendMessage" ref="ChildComponents" />
    <button type="button" @click="showData">부모 버튼</button>
  </div>
</template>
<script>
import ChildEvent from '../components/ChildEvent.vue';
import MsgComponents from '../components/MsgComponents.vue';

export default {
  name: 'comPo',
  components: { ChildEvent, MsgComponents },
  data() {
    return {
      parentMessage: '',
    };
  },
  computed: {
    msg() {
      return this.$refs.ChildComponents.msg;
    },
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
    sendMessage(data) {
      this.parentMessage = data;
    },
    showData() {
      alert(this.msg);
    },
  },
};
</script>
<style lang=""></style>
