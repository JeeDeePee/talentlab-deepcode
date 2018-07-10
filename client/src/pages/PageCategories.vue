<template>
  <v-container fluid grid-list-xl>
    <v-layout row wrap>
      <v-flex v-for="category in categories" :key="category.id" xs4 class="text-center">
        <img :src="category.node.icon"><br>
        {{category.node.title}}
      </v-flex>
      <v-flex xs12 sm6 v-for="module in modules" :key="module.node.id" class="mb-1">
        <ModuleTeaser :module="module.node"/>
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
      document.title = 'Lernmodule'
    },

    apollo: {
      categories: {
        query: CATEGORIES_QUERY,
        manual: true,
        result(data, loading, networkStatus) {
          if (!loading) {
            this.categories = data.data.categories.edges
            this.modules = data.data.modules.edges
          }
        }
      }
    }
  }
</script>

<style scoped>
  .category-wrapper {
    width: 100%;
  }
</style>
