<template>
  <div class="text-xs-center">
    <h1>Rekapituliere Deine Ziele</h1>
    <p>Dein Ziel zum Container «Digital Communication & Virtual Collaboration». Passe bei Bedarf noch einmal an.</p>

    <div class="module-user-goal pa-3 mt-5 mb-5">{{moduleUserGoal.text}}</div>

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
        moduleUserGoal: 'getModuleUserGoal'
      })
    },

    created() {
      this.$store.dispatch('fetchModuleUserGoal')
      // this.breadcrumbs[1].disabled = true
      // console.log(this.$options._componentTag)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";

  .module-user-goal {
    background-color: rgba(255, 255, 255, 0.2);
    font-size: 150%;
    max-width: 620px;
    margin: auto;
  }
</style>
