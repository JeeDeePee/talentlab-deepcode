<template>
  <div class="grey--text">
    <h2>Job-Context und Motivation</h2>

    <v-container fluid grid-list-xl>
      <p>
        Beschreibe deinen Job-Context und deine Motivation
      </p>

      <p>
        Schritt 1: Zunächst wird – zuhanden Besprechung mit dem Learning Advisor – eine kurze Beschreibung des Job-Context und der Motivation zur Buchung des Containers beim PARTICIPANT abgeholt.
      </p>
    </v-container>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn @click="$emit('proceed')">Motivation speichern</v-btn>
  </div>
</template>

<script>
  export default {
    name: 'my-motivation',

    // https://github.com/vuetifyjs/vuetify/issues/3466
    // https://stackoverflow.com/questions/50218773/typeerror-vm-refs-dialog-save-is-not-a-function-in-vuetifyjs

    methods: {},

    data() {
      return {
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
