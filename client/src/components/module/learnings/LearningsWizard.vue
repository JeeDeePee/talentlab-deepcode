<template>
  <Wizard v-model="show" :wizard-name="'Meine Learnings'" :process-steps="processSteps"
          @close="show=false">
    <div class="text-xs-center small--content">

      <h1 class="text-xs-center text--violet">Was sind Deine Learnings?</h1>
      <div class="mt-4 mb-5 lead">Hier erfasst Du laufend Deine wichtigsten Learnings aus dem Modul</div>

      <TextBox :placeholder="'Text erfassen'" v-model="learningsText"></TextBox>

      <div class="mt-5">
        <v-btn class="btn-secondary mr-2" @click="show=false">Zurück</v-btn>
        <v-btn class="ml-2" @click="save">Speichern</v-btn>
      </div>

    </div>
  </Wizard>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import Wizard from '@/components/reusable/Wizard'
  import TextBox from '@/components/reusable/TextBox'

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
      TextBox,
      Wizard
    },

    data() {
      return {
        learningsText: '',
        processSteps: [
          {text: 'Meine Learnings', disabled: false}
        ]
      }
    },

    computed: {
      ...mapGetters({
        actionPlan: 'getActionPlan'
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
        defineActionPlan: 'defineActionPlan',
        fetchModuleUserGoal: 'fetchModuleUserGoal',
        newCurrentModule: 'newCurrentModule',
        resetActionPlanWizardState: 'resetActionPlanWizardState'
      }),
      save() {
        this.defineActionPlan([{'learningsText': this.learningsText}])
        this.resetActionPlanWizardState()
        this.fetchModuleUserGoal()
        this.show = false
      }
    },

    watch: {
      actionPlan() {
        this.learningsText = this.actionPlan.learningsText
      }
    },

    created() {
      this.newCurrentModule(this.module)
      this.fetchModuleUserGoal()
    }
  }
</script>

<style lang="scss" scoped>
</style>
