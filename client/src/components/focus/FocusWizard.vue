<template>
  <Wizard v-model="show" :wizard-name="'Mein Fokus'" :process-steps="processSteps" @close="show=false">

    <DetermineFocus
      v-on:proceed="determineFocusProceed($event)"
      v-on:back="determineFocusBack($event)"
      v-if="isDetermineFocus">
    </DetermineFocus>
    <MyFocus
      v-on:proceed="myFocusProceed($event)"
      v-on:back="myFocusBack($event)"
      v-if="isMyFocus">
    </MyFocus>

  </Wizard>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import DetermineFocus from '@/components/focus/steps/DetermineFocus'
  import MyFocus from '@/components/focus/steps/MyFocus'
  import Wizard from '@/components/reusable/Wizard';

  export default {
    props: {
      visible: {
        required: true,
        type: Boolean
      }
    },

    components: {
      MyFocus,
      DetermineFocus,
      Wizard
    },

    data() {
      return {
        processSteps: [
          { text: 'Fokus erfasssen', disabled: false },
          { text: 'Mein Fokus', disabled: false }
        ]
      }
    },

    computed: {
      ...mapGetters({
        userFocusState: 'userFocusState',
        isMyFocus: 'isMyFocus',
        isDetermineFocus: 'isDetermineFocus'
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
        newFocusWizardState: 'newFocusWizardState',
        storeFocusCompetences: 'storeFocusCompetences',
        fetchFocusCompetences: 'fetchFocusCompetences'
      }),
      determineFocusBack() {
        this.newFocusWizardState('determine');
        this.$emit('close')
      },
      determineFocusProceed() {
        this.newFocusWizardState('my-focus')
      },
      myFocusProceed() {
        let self = this;
        this.storeFocusCompetences().then(function () {
          self.newFocusWizardState('determine');
          self.$emit('close')
        });
      },
      myFocusBack() {
        this.newFocusWizardState('determine')
      }
    },

    created() {
      this.fetchFocusCompetences()
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";
</style>
