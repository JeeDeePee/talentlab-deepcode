<template>
  <div v-if="module">
    <v-container class="mt-3">
      <span class="grey--text">{{module.category.title}} - {{module.skill}}</span><br>
      <h2 class="mb-1 mt-1">{{module.title}}</h2>
    </v-container>
    <div class="hero-bg mb-4">
      <v-container grid-list-md>
        <v-layout row wrap>
          <v-flex xs12 sm6 md6 lg6 xl6>
            <div v-html="module.description" class="mb-2 mt-1 description"></div>

            <div v-if="module.videoId" class="mt-5 mb-1">
              <a href="#" @click.stop="showVideoPlayer=true">
                <img class="video-thumbnail"
                     :src="module.videoThumbnailData.thumbnail_url_with_play_button"/>
              </a>
              <div v-html="module.videoDescription"></div>
              <VideoPlayer :visible="showVideoPlayer" :videoId="module.videoId" @close="showVideoPlayer=false"/>
            </div>

          </v-flex>
          <v-flex xs12 sm6 md6 lg6 xl6>
            <img :src="module.heroImage"/>
          </v-flex>
        </v-layout>
      </v-container>
    </div>

    <v-container grid-list-xl>
      <v-layout row wrap>
        <v-flex xs12 sm8 md8 lg8 xl8>
          <h3>Lernangebote</h3>
          <Unit v-for="(item, index) in module.units.edges" :key="index" :unit="item.node"  class="mb-4"></Unit>
        </v-flex>
        <v-flex xs12 sm4 md4 lg4 xl4>
          <h3>Ressourcen</h3>
          <Tools :tools="module.tools"/>
          <h3>Tools & Templates</h3>
          <Tools :tools="module.resources"/>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import MODULE_QUERY from '@/graphql/gql/module'
  import Tools from '@/components/Tools'
  import VideoPlayer from '@/components/VideoPlayer'
  import Unit from '@/components/Unit'

  export default {
    name: 'page-module',
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
        module: null,
        showVideoPlayer: false
      }
    },
    created() {
      this.$apollo.addSmartQuery('container', {
        query: MODULE_QUERY,
        variables: {
          slug: this.slug
        },
        manual: true,
        result(data, loading, networkStatus) {
          if (!loading) {
            let _module = this.$lodash.clone(data.data.modules.edges[0].node)

            _module.tools = JSON.parse(_module.tools)
            _module.resources = JSON.parse(_module.resources)
            _module.category = JSON.parse(_module.category)
            _module.videoThumbnailData = JSON.parse(_module.videoThumbnailData)

            this.module = _module
            document.title = _module.title
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
