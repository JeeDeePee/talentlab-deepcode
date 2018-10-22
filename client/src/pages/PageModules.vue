<template>
  <div class="pb-4">
    <section class="background--violet text-xs-center">
      <v-container class="pb-0">
        <h1 class="py-5">Wähle die passenden Module zur Stärkung deiner Kompetenzen!</h1>
        <div class="text-xs-center">
          <v-btn @click="$vuetify.goTo('#learn-more', {duration: 200, offset: -50})" class="mx-2">
            Module surfen
          </v-btn>
          <v-btn v-if="user" :to="{name: 'development', params: {showFocusDialog: true}}" exact router class="mx-2">
            Kompetenzen erfassen
          </v-btn>
        </div>
        <v-img :src="require(`@/assets/img/moods/communication_2.png`)" class="mt-4 hero--image"></v-img>
      </v-container>

    </section>

    <v-container grid-list-xl class="py-5" id="learn-more">

      <v-layout row wrap>
        <v-flex v-for="category in categories" :key="category.id" xs4 class="text-xs-center">
          <!--<img :src="category.icon"><br>-->
          <component :is="category.iconComponent"/>
          <div>
            <h3 class="my-3">{{category.title}}</h3>
            <p class="paragraph mb-5">{{category.teaser}}</p>
          </div>
        </v-flex>
        <v-flex xs12 sm6 v-for="module in modules" :key="module.id" class="mb-1">
          <ModuleCard :module="module"/>
        </v-flex>
      </v-layout>
    </v-container>
  </div>

</template>

<script>
  import CATEGORIES_QUERY from '@/graphql/gql/categories.gql'

  import {mapGetters} from 'vuex'

  import GrowingAsALeader from '@/assets/img/icons/growing-as-a-leader-grey.svg'
  import MasteringComplexity from '@/assets/img/icons/mastering-complexity-grey.svg'
  import MasteringRelations from '@/assets/img/icons/mastering-relations-grey.svg'

  import ModuleCard from '@/components/reusable/ModuleCard'

  export default {
    components: {
      GrowingAsALeader,
      MasteringComplexity,
      MasteringRelations,
      ModuleCard
    },

    data() {
      return {
        initialQuery: CATEGORIES_QUERY,
        categories: [],
        modules: []
      }
    },

    computed: {
      ...mapGetters({
        user: 'getUser'
      })
    },

    apollo: {
      categories: {
        query: CATEGORIES_QUERY,
        variables: {
          numModules: -1
        },
        fetchPolicy: 'network-only',
        manual: true,
        result({data, loading, networkStatus}) {
          if (!loading) {
            this.categories = data.categories.edges.map(entry => entry.node)
            this.modules = data.userModules.edges.map(entry => ({'status': entry.node.status, ...entry.node.module}))
          }
        }
      }
    },

    created() {
      document.title = 'Modul'
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  .category-wrapper {
    width: 100%;
  }
</style>
