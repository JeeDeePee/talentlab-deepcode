<template>
  <v-card>
    <v-card-text>
      <v-textarea
        :label="message"
        @input="handleInput"
        v-model="content"
        auto-grow
        full-width
        single-line
        hide-details
        placeholder="Erfasse deine Learnings">
      </v-textarea>
    </v-card-text>
    <v-card-actions>
      <!--<v-btn class="button primary item2 btn-minimal" outline @click="edit">-->
        <!--<v-icon color="primary">edit</v-icon>-->
      <!--</v-btn>-->
      <!--<v-btn class="button item2" @click="save">-->
        <!--Speichern-->
      <!--</v-btn>-->
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {
    props: ['message', 'value'],
    data () {
      return {
        content: this.value
      }
    },
    methods: {
      handleInput() {
        this.$emit('input', this.content)
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
