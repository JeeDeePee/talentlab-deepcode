<template>
  <div>
    <v-container class="mt-3">
      <span class="grey--text">{{module.category.title}} - {{module.skill}}</span><br>
      <h2 class="mb-1 mt-1">{{module.title}}</h2>
      <v-btn class="button item2" @click="$emit('start-module-progress', module.slug)">
        Container buchen
      </v-btn>

    </v-container>
    <div class="hero-bg mb-4">
      <v-container grid-list-md>
        <v-layout row wrap>
          <v-flex xs12 sm6 md6 lg6 xl6>
            <div v-html="module.description" class="mb-2 mt-1 description"></div>

            <div v-if="module.videoId" class="mt-5 mb-1">
              <a href="#" @click.stop="showVideoPlayer=true">
                <img class="video-thumbnail" :src="module.videoThumbnailData.thumbnail_url_with_play_button"/>
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
          <Unit v-for="(item, index) in module.units.edges" :key="index" :unit="item.node" class="mb-4" :booked="false"></Unit>
        </v-flex>
        <v-flex xs12 sm4 md4 lg4 xl4>
          <h3>Ressourcen</h3>
              <v-card class="bg mb-5">
                <v-card-text>
                  <div class="mt-1 mb-3">
                    <i class="material-icons icon-color">library_books</i>
                  </div>
                  Hier werden bei Buchung weiterführende Inhalte ergänzt.
                </v-card-text>
              </v-card>
          <h3>Tools & Templates</h3>
              <v-card class="bg mb-5">
                <v-card-text>
                  <div class="mt-1 mb-3">
                    <i class="material-icons icon-color">library_books</i>
                  </div>
                  Hier werden bei Buchung nützliche Dokumente ergänzt.
                </v-card-text>
              </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import Tools from '@/components/module/Tools'
  import VideoPlayer from '@/components/module/VideoPlayer'
  import Unit from '@/components/module/Unit'

  export default {
    name: 'module-detail',

    props: {
      module: {
        required: true,
        type: Object
      }
    },

    components: {
      Tools,
      VideoPlayer,
      Unit
    },

    data() {
      return {
        showVideoPlayer: false
      }
    },

    methods: {
      // ...mapActions({
      //   startModuleProgress: 'startModuleProgress'
      // })
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

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

  .bg {
    background-color: $grey-3;
  }

  .icon-color {
    color: $orange;
  }
</style>
