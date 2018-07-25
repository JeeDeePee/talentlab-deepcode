<template>
  <v-dialog
    v-model="show"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    scrollable
  >
    <v-card tile>
      <div class="pa-2">
        <v-btn class="btn--close" large flat icon @click.stop="show=false">
          <v-icon>close</v-icon>
        </v-btn>

        <v-breadcrumbs divider="/">
          <v-breadcrumbs-item
            :disabled="isDetermineFocus"
          >
            Fokus erfasssen
          </v-breadcrumbs-item>
          <v-breadcrumbs-item
            :disabled="isMyFocus"
          >
            Mein Foukus
          </v-breadcrumbs-item>

        </v-breadcrumbs>

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

      </div>
    </v-card>
  </v-dialog>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import DetermineFocus from '@/components/focus/DetermineFocus'
  import MyFocus from '@/components/focus/MyFocus'

  export default {
    name: 'focus-wizard',
    props: ['visible'],

    components: {
      MyFocus,
      DetermineFocus
    },

    data() {
      return {
        module: null
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
        newFocusWizardState: 'newFocusWizardState'
      }),

      determineFocusBack() {
        this.newFocusWizardState('determine')
        this.$emit('close')
      },

      determineFocusProceed() {
        this.newFocusWizardState('my-focus')
      },

      myFocusProceed() {
        this.newFocusWizardState('determine')
        this.$emit('close')
      },

      myFocusBack() {
        this.newFocusWizardState('determine')
      }

    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  .card {
    background-color: $grey-9;
  }
</style>
