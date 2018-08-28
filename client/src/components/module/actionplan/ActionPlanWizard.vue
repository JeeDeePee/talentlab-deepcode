<template>
  <v-dialog v-model="show" fullscreen hide-overlay transition="dialog-bottom-transition" scrollable>
    <v-card tile>
      <div class="pa-2">
        <v-btn class="btn--close" large flat icon @click.stop="show=false">
          <v-icon>close</v-icon>
        </v-btn>

        <StartActionPlan
          v-on:proceed="newActionPlanWizardState($event)"
          v-if="isCurrentWizardState('StartActionPlan')">
        </StartActionPlan>
        <ReviseGoals
          v-on:back="newActionPlanWizardState($event)"
          v-on:proceed="newActionPlanWizardState($event)"
          v-if="isCurrentWizardState('ReviseGoals')">
        </ReviseGoals>
        <Learnings
          v-on:back="newActionPlanWizardState($event)"
          v-on:proceed="newActionPlanWizardState($event)"
          v-if="isCurrentWizardState('Learnings')">
        </Learnings>
        <ActionPlanBusinessGoal
          v-on:back="newActionPlanWizardState($event)"
          v-on:proceed="newActionPlanWizardState($event)"
          v-if="isCurrentWizardState('ActionPlanBusinessGoal')">
        </ActionPlanBusinessGoal>
        <ActionPlanMeasures
          v-on:back="newActionPlanWizardState($event)"
          v-on:proceed="newActionPlanWizardState($event)"
          v-if="isCurrentWizardState('ActionPlanMeasures')">
        </ActionPlanMeasures>
        <ActionPlanOverview
          v-on:back="newActionPlanWizardState($event)"
          v-on:proceed="newActionPlanWizardState($event)"
          v-if="isCurrentWizardState('ActionPlanOverview')">
        </ActionPlanOverview>

        <!--<ActionPlanOverview-->
          <!--v-on:back="newActionPlanWizardState($event)"-->
          <!--v-on:proceed="newActionPlanWizardState($event); show=false"-->
          <!--v-if="isCurrentWizardState('ActionPlanOverview')">-->
        <!--</ActionPlanOverview>-->

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
        getActionPlanWizardState: 'getActionPlanWizardState',
        isCurrentWizardState: 'isCurrentWizardState'
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
      })
    },

    created() {
      // this.$store.dispatch('fetchModuleGoals', { moduleSlug: this.module.slug })
    }

    // methods: {
    //   myGoalBack() {
    //     this.$emit('close')
    //   },
    //
    //   myGoalProceed(goalLevel) {
    //     this.$emit('close')
    //     this.storeMyGoal(this.module.slug, goalLevel)
    //   },
    //
    //   storeMyGoal(moduleSlug, goalLevel) {
    //     console.log(`storeMyGoal(moduleSlug: ${moduleSlug}, goalLevel: ${goalLevel})`)
    //
    //     this.$apollo.mutate({
    //       mutation: DEFINE_USER_GOAL,
    //       variables: {
    //         moduleSlug: moduleSlug,
    //         goalLevel: goalLevel
    //       }
    //     }).then(data => {
    //       // console.log('Done storing goal.');
    //     });
    //   }
    // }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";
</style>
