<template>
  <div class="grey--text">
    <h2>Drei Schritte bis zum Action Plan</h2>

    <div></div>

    <!--<v-btn @click="$emit('back')">Zurück</v-btn>-->
    <v-btn @click="$emit('proceed', 'ReviseGoals')">Start</v-btn>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    computed: {
      ...mapGetters({
      })
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
