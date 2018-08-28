<template>
  <v-dialog v-model="show" fullscreen hide-overlay transition="dialog-bottom-transition" scrollable>
    <v-card tile>
      <div class="pa-2">
        <v-btn class="btn--close" large flat icon @click.stop="show=false">
          <v-icon>close</v-icon>
        </v-btn>

        <component
          :is="getActionPlanWizardState"
          v-on:back="newActionPlanWizardState"
          v-on:proceed="nextWizardStep">
        </component>

      </div>
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
