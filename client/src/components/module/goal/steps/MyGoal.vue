<template>
  <div class="text-xs-center">
    <h1 class="text-xs-center text--violet">Was ist Dein Ziel?</h1>

    <div class="mt-4 mb-5 lead">
      Wähle das Ziel, das am besten zu Dir passt.
    </div>

    <v-radio-group v-model="currentGoal.level" hide-details>
      <v-layout row wrap>
        <v-flex xs12 sm4 v-for="goal in moduleGoals" :key="goal.id">
          <div class="background--white pa-4 mygoal--selection v-align--center">
            <v-radio :label="goal.text" :value="goal.level">
              {{goal.text}}
            </v-radio>
          </div>
        </v-flex>
      </v-layout>
    </v-radio-group>

    <div class="mt-5">
      <v-btn class="btn-secondary mr-2" @click="$emit('back')">zurück</v-btn>
      <v-btn class="ml-2" @click="$emit('proceed', currentGoal.level)">speichern</v-btn>
    </div>
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

  .mygoal--selection {
    height: 100%;
  }

</style>
