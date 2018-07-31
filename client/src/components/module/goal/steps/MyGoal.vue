<template>
  <div class="grey--text">
    <h2>Was ist dein Ziel</h2>

    <v-container fluid grid-list-xl>
      Wähle das Ziel, das am besten zu dir passt.
    </v-container>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn @click="$emit('proceed')">Ziel speichern</v-btn>
  </div>
</template>

<script>
  export default {
    name: 'my-goal',

    methods: {

    },

    data() {
      return {
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
