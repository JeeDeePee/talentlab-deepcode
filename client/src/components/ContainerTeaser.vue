<template>
  <div>

    <v-card v-for="container in containers" v-bind:key="container.id" class="mb-1">
      <v-card-title primary-title>
        <div>
          <h2 class="headline mb-1">{{container.title}}</h2>
          <div class="mt-2" v-for="(item, index) in container.units.edges" v-bind:key="index">
            {{item.node.type}}: {{item.node.title}}
            {{item.node.teaser}}
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
  import store from '@/store/core'
  import CONTAINERS_QUERY from '@/graphql/gql/containers'

  export default {
    data() {
      return {
        store: store,
        initialQuery: CONTAINERS_QUERY,
        containers: []
      }
    },
    apollo: {
      containers: {
        query: CONTAINERS_QUERY,
        manual: true,
        result({data: {containers: {edges}}, loading, networkStatus}) {
          if (!loading) {
            // debugger
            let _containers = []
            // let self = this
            edges.forEach(function (container) {
              console.log(container)
              // let node = self.$lodash.clone(item.node)
              // node.content = JSON.parse(node.content)
              _containers.push(container.node)
            })
            this.containers = _containers
          }
        }
      }
    }
  }
</script>

<style scoped>

</style>
