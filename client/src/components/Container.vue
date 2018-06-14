<template>
  <div>

    <v-card v-for="container in containers" v-bind:key="container.id" class="mb-1">
      <v-card-title primary-title>
        <div>
          <h2 class="headline mb-1">{{container.title}}</h2>
          <div class="mt-2" v-for="(item, index) in container.content" v-bind:key="index">
            <div v-if="item.type=='text'" v-html="item.value.text"></div>
            <div v-else>
              {{item.type}}: {{item.value}}
            </div>
          </div>
        </div>
      </v-card-title>
      <v-card-actions>
        <v-btn flat color="orange">Share</v-btn>
        <v-btn flat color="orange">Explore</v-btn>
      </v-card-actions>
    </v-card>

  </div>
</template>

<script>
  import store from '@/store/core'
  import CONTAINERS_QUERY from '@/graphql/containers'

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
            let _items = []
            let self = this
            edges.forEach(function (item) {
              let node = self.$lodash.clone(item.node)
              node.content = JSON.parse(node.content)
              _items.push(node)
            })
            this.containers = _items
          }
        }
      }
    }
  }
</script>

<style scoped>

</style>
