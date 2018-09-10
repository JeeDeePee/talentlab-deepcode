<template>
  <Wizard v-model="show" :wizard-name="'Action Plan'" :process-steps="processSteps" @close="show=false">

    <component
      :is="getActionPlanWizardState"
      @back="newActionPlanWizardState"
      @proceed="nextWizardStep">
    </component>

  </Wizard>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import Wizard from '@/components/reusable/Wizard'

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
      },
      module: {
        required: true,
        type: Object
      }
    },

    components: {
      StartActionPlan,
      ReviseGoals,
      Learnings,
      ActionPlanBusinessGoal,
      ActionPlanMeasures,
      ActionPlanOverview,
      Wizard
    },

    data() {
      return {
        actionPlanWizardState: 'StartActionPlan',
        processSteps: [
          { text: 'Rekapitualtion Ziele', disabled: true },
          { text: 'Reflektion Learnings', disabled: true },
          { text: 'Definition Action Plan', disabled: true }
        ]
      }
    },

    computed: {
      ...mapGetters({
        getActionPlanWizardState: 'getActionPlanWizardState'
      }),
      // TODO: refactor with a mixin
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
        newActionPlanWizardState: 'newActionPlanWizardState',
        newCurrentModule: 'newCurrentModule'
      }),
      nextWizardStep(step, finishWizard) {
        if (finishWizard) {
          this.show = false
        }
        this.newActionPlanWizardState(step)
      }
    },

    created() {
      this.newCurrentModule(this.module)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";
</style>
