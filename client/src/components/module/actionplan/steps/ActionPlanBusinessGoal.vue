<template>
  <div class="text-xs-center">
    <h1>Was soll sich ändern?</h1>
    <p>Beschreibe möglichst konkret das Zielbild aus Business-Sicht.</p>

    <v-container fluid grid-list-xl>
      <v-layout align-space-between justify-space-between row fill-height>
        <v-flex sm6>
          <v-layout align-space-between justify-space-between column fill-height>
            <v-flex>
              <p>Was möchtest Du in Deiner Organisation bewirken?</p>
            </v-flex>
            <v-flex>
              <v-spacer></v-spacer>
            </v-flex>
            <v-flex>
              <TextBox :placeholder="'Zielzustand/Wirkung'" v-model="actionPlan.impactText"></TextBox>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex sm6>
          <v-layout align-space-between justify-space-between column fill-height>
            <v-flex>
              <p>Woran merkst Du, dass Du erfolgreich bist?</p>
            </v-flex>
            <v-flex>
              <v-spacer></v-spacer>
            </v-flex>
            <v-flex justify-end>
              <TextBox :placeholder="'Wirkungsmessung'" v-model="actionPlan.measurementText"></TextBox>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>

    <v-btn class="btn-secondary" @click="$emit('back', 'Learnings')">Zurück</v-btn>
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
