<template>
  <div>
    <v-card-title primary-title>
      <div>
        <h2 class="headline mb-1">{{container.title}}</h2>
        <div>{{container.slug}}</div>

        <router-link :to="{name: 'container', params: {id: container.slug}}">
          {{ container.title }}
        </router-link>

        <!-- <div class="mt-2" v-for="(item, index) in container.units.edges" v-bind:key="index">
          {{item.node.type}}: {{item.node.title}}
          {{item.node.teaser}}
        </div> -->
      </div>
    </v-card-title>
  </div>
</template>

<script>
  // import store from '@/store/core'
  // import CONTAINERS_QUERY from '@/graphql/gql/containers'

  export default {
    name: 'container-teaser',

    props: {
      container: {
        required: true,
        type: Object
      }
    }
  }
</script>

<style scoped>
</style>
