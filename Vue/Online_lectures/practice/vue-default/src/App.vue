<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/contact">Contact</router-link> |
    <router-link to="/databinding">Databinding</router-link> |
    <router-link to="/example">Example</router-link> |
    <router-link to="/example2">Example2</router-link> |
    <router-link to="/rendering">Rendering</router-link>
    <br />
    <router-link to="/event">event</router-link> |
    <router-link to="/computed">computed</router-link> |
    <router-link to="/watch">watch</router-link> |
    <router-link to="/inquiry">Inquiry</router-link> |
    <router-link to="/save">Save</router-link> |
    <router-link to="/server">Server</router-link> |
    <router-link to="/component">component</router-link> |
    <router-link to="/slot">slot</router-link> |
  </nav>
  <router-view> </router-view>
</template>

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
