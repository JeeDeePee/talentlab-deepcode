<template>
  <v-app>
    <div>
      <v-tabs
        v-model="active"
        color="cyan"
        dark
        slider-color="yellow"
      >
        <v-tab ripple :to="{ name: 'container'}" exact router>
          Containers
        </v-tab>
        <v-tab ripple :to="{ name: 'about'}" exact router>
          About
        </v-tab>
      </v-tabs>
      <v-content class="pa-3">
        <v-slide-x-transition mode="out-in">
          <router-view></router-view>
        </v-slide-x-transition>
      </v-content>
    </div>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        active: null
      }
    }
  }
</script>

<style>
  #app {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
</style>
