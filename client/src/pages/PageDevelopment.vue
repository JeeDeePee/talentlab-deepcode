<template>
  <v-container class="mt-3">
    <h2 class="grey--text mb-3">Meine Ziele</h2>
    <Goal class="mb-4"/>

    <div class="clearfix">
      <v-btn class="hidden-sm-and-down float-r" @click="startModuleProgress('theFooBar123')">
        <v-icon>add</v-icon>
        Lernmodule auswählen
      </v-btn>

      <h2 class="grey--text mb-3">Meine Lernmodule</h2>

      <v-btn class="mb-4 ml-0 mt-0 hidden-md-and-up">
        <v-icon>add</v-icon>
        Lernmodule auswählen
      </v-btn>
    </div>

    <ModuleProgressListItem v-for="(moduleProgress, index) in userModules"
                            :moduleProgress="moduleProgress"
                            :key="index"
                            class="mb-4"/>

    <h3 class="title-recomendations pt-3">Vorgeschlagene Lernmodule</h3>
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
  import { mapGetters, mapState, mapActions } from 'vuex'

  import Goal from '@/components/development/Goal'
  import ModuleProgressListItem from '@/components/development/ModuleProgressListItem'
  import Recomendation from '@/components/development/Recomendation'

  import USER_PROGRESS_QUERY from '@/graphql/gql/userProgress.gql'

  // import MODULE_PROGRESS_QUERY from '@/graphql/gql/moduleProgress.gql'
  // import START_MODULE_PROGRESS_QUERY from '@/graphql/gql/startModuleProgress.gql'

  export default {
    name: 'page-development',

    components: {
      Goal,
      ModuleProgressListItem,
      Recomendation
    },

    data() {
      return {
        loading: true,
        userProgress: {
          usermoduleSet: {
            edges: []
          }
        },
        recomendations: [1, 2]
      }
    },

    apollo: {
      userProgress: {
        query: USER_PROGRESS_QUERY,
        variables: {
          id: 'VXNlck5vZGU6MQ=='
        }
      }

      // categories: {
      //   query: CREATE_USER_MODULE_QUERY,
      //   manual: true
      //   // result(data, loading, networkStatus) {
      //   //   if (!loading) {
      //   //     this.categories = data.data.categories.edges
      //   //     this.modules = data.data.modules.edges
      //   //   }
      //   // }
      // }
    },

    computed: {
      userModules: function () {
        let moduleProgress = this.userProgress.usermoduleSet.edges.map(entry => entry.node.module)
        return moduleProgress.map(function(entry) {
          const parsedCategory = JSON.parse(entry.category)
          return {...entry, category: {title: parsedCategory.title, slug: parsedCategory.slug}}
        })
      },

      ...mapGetters({
        // productIsInStock: 'productIsInStock'
      }),

      ...mapState({
        // allProducts: state => state.products,
        // firstProduct: state => state.products[0]
      })
    },

    methods: {
      // startModuleProgress(progress) {
      //   debugger
      // }

      ...mapActions({
        startModuleProgress: 'startModuleProgress'
      })
    }
    // created() {
    //   this.loading = true
    //   this.$store.dispatch('fetchUserProgress').then(() => { this.loading = false })
    // }
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
