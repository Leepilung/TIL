<!-- 옵션 API 스타일 형식 -->
<script>
export default {
  data() {
    return {
      count: 0,
    }
  },

  // methods는 속성 값을 변경하고 업데이트 할 수 있는 함수.
  // 템플릿 내에서 이벤트 리스너로 바인딩 될 수 있음.
  methods: {
    increment() {
      this.count++
    },
  },

  // 생명주기 훅(Lifecycle hooks)은 컴포넌트 생명주기의 여러 단계에서 호출됩니다.
  // 이 함수는 컴포넌트가 마운트 된 후 호출됩니다.
  mounted() {
    console.log(`숫자 세기의 초기값은 ${this.count} 입니다.`)
  },
}
</script>

<template>
  <button @click="increment">숫자 세기: {{ count }}</button>
</template>
