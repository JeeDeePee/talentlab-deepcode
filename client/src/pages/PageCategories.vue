<template>
  <div>
    <v-card v-for="category in categories" v-bind:key="category.id" class="mb-1">
      <v-card-title primary-title>
        <div>
          <h2 class="headline mb-1">{{category.title}}</h2>
          <ContainerTeaser v-for="container in category.containers.edges"
                           :container="container.node"
                           :key="container.node.id"/>
        </div>
      </v-card-title>
    </v-card>
  </div>
</template>

<script>
  import store from '@/store/core'
  import CATEGORIES_QUERY from '@/graphql/gql/categories'
  import ContainerTeaser from '@/components/ContainerTeaser'

  export default {
    name: 'page-categories',

    components: {
      ContainerTeaser
    },

    data() {
      return {
        store: store,
        initialQuery: CATEGORIES_QUERY,
        categories: []
      }
    },

    apollo: {
      categories: {
        query: CATEGORIES_QUERY,
        manual: true,
        result({data: {categories: {edges}}, loading, networkStatus}) {
          if (!loading) {
            // debugger
            let _categories = []
            // let self = this
            edges.forEach(function (category) {
              // let node = self.$lodash.clone(item.node)
              // node.content = JSON.parse(node.content)
              _categories.push(category.node)
            })
            this.categories = _categories
            // debugger
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
