<template>
  <Wizard v-model="show" :wizard-name="'Mein Ziel'" :process-steps="processSteps" @close="show=false">

    <MyGoal :goal="currentGoal" v-on:proceed="myGoalProceed" v-on:back="myGoalBack"></MyGoal>

  </Wizard>
</template>

<script>
  import DEFINE_USER_GOAL from '@/graphql/gql/moduleGoals/defineUserGoal.gql'

  import {mapActions, mapGetters} from 'vuex'

  import Wizard from '@/components/reusable/Wizard'
  import MyGoal from '@/components/module/goal/steps/MyGoal'

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
      MyGoal,
      Wizard
    },

    data() {
      return {
        processSteps: [
          { text: 'Meine Ziele', disabled: false }
        ]
      }
    },

    computed: {
      ...mapGetters({
        currentGoal: 'getCurrentGoal'
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
        fetchModuleGoals: 'fetchModuleGoals'
      }),

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
    },

    created() {
      this.fetchModuleGoals({ moduleSlug: this.module.slug })
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";
</style>
