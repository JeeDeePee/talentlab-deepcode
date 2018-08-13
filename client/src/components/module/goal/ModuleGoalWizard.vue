<template>
  <v-dialog v-model="show" fullscreen hide-overlay transition="dialog-bottom-transition" scrollable>
    <v-card tile>
      <div class="pa-2">
        <v-btn class="btn--close" large flat icon @click.stop="show=false">
          <v-icon>close</v-icon>
        </v-btn>

        <v-breadcrumbs>
          <v-icon slot="divider">chevron_right</v-icon>
          <v-breadcrumbs-item :disabled="isMyMotivation">
            Meine Motivation
          </v-breadcrumbs-item>
          <v-breadcrumbs-item :disabled="isMyGoal">
            Mein Ziel
          </v-breadcrumbs-item>
        </v-breadcrumbs>

        <MyMotivation
          v-on:proceed="myMotivationProceed($event)"
          v-on:back="myMotivationBack($event)"
          v-if="isMyMotivation">
        </MyMotivation>
        <MyGoal
          v-on:proceed="myGoalProceed($event)"
          v-on:back="myGoalBack($event)"
          v-if="isMyGoal">
        </MyGoal>

      </div>
    </v-card>
  </v-dialog>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import MyMotivation from '@/components/module/goal/steps/MyMotivation'
  import MyGoal from '@/components/module/goal/steps/MyGoal'

  export default {
    name: 'module-goal-wizard',

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
      MyMotivation,
      MyGoal
    },

    data() {
      return {
      }
    },

    computed: {
      ...mapGetters({
        isMyMotivation: 'isMyMotivation',
        isMyGoal: 'isMyGoal'
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

    created() {
      this.$store.dispatch('fetchModuleGoals', { moduleSlug: this.module.slug })
    },

    methods: {
      ...mapActions({
        newModuleGoalWizardState_MyMotivation: 'newModuleGoalWizardState_MyMotivation',
        newModuleGoalWizardState_MyGoal: 'newModuleGoalWizardState_MyGoal'
      }),

      myMotivationProceed() {
        this.newModuleGoalWizardState_MyGoal()
      },

      myMotivationBack() {
        this.newModuleGoalWizardState_MyMotivation()
        this.$emit('close')
      },

      myGoalProceed() {
        this.newModuleGoalWizardState_MyMotivation()
        this.$emit('close')
      },

      myGoalBack() {
        this.newModuleGoalWizardState_MyMotivation()
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";
</style>
