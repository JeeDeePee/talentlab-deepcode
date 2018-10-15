<template>
  <Wizard v-model="show" :process-steps="processSteps" @close="show=false">
    <div class="medium--content">
      <component
        :is="getCoachingWizardState"
        @back="newCoachingWizardState"
        @proceed="nextWizardStep">
      </component>
    </div>

  </Wizard>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import Wizard from '@/components/reusable/Wizard'

  import Coaches from '@/components/coaching/steps/Coaches'
  import Organize from '@/components/coaching/steps/Organize'
  import Topics from '@/components/coaching/steps/Topics'

  export default {
    props: {
      visible: {
        required: true,
        type: Boolean
      }
    },

    components: {
      Wizard,
      Coaches,
      Organize,
      Topics
    },

    data() {
      return {
        CoachingWizardState: 'Coaches',
        processSteps: [
          {text: 'Coaching Thema auswählen', disabled: true},
          {text: 'Coach Finden', disabled: true},
          {text: 'Coaching Sessions organisieren', disabled: true}
        ]
      }
    },

    computed: {
      ...mapGetters({
        getCoachingWizardState: 'getCoachingWizardState'
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
        newCoachingWizardState: 'newCoachingWizardState'
      }),
      nextWizardStep(step, finishWizard) {
        if (finishWizard) {
          this.show = false
        }
        this.newCoachingWizardState(step)
      }
    }
  }
</script>

