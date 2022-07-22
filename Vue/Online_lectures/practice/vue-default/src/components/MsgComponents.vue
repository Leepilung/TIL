<template lang="">
  <div>
    자식 컴포넌트에서의 메시지 : {{ msg }}
    <br />
    <button type="button" @click="sendFromChild">자식 컴포넌트 버튼</button>
    <hr />
    <button type="button" @click="changeData">자식 컴포넌트 데이터 변경</button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      msg: '자식 컴포넌트에 있던 메시지',
    };
  },
  methods: {
    sendFromChild() {
      // $emit => 자식에서 부모로 특정 이벤트를 발생시키는 녀석
      // 첫 번째 파라미터는 부모컴포넌트에 정의되있는 함수명, 2번째는 데이터
      this.$emit('send-message', this.msg);
    },
    changeData() {
      this.msg = '자식 컴포넌트에서 데이터 변경이 일어났습니다.';
    },
  },
};
</script>
<style lang=""></style>
