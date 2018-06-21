<template>
  <v-container grid-list-lg>
    <v-container fluid grid-list-md>
      <v-layout row wrap>
        <v-flex v-for="category in categories" v-bind:key="category.id" xs4 class="text-center">
          <img v-bind:src="category.node.icon"><br>
          {{category.node.title}}
        </v-flex>
        <v-flex xs12 sm6 v-for="container in containers" :key="container.node.id" class="mb-1">
          <ContainerTeaser :container="container.node"/>
        </v-flex>
      </v-layout>
    </v-container>
  </v-container>
</template>

<script>
  import CATEGORIES_QUERY from '@/graphql/gql/categories'
  import ContainerTeaser from '@/components/ContainerTeaser'

  export default {
    name: 'page-categories',

    components: {
      ContainerTeaser
    },

    data() {
      return {
        initialQuery: CATEGORIES_QUERY,
        categories: [],
        containers: []
      }
    },

    apollo: {
      categories: {
        query: CATEGORIES_QUERY,
        manual: true,
        result(data, loading, networkStatus) {
          if (!loading) {
            this.categories = data.data.categories.edges
            this.containers = data.data.containers.edges
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
