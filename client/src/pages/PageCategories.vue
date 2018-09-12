<template>
  <v-container fluid grid-list-xl>
    <v-layout row wrap>
      <div>Wähle die passenden Module!</div>
      <img src="/static/modul_way-career.jpg" width="100%" height="auto">
      <v-btn class="button item2">
        Modul buchen
      </v-btn>
      <v-btn class="button item2 btn-border">
        Modul buchen
      </v-btn>

    </v-layout>
    <v-layout row wrap>
      <v-flex v-for="category in categories" :key="category.id" xs4 class="text-xs-center">
        <img :src="category.icon"><br>
        {{category.title}}
      </v-flex>
      <v-flex xs12 sm6 v-for="module in modules" :key="module.id" class="mb-1">
        <ModuleTeaser :module="module"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import CATEGORIES_QUERY from '@/graphql/gql/categories.gql'
  import ModuleTeaser from '@/components/categories/ModuleTeaser'

  export default {
    components: {
      ModuleTeaser
    },

    data() {
      return {
        initialQuery: CATEGORIES_QUERY,
        categories: [],
        modules: []
      }
    },

    created() {
      document.title = 'Modul'
    },

    apollo: {
      categories: {
        query: CATEGORIES_QUERY,
        fetchPolicy: 'network-only',
        manual: true,
        result({data, loading, networkStatus}) {
          console.log(`loading(${loading}, ${networkStatus})`)
          // debugger
          if (!loading) {
            this.categories = data.categories.edges.map(entry => entry.node)
            this.modules = data.userModules.edges.map(entry => ({'status': entry.node.status, ...entry.node.module}))
          }
        },
        watchLoading(isLoading, countModifier) {
          // debugger
          console.log(`watchLoading(${isLoading}, ${countModifier})`)
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  .category-wrapper {
    width: 100%;
  }
</style>
