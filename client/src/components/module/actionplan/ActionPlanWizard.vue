<template>
  <v-dialog v-model="show" fullscreen hide-overlay transition="dialog-bottom-transition" scrollable>
    <v-card class="white--text">

      <v-toolbar dark color="primary">
        <v-toolbar-title>Action Plan</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn class="btn--close" large flat icon @click.stop="show=false">
            <v-icon>close</v-icon>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>

      <v-container>
        <v-layout align-center justify-center row fill-height>
          <v-flex xs12>

            <component
              :is="getActionPlanWizardState"
              v-on:back="newActionPlanWizardState"
              v-on:proceed="nextWizardStep">
            </component>

          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import StartActionPlan from '@/components/module/actionplan/steps/StartActionPlan'
  import ReviseGoals from '@/components/module/actionplan/steps/ReviseGoals'
  import Learnings from '@/components/module/actionplan/steps/Learnings'
  import ActionPlanBusinessGoal from '@/components/module/actionplan/steps/ActionPlanBusinessGoal'
  import ActionPlanMeasures from '@/components/module/actionplan/steps/ActionPlanMeasures'
  import ActionPlanOverview from '@/components/module/actionplan/steps/ActionPlanOverview'

  export default {
    props: {
      visible: {
        required: true,
        type: Boolean
      }
    },

    components: {
      StartActionPlan,
      ReviseGoals,
      Learnings,
      ActionPlanBusinessGoal,
      ActionPlanMeasures,
      ActionPlanOverview
    },

    data() {
      return {
        actionPlanWizardState: 'StartActionPlan'
      }
    },

    computed: {
      ...mapGetters({
        getActionPlanWizardState: 'getActionPlanWizardState'
      }),
      show: {
        get() {
          return this.visible
        },
        set(value) {
          if (!value) {
            this.$emit('close')
          }
        }
      }
    },

    methods: {
      ...mapActions({
        newActionPlanWizardState: 'newActionPlanWizardState'
      }),
      nextWizardStep(step, finishWizard) {
        if (finishWizard) {
          this.show = false
        }
        this.newActionPlanWizardState(step)
      }
    },

    created() {
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";
</style>
