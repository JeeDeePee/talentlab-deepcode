<template>
  <div class="text-xs-center">
    <h1>Reflektiere was Du gelernt hast</h1>
    <p>Das sind Deine Learnings aus den verschiedenen Units. Passe bei Bedarf noch einmal an.</p>

    <TextBox :placeholder="'Deine Learnings'" v-model="actionPlan.learningsText"></TextBox>

    <v-btn class="btn-secondary" @click="$emit('back', 'ReviseGoals')">Zurück</v-btn>
    <v-btn @click="save">Weiter</v-btn>
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
