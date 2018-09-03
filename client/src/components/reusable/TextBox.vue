<template>
  <v-card>
    <v-card-text>
      <v-textarea
        v-model="initial"
        :label="message"
        auto-grow
        full-width
        single-line
        hide-details="true"
        placeholder="Erfasse deine Learnings">
      </v-textarea>
    </v-card-text>
    <v-card-actions>
      <v-btn class="button primary item2 btn-minimal" outline @click="edit">
        <v-icon color="primary">edit</v-icon>
      </v-btn>
      <v-btn class="button item2" @click="save">
        Speichern
      </v-btn>
    </v-card-actions>
  </v-card>
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

<style lang="scss" scoped>
  .v-card {
    box-shadow: initial;
  }

  .v-card__actions {
    border-top: initial;
  }

  .v-textarea {
    background-color: rgba(255, 255, 255, 0.2);
    margin: auto;

    textarea::placeholder {
      color: red;
    }
  }
</style>
