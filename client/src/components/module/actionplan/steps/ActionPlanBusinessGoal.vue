<template>
  <div class="grey--text">
    <h2>Definiere Deinen Action Plan - Business-Ziel</h2>

    <div></div>

    <v-btn @click="$emit('back', 'Learnings')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', 'ActionPlanMeasures')">Weiter</v-btn>
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
