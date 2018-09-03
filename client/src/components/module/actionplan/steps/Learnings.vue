<template>
  <div class="text-xs-center">
    <h1>Reflektiere was Du gelernt hast</h1>
    <p>Das sind Deine Learnings aus den verschiedenen Units. Passe bei Bedarf noch einmal an.</p>

    <TextBox v-model="actionPlan.learnings"></TextBox>

    <v-btn class="btn-secondary" @click="$emit('back', 'ReviseGoals')">Zurück</v-btn>
    <v-btn @click="save">Weiter</v-btn>
  </div>
</template>

<script>

  import {mapGetters} from 'vuex'
  import TextBox from '@/components/reusable/TextBox'

  export default {
    props: ['breadcrumbs'],

    components: {
      TextBox
    },

    computed: {
      ...mapGetters({
        actionPlan: 'getActionPlan'
      })
    },

    data() {
      return {
      }
    },

    methods: {
      save() {
        console.log(this.actionPlan.learnings)
        this.$emit('proceed', 'ActionPlanBusinessGoal')
      }
    },

    created() {
      // this.breadcrumbs[2].disabled = true
      // console.log(this.$options._componentTag)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
