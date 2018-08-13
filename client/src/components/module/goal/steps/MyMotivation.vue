<template>
  <div class="grey--text">
    <h2>Job-Context und Motivation</h2>

    <v-container fluid grid-list-xl>
      <p>
        Beschreibe deinen Job-Context und deine Motivation
      </p>

      <p>
        Schritt 1: Zunächst wird – zuhanden Besprechung mit dem Learning Advisor – eine kurze Beschreibung des Job-Context und der Motivation zur Buchung des Containers beim PARTICIPANT abgeholt.
      </p>

      <div v-for="goal in moduleGoals" :key="goal.id">{{goal.text}}</div>
    </v-container>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn @click="$emit('proceed')">Motivation speichern</v-btn>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: 'my-motivation',

    computed: {
      ...mapGetters({
        moduleGoals: 'getModuleGoals',
        isMyGoal: 'isMyGoal'
      })
    },

    created() {
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
