<template>
  <v-container class="mt-3">
    <h2 class="grey--text mb-3">Meine Fokus</h2>
    <MyFocus class="mb-4"/>

    <div class="clearfix">
      <v-btn class="hidden-sm-and-down float-r" :to="{ name: 'categories'}" exact router>
        <v-icon>add</v-icon>
        Modul auswählen
      </v-btn>

      <h2 class="grey--text mb-3">Meine Module</h2>

      <v-btn class="mb-4 ml-0 mt-0 hidden-md-and-up" @click.stop="showFocusDialog=true">
        <v-icon>add</v-icon>
        Modul auswählen
      </v-btn>
    </div>

    <ModuleProgressListItem v-for="(moduleProgress, index) in userModules"
                            :moduleProgress="moduleProgress"
                            :key="index"
                            class="mb-4"/>

    <h3 class="title-recomendations pt-3">Vorgeschlagene Module</h3>
    <v-container fluid grid-list-md>
      <v-layout row wrap>
        <v-flex v-for="(item, index) in recomendations" :key="index" xs12 sm6 class="mb-1">
          <Recomendation/>
        </v-flex>
      </v-layout>
    </v-container>

  </v-container>
</template>

<script>
  import USER_DEVELOPMENT_QUERY from '@/graphql/gql/userDevelopment.gql'

  import {mapActions} from 'vuex'

  import MyFocus from '@/components/focus/MyFocus.vue'
  import ModuleProgressListItem from '@/components/development/ModuleProgressListItem'
  import Recomendation from '@/components/development/Recomendation'

  export default {
    components: {
      MyFocus,
      ModuleProgressListItem,
      Recomendation
    },

    data() {
      return {
        loading: true,
        userProgress: {
          usermoduleprogressSet: {
            edges: []
          }
        },
        recomendations: [1, 2]
      }
    },

    apollo: {
      userProgress: {
        query: USER_DEVELOPMENT_QUERY,
        fetchPolicy: 'network-only',
        watchLoading(isLoading, countModifier) {
          // debugger
          console.log(`watchLoading(${isLoading}, ${countModifier})`)
        }
      }
    },

    computed: {
      userModules: function () {
        let moduleProgress = this.userProgress.usermoduleprogressSet.edges.map(entry => entry.node.module)
        return moduleProgress.map(function (entry) {
          const parsedCategory = JSON.parse(entry.category)
          return { ...entry, category: { title: parsedCategory.title, slug: parsedCategory.slug } }
        })
      }
    },

    methods: {
      ...mapActions({
        startModuleProgress: 'startModuleProgress'
      })
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  img {
    max-width: 100%;
  }

  h2 {
    font-size: 24px;
    font-weight: 400;
  }

  h3 {
    font-size: 24px;
    margin-bottom: 12px;
  }

  .title-recomendations {
    font-size: 15px;
    font-weight: 400;
    text-transform: uppercase;
  }

  .video-thumbnail {
    max-width: 200px;
  }

  .hero-bg {
    background-color: $blue;
  }

  .description {
    font-size: 18px;
    font-weight: bold;
  }

  .clearfix::after {
    content: "";
    clear: both;
    display: table;
  }

  .float-l {
    float: left;
  }

  .float-r {
    float: right;
    margin-top: -5px;
  }
</style>
