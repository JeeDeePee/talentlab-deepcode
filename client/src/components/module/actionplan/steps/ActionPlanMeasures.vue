<template>
  <div class="text-xs-center">
    <h1 class="text--violet">Was tust du dazu?</h1>
    <div class="mt-4 mb-5 lead">Konkretisiere Massnahmen, Termine, Ressourcen und den benötigten Support.</div>

    <v-layout row wrap>
      <v-flex xs12 sm4>
        <div class="three-line bold">Welche Massnahmen ergreifst Du bis wann?</div>
        <TextBox :placeholder="'Umsetzungsmassnahmen'" v-model="actionPlan.measuresText"></TextBox>
      </v-flex>

      <v-flex xs12 sm4>
        <div class="three-line bold">Welche Ressourcen und/oder Skills benötigst Du?</div>
        <TextBox :placeholder="'Benötigte Ressourcen/Skills'" v-model="actionPlan.resourcesSkillsText"></TextBox>
      </v-flex>

      <v-flex xs12 sm4>
        <div class="three-line bold">Von wem benötigst Du Unterstützung?</div>
        <TextBox :placeholder="'Commitment'" v-model="actionPlan.commitmentSupportText"></TextBox>
      </v-flex>
    </v-layout>

    <div class="mt-5">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'ActionPlanBusinessGoal')">Zurück</v-btn>
      <v-btn class="ml-2" @click="save">Weiter</v-btn>
    </div>
  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'
  import TextBox from '@/components/reusable/TextBox'

  export default {
    components: {
      TextBox
    },

    computed: {
      ...mapGetters({
        actionPlan: 'getActionPlan'
      })
    },

    methods: {
      ...mapActions({
        defineActionPlan: 'defineActionPlan'
      }),
      save() {
        this.defineActionPlan([
          {
            'measuresText': this.actionPlan.measuresText,
            // 'timeFrameText': this.actionPlan.timeFrameText,
            'resourcesSkillsText': this.actionPlan.resourcesSkillsText,
            'commitmentSupportText': this.actionPlan.commitmentSupportText
          }
        ])
        this.$emit('proceed', 'ActionPlanOverview')
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
