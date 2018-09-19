<template>
  <v-dialog v-model="show" persistent max-width="500px" class="background--white">
    <v-card class="light">
      <v-card-title class="dummy-chat">
        <span class="headline">Hallo 👋</span>
        <v-spacer></v-spacer>
        <v-btn flat icon depressed @click.stop="show=false">
          <v-icon>close</v-icon>
        </v-btn>
      </v-card-title>
      <v-card-text class="dummy-chat">
        <div>Das talenlab Team kann dich in sämtlichen Fragen zuverlässig und kompetent beraten.
        </div>

        <div class="mt-3 mb-4 text-xs-center">
          <v-avatar size="40px" v-for="(image, i) in items" :key="i" class="mr-1">
            <v-img
              :src="image"
              alt="mage"
            ></v-img>
          </v-avatar>
        </div>

        <v-textarea
          solo
          name="input-7-4"
          label="Schreibe eine nachricht ..."
          hide-details
        ></v-textarea>

      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn depressed @click.stop="show=false">Send</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
  export default {
    props: ['visible'],

    data() {
      return {
        items: [
          'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          'https://cdn.vuetifyjs.com/images/lists/4.jpg'
        ]
      }
    },
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

<style lang="scss">
  @import "../styles/var";

  .dummy-chat {
    label, textarea {
      color: $text-color !important;
    }
    .v-input__slot {
      background-color: $grey-2 !important;
      color: $text-color !important;
    }
    .v-btn .v-btn__content .v-icon {
      color: black;
    }
  }
</style>
