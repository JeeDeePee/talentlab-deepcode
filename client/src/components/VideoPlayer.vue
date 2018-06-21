<template>
  <v-dialog
    v-model="show"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    scrollable
  >
    <v-card tile>
      <v-btn class="close" large flat icon @click.stop="show=false">
        <v-icon>close</v-icon>
      </v-btn>
      <v-container grid-list-xl text-xs-center>
        <v-layout row wrap>
          <v-flex xs10 offset-xs1>
            <vimeo-player :video-id=videoId :autoplay="true" class="mt-5"></vimeo-player>
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

<style lang="scss" scoped>
  @import "../styles/var";

  .card {
    background-color: $grey-9;
  }

  .close {
    color: #fff;
    position: absolute;
    right: 0;

    .icon {
      font-size: 50px;
    }
  }

</style>
