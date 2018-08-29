<template>
  <div class="text-center">
    <h1>Drei Schritte bis zum Action Plan</h1>

    <h2 class="text--primary-accent">1</h2>
    <p>Rekapituliere Deine Ziele</p>

    <h2 class="text--primary-accent">2</h2>
    <p>Reflektiere was Du gelernt hast</p>

    <h2 class="text--primary-accent">3</h2>
    <p>Definiere Deinen Action Plan</p>

    <v-btn @click="$emit('proceed', 'ReviseGoals')">Start</v-btn>
  </div>

</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    computed: {
      ...mapGetters({})
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
