<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" fixed class="hidden-md-and-up">
      <v-list dense>
        <v-list-tile :to="{ name: 'development'}" exact router>
          <v-list-tile-content v-if="user">
            <v-list-tile-title>Meine Entwicklung</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile :to="{ name: 'categories'}" exact router>
          <v-list-tile-content>
            <v-list-tile-title>Module</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile v-if="user" :to="{ name: 'logout'}" exact router>
          <v-list-tile-content>
            <v-list-tile-title>Logout</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile v-else :to="{ name: 'login'}" exact router>
          <v-list-tile-content>
            <v-list-tile-title>Login</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <!--    EXPERIMENTS
        <v-list-tile :to="{ name: 'experiments'}" exact router>
          <v-list-tile-content>
            <v-list-tile-title>Experiments</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>   -->
        <!--    EXPERIMENTS    -->
      </v-list>
    </v-navigation-drawer>
    <v-toolbar fixed app dark class="elevation-0">
      <v-toolbar-side-icon @click.stop="drawer = !drawer" class="hidden-md-and-up"></v-toolbar-side-icon>
      <v-toolbar-title>
        <router-link :to="{ name: 'start'}" class="router">
          talent<b>lab</b>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn v-if="user" flat :to="{ name: 'development'}" exact router>Meine Entwicklung</v-btn>
        <v-btn flat :to="{ name: 'categories'}" exact router>Module</v-btn>

        <v-menu offset-y v-if="user">
          <v-btn flat slot="activator" class="text--primary-accent">
            <v-icon class="mr-1">person_outline</v-icon>
            {{user.fullName}}
          </v-btn>
          <v-list>
            <v-list-tile>
              <v-list-tile-title>
                <router-link :to="{ name: 'logout'}" class="router">
                  Abmelden
                </router-link>
              </v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-menu>
        <v-btn v-else flat :to="{ name: 'login'}" exact router class="text--primary-accent">
          <v-icon class="mr-1">person_outline</v-icon>
          Login
        </v-btn>
        <!--    EXPERIMENTS
        <v-btn flat :to="{ name: 'experiments'}" exact router>Experiments</v-btn>    -->
        <!--    EXPERIMENTS    -->
      </v-toolbar-items>
    </v-toolbar>
    <v-content fluid fill-height>
      <v-slide-x-transition mode="out-in">
        <router-view></router-view>
      </v-slide-x-transition>
    </v-content>

    <footer class="background--secondary footer" v-if="$route.meta.showFooter">
      <v-container>
        <v-layout row wrap>
          <v-flex xs12 sm4>
            <div class="py-3">Kontakt</div>
            <div>
              talentlab<br>
              c/o cedac AG<br>
              Effingerstrasse 4, 3001 Bern<br>
              T +41 (0)31 387 10 10<br>
              info@talentlab.ch<br>
            </div>
          </v-flex>
          <v-flex xs12 sm4 class="text-sm-center">
            <div class="py-3">Partner</div>
            <div>
              cb point gmbh<br>
              orbit7 GmbH<br>
            </div>
          </v-flex>
          <v-flex xs12 sm4 class="text-sm-right">
            <div class="py-3">Folge uns auf</div>
            <div class="font-weight-black headline">
              <a href="https://www.linkedin.com/">in</a>
            </div>
          </v-flex>
        </v-layout>
      </v-container>
    </footer>

    <v-fab-transition v-if="!$route.meta.hideChatButton">
      <v-btn
        color="primary"
        dark
        fab
        fixed
        bottom
        right
        @click.stop="showChat=true"
      >
        <v-icon>chat</v-icon>
      </v-btn>
    </v-fab-transition>

    <DummyChat :visible="showChat" @close="showChat=false"/>

  </v-app>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'
  import DummyChat from '@/components/DummyChat'

  export default {
    name: 'App',

    components: {
      DummyChat
    },

    methods: {
      ...mapActions({
        fetchUser: 'fetchUser'
      })
    },

    data() {
      // TODO: ist das hier der eingeloggter user oder der app user?
      return {
        active: null,
        drawer: null,
        showChat: false
      }
    },

    computed: {
      ...mapGetters({
        user: 'getUser'
      })
    },

    created() {
      this.fetchUser()

      this.$on('showChat', () => {
        console.info('---')
        this.showChat = true
      })
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
  /*@import "styles/main";*/
</style>
