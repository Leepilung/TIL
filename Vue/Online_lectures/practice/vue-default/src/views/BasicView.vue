<template lang="">
  <div>
    <h1>
      {{ title }}
    </h1>
    <input type="text" v-model="title" />
  </div>
</template>
<script>
export default {
  components_name: '',
  components: {},
  data() {
    // 데이터 () 안에 바인딩되는 태그들은
    return {
      title: 'Hello world2',
    };
  },
  setup() {},
  created() {}, // 뷰 컴포넌트가 생성되는 순간 실행
  mounted() {}, // DOM이 실제 로딩이 되는순간 실행
  unmounted() {}, // 특정 컴포넌트에서 다른 컴포넌트로 이동되는 순간
  methods: {}, //
};
</script>
<style lang="" scoped></style>
