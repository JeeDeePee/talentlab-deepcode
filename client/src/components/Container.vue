<template>
  <div>

    <v-card v-for="container in containers">
      <v-card-title primary-title>
        <div>
          <h3 class="headline mb-0">{{container.title}}</h3>
          {{container.content}}
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
        query: CONTAINERS_QUERY
      }
    }
  }
</script>

<style scoped>

</style>
