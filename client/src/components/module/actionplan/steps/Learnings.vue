<template>
  <div class="text-xs-center small--content">
    <h1>Deine Learnings</h1>
    <div class="mt-4 mb-5">Während der Bearbeitung des Moduls hast Du laufend Deine Learnings erfasst. Ergänze falls nötig.</div>

    <TextBox :placeholder="'Deine Learnings'" v-model="actionPlan.learningsText"></TextBox>

    <div class="mt-5">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'ReviseGoals')">Zurück</v-btn>
      <v-btn @click="save" class="ml-2">Weiter</v-btn>
    </div>
  </div>
</template>

<script>

  import {mapActions, mapGetters} from 'vuex'
  import TextBox from '@/components/reusable/TextBox'

  export default {
    components: {
      TextBox
    },

    computed: {
      ...mapGetters({
        actionPlan: 'getActionPlan'
      })
    },

    methods: {
      ...mapActions({
        defineActionPlan: 'defineActionPlan'
      }),
      save() {
        this.defineActionPlan([{'learningsText': this.actionPlan.learningsText}])
        this.$emit('proceed', 'ActionPlanBusinessGoal')
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
