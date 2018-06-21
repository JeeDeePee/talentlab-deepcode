<template>
  <v-dialog
    v-model="show"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    scrollable
  >
    <v-card tile>
      <v-container grid-list-xl text-xs-center>
        <v-layout row wrap>
          <v-flex xs10 offset-xs1>
            <v-btn color="primary" flat @click.stop="show=false">Close</v-btn>
            <vimeo-player :video-id=videoId :autoplay="true"></vimeo-player>
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
          if (!value) {
            this.$emit('close')
          }
        }
      }
    }
  }
</script>
