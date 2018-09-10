<template>
  <div class="text-xs-center">
    <h1>Definiere Deinen Action Plan - Massnahmen</h1>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex sm6>
          <p>Welche Umsetzungsmassnahmen leitest Du ein?</p>
        </v-flex>
        <v-flex sm6>
          <p>Was ist Dein Zeitrahmen?</p>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-flex sm6>
          <TextBox :placeholder="'Umsetzungsmassnahmen'" v-model="actionPlan.measuresText"></TextBox>
        </v-flex>
        <v-flex sm6>
          <TextBox :placeholder="'Zeitrahmen'" v-model="actionPlan.timeFrameText"></TextBox>
        </v-flex>
      </v-layout>

      <v-layout row wrap>
        <v-flex sm6>
          <p>Welche Ressourcen/Skills benötigst Du?</p>
        </v-flex>
        <v-flex sm6>
          <p>Von wem innerhalb oder ausserhalb der Organisation benötigst Du Commitment?</p>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-flex sm6>
          <TextBox :placeholder="'Benötigte Ressourcen/Skills'" v-model="actionPlan.resourcesSkillsText"></TextBox>
        </v-flex>
        <v-flex sm6>
          <TextBox :placeholder="'Commitment'" v-model="actionPlan.commitmentSupportText"></TextBox>
        </v-flex>
      </v-layout>
    </v-container>

    <v-btn class="btn-secondary" @click="$emit('back', 'ActionPlanBusinessGoal')">Zurück</v-btn>
    <v-btn @click="save">Weiter</v-btn>
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
            'timeFrameText': this.actionPlan.timeFrameText,
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
