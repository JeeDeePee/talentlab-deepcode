<template>
  <div class="text-xs-center">
    <h1 class="text--violet">Was soll sich ändern?</h1>
    <div class="mt-4 mb-5 lead">Beschreibe möglichst konkret das Zielbild aus Business-Sicht.</div>

    <v-layout>
      <v-flex sm6>
        <div class="mb-3">Was möchtest Du in Deiner Organisation bewirken?</div>
        <TextBox :placeholder="'Zielzustand/Wirkung'" v-model="actionPlan.impactText"></TextBox>
      </v-flex>
      <v-flex sm6>
        <div class="mb-3">Woran merkst Du, dass Du erfolgreich bist?</div>
        <TextBox :placeholder="'Wirkungsmessung'" v-model="actionPlan.measurementText"></TextBox>
      </v-flex>
    </v-layout>

    <div class="mt-5">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'Learnings')">Zurück</v-btn>
      <v-btn @click="save" class="ml-2">Weiter</v-btn>
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
            'impactText': this.actionPlan.impactText,
            'measurementText': this.actionPlan.measurementText
          }
        ])
        this.$emit('proceed', 'ActionPlanMeasures')
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
