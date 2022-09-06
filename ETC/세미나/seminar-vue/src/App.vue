<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <button :disabled="button">
    {{ button ? "버튼 비활성화" : "버튼 활성화" }}
  </button>
  <button @click="button = !button">버튼 상태 전환</button>
  <input :disabled="button" />
  <router-view />
  <StateVue />
</template>

<script>
import StateVue from "./세미나/1_State.vue";
export default {
  components: { StateVue },
  data() {
    return {
      button: false,
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
