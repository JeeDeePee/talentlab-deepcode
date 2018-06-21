<template>
  <v-dialog
    v-model="show"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    scrollable
  >
    <v-card tile>
      <vimeo-player :video-id=videoId :autoplay="true"></vimeo-player>
      <v-btn color="primary" flat @click.stop="show=false">Close</v-btn>
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
