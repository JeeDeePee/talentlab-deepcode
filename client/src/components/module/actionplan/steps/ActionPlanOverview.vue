<template>
  <div class="text-xs-center">
    <h1>Dein Action Plan steht!</h1>

    <div></div>

    <v-btn class="btn-secondary" @click="$emit('back', 'ActionPlanMeasures')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', 'StartActionPlan', true);">Weiter</v-btn>
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
