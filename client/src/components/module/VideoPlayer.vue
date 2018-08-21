<template>
  <v-dialog v-model="show" fullscreen hide-overlay transition="dialog-bottom-transition" scrollable>
    <v-card tile>
      <v-btn class="btn--close" large flat icon @click.stop="show=false">
        <v-icon>close</v-icon>
      </v-btn>
      <v-container grid-list-xl text-xs-center>
        <v-layout row wrap>
          <v-flex xs10 offset-xs1>
            <vimeo-player ref="player" :video-id=videoId :autoplay="false" class="mt-5"></vimeo-player>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
  export default {
    props: ['visible', 'videoId'],

    computed: {
      show: {
        get() {
          return this.visible
        },
        set(value) {
          // console.log('setting value')
          if (!value) {
            // console.log('set video hidden')
            this.$emit('close')
            this.$refs.player.pause()
          } else {
            // console.log('set(): set video visible')
            this.$refs.player.play()
          }
          // TODO: why is the set(value) not called with the show=false
        }
      }
    },

    watch: {
      show: function() {
        // console.log('watching show')
        if (this.show) {
          // console.log('watch: set video visible')
          this.$refs.player.play()
        }
      }
    },

    created() {
      // if (!this.visible) {
      //   this.$refs.player.pause()
      // }
      // console.log(`created VideoPlayer: ${this.visible}`)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";
</style>
