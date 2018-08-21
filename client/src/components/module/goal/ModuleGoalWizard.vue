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

        <MyGoal v-on:proceed="myGoalProceed($event)" v-on:back="myGoalBack($event)"></MyGoal>

      </div>
    </v-card>
  </v-dialog>
</template>

<script>
  import DEFINE_USER_GOAL from '@/graphql/gql/moduleGoals/defineUserGoal.gql'
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
      myGoalBack() {
        this.$emit('close')
      },

      myGoalProceed(goalLevel) {
        this.$emit('close')
        this.storeMyGoal(this.module.slug, goalLevel)
      },

      storeMyGoal(moduleSlug, goalLevel) {
        console.log(`storeMyGoal(moduleSlug: ${moduleSlug}, goalLevel: ${goalLevel})`)

        this.$apollo.mutate({
          mutation: DEFINE_USER_GOAL,
          variables: {
            moduleSlug: moduleSlug,
            goalLevel: goalLevel
          }
        }).then(data => {
          // console.log('Done storing goal.');
        });
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";
</style>
