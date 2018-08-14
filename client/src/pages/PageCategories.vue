<template>
  <v-container fluid grid-list-xl>
    <v-layout row wrap>
      <v-flex v-for="category in categories" :key="category.id" xs4 class="text-center">
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
    name: 'page-categories',

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
      document.title = 'Container'
    },

    apollo: {
      categories: {
        query: CATEGORIES_QUERY,
        variables: {
          username: 'test'
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
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  .category-wrapper {
    width: 100%;
  }
</style>
