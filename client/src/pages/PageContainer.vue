<template>
  <v-container grid-list-md v-if="container">
    <span class="grey--text">{{container.category.title}} - {{container.skill}}</span><br>
    <h2 class="headline mb-1">{{container.title}}</h2>

    <v-layout row wrap>
      <v-flex xs12 sm6 md6 lg6 xl6>
        <div v-html="container.description" class="mb-2"></div>
        <vimeo-player :video-id='container.videoId' :player-height="'100px'"></vimeo-player>
        <div v-html="container.videoDescription"></div>

      </v-flex>
      <v-flex xs12 sm6 md6 lg6 xl6>
        <img v-bind:src="container.heroImage"/>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <v-flex xs12 sm8 md8 lg8 xl8>
        <h3>Lernangebote</h3>
        <v-card v-for="(item, index) in container.units.edges" v-bind:key="index" class="mb-1">
          <v-card-title primary-title>
            {{item.node.title}}
          </v-card-title>
          <v-card-text>
            {{item.node.type}} - {{item.node.count}} - {{item.node.duration}}
          </v-card-text>
        </v-card>
      </v-flex>
      <v-flex xs12 sm4 md4 lg4 xl4>
        <Tools :tools="container.tools" :title="'Ressourcen'"/>
        <Tools :tools="container.resources" :title="'Tools & Templates'"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  // import store from '@/store/core'
  import CONTAINER_QUERY from '@/graphql/gql/container'
  import Tools from '@/components/Tools'

  export default {
    name: 'page-container',
    props: {
      slug: {
        required: true,
        type: String
      }
    },
    components: {
      Tools
    },
    data() {
      return {
        container: null
      }
    },
    created() {
      this.$apollo.addSmartQuery('container', {
        query: CONTAINER_QUERY,
        variables: {
          slug: this.slug
        },
        manual: true,
        result(data, loading, networkStatus) {
          if (!loading) {
            let _container = this.$lodash.clone(data.data.containers.edges[0].node)

            _container.tools = JSON.parse(_container.tools)
            _container.resources = JSON.parse(_container.resources)
            _container.category = JSON.parse(_container.category)

            this.container = _container
          }
        }
      })
    }
  }
</script>

<style scoped lang="scss">
  img {
    max-width: 100%;
  }

</style>
