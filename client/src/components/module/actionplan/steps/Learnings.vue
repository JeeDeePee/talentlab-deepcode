<template>
  <div class="grey--text">
    <h2>Reflektiere was Du gelernt hast</h2>

    <div></div>

    <v-btn @click="$emit('back', 'ReviseGoals')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', 'ActionPlanBusinessGoal')">Weiter</v-btn>
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
      // this.breadcrumbs[2].disabled = true
      console.log(this.$options._componentTag)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
