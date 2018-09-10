<template>
  <div class="text-xs-center">
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
  import {mapActions, mapGetters} from 'vuex'

  export default {
    props: ['breadcrumbs'],

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
      // this.breadcrumbs[0].disabled = true
      // console.log(this.$options._componentTag)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
