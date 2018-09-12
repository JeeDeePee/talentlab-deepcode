<template>
  <div class="text-xs-center">
    <h1>Was ist dein Ziel</h1>

    <v-container fluid grid-list-xl>
      Wähle das Ziel, das am besten zu dir passt.
    </v-container>

    <v-radio-group v-model="currentGoal.level" column>
      <v-radio v-for="goal in moduleGoals" :key="goal.id" :label="goal.text" :value="goal.level">{{goal.text}}</v-radio>
    </v-radio-group>

    <p></p>

    <v-btn class="btn-secondary" @click="$emit('back')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', currentGoal.level)">Ziel speichern</v-btn>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'
  import Vue from 'vue'

  export default {
    props: {
      goal: {
        required: true,
        type: Object
      }
    },

    data() {
      return {
        currentGoal: this.goal
      }
    },

    computed: {
      ...mapGetters({
        moduleGoals: 'getModuleGoals'
      })
    },

    watch: {
      goal() {
        this.currentGoal = Vue.util.extend({}, this.goal)
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
