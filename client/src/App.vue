<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" fixed class="hidden-md-and-up">
      <v-list dense>
        <v-list-tile :to="{ name: 'development'}" exact router>
          <v-list-tile-content>
            <v-list-tile-title>Meine Entwicklung</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile :to="{ name: 'categories'}" exact router>
          <v-list-tile-content>
            <v-list-tile-title>Lernmodule</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <!--
        <v-list-tile :to="{ name: 'dashboard'}" exact router>
          <v-list-tile-content>
            <v-list-tile-title>Dashboard</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        -->
      </v-list>
    </v-navigation-drawer>
    <v-toolbar fixed app dark class="elevation-0">
      <v-toolbar-side-icon @click.stop="drawer = !drawer" class="hidden-md-and-up"></v-toolbar-side-icon>
      <v-toolbar-title>talent<b>lab</b></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat :to="{ name: 'development'}" exact router>Meine Entwicklung</v-btn>
        <v-btn flat :to="{ name: 'categories'}" exact router>Lernmodule</v-btn>
        <!--
        <v-btn flat :to="{ name: 'dashboard'}" exact router>Dashboard</v-btn>
        -->
      </v-toolbar-items>
    </v-toolbar>
    <v-content fluid fill-height>
      <v-slide-x-transition mode="out-in">
        <router-view></router-view>
      </v-slide-x-transition>
    </v-content>
  </v-app>

</template>

<script>
  export default {
    name: 'App',

    data() {
      return {
        active: null,
        drawer: null,
        userid: 1,
        name: 'Max Muster',
        email: 'talenlab@orbit7.ch'
      }
    },

    mounted() {
      this.$intercom.boot({
        user_id: this.userid,
        name: this.name,
        email: this.email
      })
      // this.$intercom.show()
    }
  }
</script>

<style lang="scss">
  @import "styles/main";
</style>
