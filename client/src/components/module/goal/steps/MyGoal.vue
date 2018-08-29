<template>
  <div class="grey--text">
    <h2>Was ist dein Ziel</h2>

    <v-container fluid grid-list-xl>
      Wähle das Ziel, das am besten zu dir passt.
    </v-container>

    <v-radio-group v-model="currentGoal" column>
      <v-radio v-for="goal in moduleGoals" :key="goal.id" :label="goal.text" :value="goal.level">{{goal.text}}</v-radio>
    </v-radio-group>

    <p></p>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', newSelectedGoal)">Ziel speichern</v-btn>
  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  export default {
    computed: {
      ...mapGetters({
        moduleGoals: 'getModuleGoals',
        getCurrentGoal: 'getCurrentGoal'
      }),
      currentGoal: {
        get() {
          return this.getCurrentGoal.level
        },
        set(value) {
          this.newSelectedGoal = value
        }
      }
    },

    data() {
      return {
        newSelectedGoal: -1
      }
    },

    methods: {
      ...mapActions({
        setCurrentGoal: 'setCurrentGoal'
      })
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
