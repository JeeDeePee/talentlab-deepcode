<template>
  <div class="text-xs-center small--content">
    <h1>Dein Ziel</h1>
    <p class="mt-3">Zu Beginn des Moduls hast du folgendes Ziel ausgewahlt.</p>

    <div class="background--white-opacity pa-5 mt-5 mb-5 text--white">{{moduleUserGoal.text}}</div>

    <div class="">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'StartActionPlan')">Zurück</v-btn>
      <v-btn class="btn-primary ml-2" @click="$emit('proceed', 'Learnings')">Weiter</v-btn>
    </div>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    computed: {
      ...mapGetters({
        moduleUserGoal: 'getModuleUserGoal',
        user: 'getUser'
      }),
      moduleTitle() {
        return this.moduleUserGoal.module ? this.moduleUserGoal.module.title : ''
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
