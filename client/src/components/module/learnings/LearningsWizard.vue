<template>
  <Wizard v-model="show" :wizard-name="'Meine Learnings'" :process-steps="processSteps" @close="show=false">
    <div class="text-xs-center">

      <h1>Was sind Deine Learnings?</h1>
      <p>Hier erfasst Du laufend Deine wichtigsten Learnings aus dem Modul.</p>

      <TextBox :placeholder="'Text erfassen'" v-model="learningsText"></TextBox>
      <div>Why is this not displayed? ==> {{learningsText}}</div>

      <v-btn class="btn-secondary" @click="show=false">Zurück</v-btn>
      <v-btn @click="save">Speichern</v-btn>

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
          { text: 'Meine Learnings', disabled: false }
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
        this.defineActionPlan([{ 'learningsText': this.learningsText }])
        this.resetActionPlanWizardState()
        this.fetchModuleUserGoal()
        this.show = false
      }
    },

    watch: {
      actionPlan() {
        // console.log('WATCH actionPlan()')
        // console.log(this.actionPlan)
        this.learningsText = this.actionPlan.learningsText
      }
    },

    created() {
      this.newCurrentModule(this.module)
      this.fetchModuleUserGoal()
    }
  }
</script>

<style scoped>
</style>
