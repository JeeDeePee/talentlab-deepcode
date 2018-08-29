<template>
  <v-dialog v-model="show" fullscreen hide-overlay transition="dialog-bottom-transition" scrollable>
    <v-card class="white--text">

      <v-toolbar dark color="primary" class="ml-4 mr-4">
        <v-toolbar-title>Action Plan</v-toolbar-title>
        <div class="toolbar-accent"></div>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn large flat icon @click.stop="show=false">
            <v-icon>close</v-icon>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>

      <v-breadcrumbs class="ml-4 mr-4">
        <v-icon slot="divider">chevron_right</v-icon>
        <v-breadcrumbs-item v-for="breadcrumb in breadcrumbs"
                            :key="breadcrumb.text"
                            :disabled="breadcrumb.disabled"
                            class="breadcrumbs-item"
                            @click="newActionPlanWizardState = breadcrumb.activeComponent">
          {{breadcrumb.text}}
        </v-breadcrumbs-item>
      </v-breadcrumbs>

      <v-container>
        <v-layout align-center justify-center row fill-height>
          <v-flex xs12>

            <component
              :is="getActionPlanWizardState"
              v-on:back="newActionPlanWizardState"
              v-on:proceed="nextWizardStep"
              :breadcrumbs="breadcrumbs">
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
      module: {
        required: true,
        type: Object
      },
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
        actionPlanWizardState: 'StartActionPlan',
        breadcrumbs: [
          {
            text: 'Rekapitualtion Ziele',
            activeComponent: 'ReviseGoals',
            disabledWhen: []
          },
          {
            text: 'Reflektion Learnings',
            activeComponent: 'Learnings',
            disabledWhen: ['ReviseGoals']
          },
          {
            text: 'Definition Action Plan',
            activeComponent: 'ActionPlanBusinessGoal',
            disabledWhen: []
          }
        ]
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
