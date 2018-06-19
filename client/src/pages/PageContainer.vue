<template>
  <div>
    <v-card class="mb-1">
    <!-- <v-card v-for="container in containers" v-bind:key="container.id" class="mb-1"> -->
      <v-card-title primary-title>
        <div v-if="container">
          <h2 class="headline mb-1">{{container.title}}</h2>
          <div v-for="(item, index) in container.units.edges" v-bind:key="index">
            <div>{{item.node.type}}: {{item.node.title}}</div>
            <div>{{item.node.teaser}}</div>
          </div>
        </div>
      </v-card-title>
      <!-- <v-card-actions>
        <v-btn flat color="orange">Share</v-btn>
        <v-btn flat color="orange">Explore</v-btn>
      </v-card-actions> -->
    </v-card>
  </div>
</template>

<script>
  // import store from '@/store/core'
  import CONTAINER_QUERY from '@/graphql/gql/container'

  export default {
    name: 'page-container',

    props: {
      id: {
        required: true,
        type: String
      }
    },

    data() {
      return {
        initialQuery: CONTAINER_QUERY,
        container: null
      }
    },

    apollo: {
      container: {
        query: CONTAINER_QUERY,
        manual: true,
        result({data: {containers: {edges}}, loading, networkStatus}) {
          if (!loading) {
            // debugger
            let _container = edges[0].node
            // let self = this
            // edges.forEach(function (container) {
              // console.log(container)
              // let node = self.$lodash.clone(item.node)
              // node.content = JSON.parse(node.content)
              // _containers.push(container.node)
            // })
            this.container = _container
            // debugger
          }
        }
      }
    }
  }
</script>

<style scoped>

</style>
