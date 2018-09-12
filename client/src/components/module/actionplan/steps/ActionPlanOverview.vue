<template>
  <div class="text-xs-center">
    <h1>Dein Action Plan steht!</h1>

    <h2>Talentlab wünscht Dir viel Spass und Erfolg bei der Umsetzung!</h2>
    <p>Dein Learning Advisor wird Dich in den nächsten Tagen für einen Review des Action Plans kontaktieren und weitere Schritte mit Dir besprechen.</p>

    <h2>{{currentModule}}</h2>


    <v-btn class="btn-secondary" @click="$emit('back', 'ActionPlanMeasures')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', 'StartActionPlan', true);">Weiter</v-btn>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    computed: {
      ...mapGetters({
        actionPlan: 'getActionPlan',
        currentModule: 'getCurrentModule',
        user: 'getUser'
      })
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
