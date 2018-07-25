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
        <v-btn class="dialog__close" large flat icon @click.stop="show=false">
          <v-icon>close</v-icon>
        </v-btn>

        <FocusStart v-on:proceed="proceedAfterStart($event)" v-if="isFocusStart"></FocusStart>
        <FocusDetail v-on:proceed="proceedAfterDetail($event)" v-if="isFocusDetail"></FocusDetail>
        <FocusFinish v-on:proceed="proceedAfterFinish($event)" v-if="isFocusFinish"></FocusFinish>

      </div>
    </v-card>
  </v-dialog>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import FocusStart from '@/components/focus/FocusStart'
  import FocusDetail from '@/components/focus/FocusDetail'
  import FocusFinish from '@/components/focus/FocusFinish'

  export default {
    name: 'focus-wizard',
    props: ['visible'],

    components: {
      FocusDetail,
      FocusStart,
      FocusFinish
    },

    data() {
      return {
        module: null,
        moduleBooked: false
      }
    },

    computed: {
      ...mapGetters({
        userFocusState: 'userFocusState',
        isFocusStart: 'isFocusStart',
        isFocusDetail: 'isFocusDetail',
        isFocusFinish: 'isFocusFinish'
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

      proceedAfterStart() {
        this.newFocusWizardState('detail')
      },

      proceedAfterDetail() {
        this.newFocusWizardState('finish')
      },

      proceedAfterFinish() {
        this.newFocusWizardState('start')
        this.$router.push('development')
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
