<template>
  <div class="text-xs-center">
    <h1>Drei Schritte bis zum Action Plan</h1>

    <h2 class="text--orange">1</h2>
    <p>Rekapituliere Deine Ziele</p>

    <h2 class="text--orange">2</h2>
    <p>Reflektiere was Du gelernt hast</p>

    <h2 class="text--orange">3</h2>
    <p>Definiere Dein Business-Ziel</p>

    <h2 class="text--orange">4</h2>
    <p>Bestimme Massnahmen</p>

    <v-btn @click="$emit('proceed', 'ReviseGoals')">Start</v-btn>
  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  export default {
    computed: {
      ...mapGetters({
        currentModule: 'getCurrentModule'
      })
    },

    methods: {
      ...mapActions({
        fetchModuleUserGoal: 'fetchModuleUserGoal'
      })
    },

    created() {
      this.fetchModuleUserGoal()
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
