<template>
  <div class="text-xs-center">
    <h1>Definiere Deinen Action Plan - Massnahmen</h1>

    <div></div>

    <v-btn class="btn-secondary" @click="$emit('back', 'ActionPlanBusinessGoal')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', 'ActionPlanOverview')">Weiter</v-btn>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    computed: {
      ...mapGetters({
      })
    },

    created() {
      // console.log(this.$options._componentTag)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
