<template>
  <Wizard :visible="visible" :wizardName="'Meine Learnings'" :process-steps="processSteps" @close="show=false">
    <div class="text-xs-center">
      <h1>Was sind Deine Learnings?</h1>
      <p>Hier erfasst Du laufend Deine wichtigsten Learnings aus dem Modul.</p>

      <TextBox :placeholder="'Text erfassen'" v-model="actionPlan.learningsText"></TextBox>
      <TextBox :placeholder="'Deine Learnings'" v-model="actionPlan.learningsText"></TextBox>

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
      visible: Boolean,
      module: { required: true, type: Object }
    },

    components: { TextBox, Wizard },

    data() {
      return {
        actionPlanWizardState: 'StartActionPlan',
        processSteps: [
          { text: 'Meine Motivation', disabled: true },
          { text: 'Mein Ziel', disabled: true },
          { text: 'Meine Learnings', disabled: false },
          { text: 'Mein Action Plan', disabled: true }
        ]
      }
    },

    computed: {
      ...mapGetters({
        getActionPlanWizardState: 'getActionPlanWizardState',
        actionPlan: 'getActionPlan'
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
        defineActionPlan: 'defineActionPlan',
        fetchModuleUserGoal: 'fetchModuleUserGoal',
        newCurrentModule: 'newCurrentModule'
      }),
      save() {
        this.defineActionPlan([{ 'learningsText': this.actionPlan.learningsText }])
        this.show = false
      }
    },

    created() {
      // debugger
      // this.newCurrentModule(this.module)
      // this.fetchModuleUserGoal(this.module)
    }
  }
</script>

<style scoped>
</style>
