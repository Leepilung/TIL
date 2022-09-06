<template>
  <div>
    <input :disabled="click" v-model="state" />
    <p>{{ state }}</p>
    <button @click="click = !click">상태값 전환</button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      state: "",
      click: true,
    };
  },
};
</script>

<style lang="scss"></style>
