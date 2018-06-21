<template>
  <div v-if="container">
    <v-container class="mt-3">
      <span class="grey--text">{{container.category.title}} - {{container.skill}}</span><br>
      <h2 class="mb-1 mt-1">{{container.title}}</h2>
    </v-container>
    <div class="hero-bg mb-4">
      <v-container grid-list-md>
        <v-layout row wrap>
          <v-flex xs12 sm6 md6 lg6 xl6>
            <div v-html="container.description" class="mb-2 description"></div>

            <div v-if="container.videoId" class="mt-5">
              <a href="#" @click.stop="showVideoPlayer=true">
                <img class="video-thumbnail"
                     v-bind:src="container.videoThumbnailData.thumbnail_url_with_play_button"/>
              </a>
              <div v-html="container.videoDescription"></div>
              <VideoPlayer :visible="showVideoPlayer" :videoId="container.videoId" @close="showVideoPlayer=false"/>
            </div>

          </v-flex>
          <v-flex xs12 sm6 md6 lg6 xl6>
            <img v-bind:src="container.heroImage"/>
          </v-flex>
        </v-layout>
      </v-container>
    </div>

    <v-container grid-list-xl>
      <v-layout row wrap>
        <v-flex xs12 sm8 md8 lg8 xl8>
          <h3>Lernangebote</h3>
          <Unit v-for="(item, index) in container.units.edges" v-bind:key="index" :unit="item.node"  class="mb-4"></Unit>
        </v-flex>
        <v-flex xs12 sm4 md4 lg4 xl4>
          <h3>Ressourcen</h3>
          <Tools :tools="container.tools"/>
          <h3>Tools & Templates</h3>
          <Tools :tools="container.resources"/>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import CONTAINER_QUERY from '@/graphql/gql/container'
  import Tools from '@/components/Tools'
  import VideoPlayer from '@/components/VideoPlayer'
  import Unit from '@/components/Unit'

  export default {
    name: 'page-container',
    props: {
      slug: {
        required: true,
        type: String
      }
    },
    components: {
      Tools,
      VideoPlayer,
      Unit
    },
    data() {
      return {
        container: null,
        showVideoPlayer: false
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
            _container.videoThumbnailData = JSON.parse(_container.videoThumbnailData)

            this.container = _container
            document.title = _container.title
          }
        }
      })
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  img {
    max-width: 100%;
  }

  h2 {
    font-size: 44px;
  }

  h3 {
    font-size: 24px;
    margin-bottom: 12px;
  }

  .video-thumbnail {
    max-width: 200px;
  }

  .hero-bg {
    background-color: $blue;
  }

  .description {
    font-size: 18px;
    font-weight: bold;
  }

</style>
