<template>
  <v-dialog v-model="show" fullscreen hide-overlay transition="dialog-bottom-transition" scrollable>
    <v-card tile>
      <div class="pa-2">
        <v-btn class="btn--close" large flat icon @click.stop="show=false">
          <v-icon>close</v-icon>
        </v-btn>

        <v-breadcrumbs>
          <v-icon slot="divider">chevron_right</v-icon>
          <v-breadcrumbs-item :disabled="true">
            Mein Ziel
          </v-breadcrumbs-item>
        </v-breadcrumbs>

        <MyGoal v-on:proceed="myGoalProceed($event)" v-on:back="myGoalBack($event)">
        </MyGoal>

      </div>
    </v-card>
  </v-dialog>
</template>

<script>
  import {mapActions} from 'vuex'

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
      MyGoal
    },

    data() {
      return {
      }
    },

    computed: {
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
      }),

      myGoalBack() {
        this.$emit('close')
        // don't save
      },

      myGoalProceed() {
        this.$emit('close')
        // save selected goal
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";
</style>
