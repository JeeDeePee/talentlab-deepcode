<template>
  <div class="text-xs-center">
    <h1>Dein Ziel</h1>
    <p class="mt-3">Zu Beginn des Moduls hast Du folgendes Ziel formuliert. Passe es bei Bedarf noch einmal an.</p>

    <div class="module-user-goal pa-3 mt-5 mb-5">{{moduleUserGoal.text}}</div>

    <v-btn class="btn-secondary" @click="$emit('back', 'StartActionPlan')">Zurück</v-btn>
    <v-btn class="btn-primary" @click="$emit('proceed', 'Learnings')">Weiter</v-btn>
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

  .module-user-goal {
    background-color: rgba(255, 255, 255, 0.2);
    font-size: 150%;
    max-width: 620px;
    margin: auto;
  }
</style>
