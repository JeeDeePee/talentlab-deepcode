<template>
  <div>

    <v-card v-for="category in categories" v-bind:key="category.id" class="mb-1">
      <v-card-title primary-title>
        <div>
          <h2 class="headline mb-1">{{category.title}}</h2>
        </div>
      </v-card-title>
    </v-card>

  </div>
</template>

<script>
  import store from '@/store/core'
  import CATEGORIES_QUERY from '@/graphql/gql/categories'

  export default {
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
          }
        }
      }
    }
  }
</script>

<style scoped>

</style>
