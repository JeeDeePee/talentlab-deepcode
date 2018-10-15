<template>
  <div class="text-xs-center">
    <h1 class="text--violet">Vier Schritte zu deinem Action Plan</h1>

    <div class="mt-4 mb-5 lead">Zu Beginn des Moduls hast du folgendes Ziel formuliert. Passe es bei Bedarf noch einmal
      an.
    </div>

    <h2 class="text--orange mt-3">1</h2>
    <div class="bold">Rekapituliere Deine Ziele</div>

    <h2 class="text--orange mt-3">2</h2>
    <div class="bold">Reflektiere was Du gelernt hast</div>

    <h2 class="text--orange mt-3">3</h2>
    <div class="bold">Definiere Dein Business-Ziel</div>

    <h2 class="text--orange mt-3">4</h2>
    <div class="bold">Bestimme Massnahmen</div>

    <v-btn class="mt-5" @click="$emit('proceed', 'ReviseGoals')">Start</v-btn>
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
