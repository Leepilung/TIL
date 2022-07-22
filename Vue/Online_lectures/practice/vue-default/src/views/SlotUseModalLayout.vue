<template lang="">
  <div>
    <modal-layout>
      <!-- slot은 이름으로 따라가기 때문에 순서는 상관없음. -->
      <!-- 자식 컴포넌트에서 mark up을 재정의해서 사용할 수 있는 녀석 -->
      <template v-slot:footer>
        <button type="button">닫기</button>
      </template>
      <template v-slot:header>
        <h1>팝업 타이틀</h1>
      </template>
      <template v-slot:default>
        <p>팝업 컨텐츠1</p>
        <p>팝업 컨텐츠2</p>
      </template>
    </modal-layout>
  </div>
</template>
<script>
import SlotModalLayout from '../components/SlotModalLayout.vue';
export default {
  components: { 'modal-layout': SlotModalLayout },
};
</script>
<style lang=""></style>
