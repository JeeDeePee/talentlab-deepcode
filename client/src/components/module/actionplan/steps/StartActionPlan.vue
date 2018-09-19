<template>
  <div class="text-xs-center">
    <h1>Vier Schritte bis zum Action Plan</h1>

    <h2 class="text--orange mt-3">1</h2>
    <div>Rekapituliere deine Ziele</div>

    <h2 class="text--orange mt-3">2</h2>
    <div>Reflektiere was du gelernt hast</div>

    <h2 class="text--orange mt-3">3</h2>
    <div>Definiere dein Business-Ziel</div>

    <h2 class="text--orange mt-3">4</h2>
    <div>Bestimme Massnahmen</div>

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
