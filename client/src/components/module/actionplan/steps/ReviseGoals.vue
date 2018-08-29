<template>
  <div class="grey--text">
    <h2>Rekapituliere Deine Ziele</h2>

    <div></div>

    <v-btn @click="$emit('back', 'StartActionPlan')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', 'Learnings')">Weiter</v-btn>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    props: ['breadcrumbs'],

    computed: {
      ...mapGetters({
      })
    },

    created() {
      // this.breadcrumbs[1].disabled = true
      console.log(this.$options._componentTag)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
