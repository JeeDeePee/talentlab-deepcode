<template>
  <v-app>
    <div>
      <v-tabs v-model="active" dark slider-color="yellow">
        <v-container grid-list-md>
          <v-tab ripple :to="{ name: 'development'}" exact router>
            Mein Entwicklung
          </v-tab>
          <v-tab ripple :to="{ name: 'categories'}" exact router>
            Lernmodule
          </v-tab>
          <v-tab ripple :to="{ name: 'dashboard'}" exact router>
            Dashboard
          </v-tab>
        </v-container>
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

<style lang="scss">
  @import "styles/var";

  body {
    font-family: $font-family;
  }

  ul {
    margin-left: 16px;
  }
</style>
