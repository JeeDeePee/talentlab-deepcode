<template>
  <v-flex xs12 sm6 class="mb-1">
    <v-card>
      <v-form>
        <v-textarea v-model="initial" :label="message" counter maxlength="1200" full-width single-line>
        </v-textarea>
      </v-form>
      <v-toolbar card dark>
        <v-btn class="button item2" @click="edit">
          <v-icon>edit</v-icon>
        </v-btn>
        <v-btn class="button item2" @click="save">
          Speichern
        </v-btn>
      </v-toolbar>
    </v-card>
  </v-flex>
</template>

<script>
  export default {
    props: ['message', 'initial'],

    data() {
      return {
        text: ''
      }
    },

    methods: {
      edit() {
        // console.log(`Edit text: ${this.text}`)
      },
      save() {
        // console.log(`Save text: ${this.text}`)
        this.$emit('save', this.text)
      }
    }
  }
</script>

<style scoped>
</style>
