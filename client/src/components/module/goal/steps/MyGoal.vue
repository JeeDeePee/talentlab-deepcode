<template>
  <div class="grey--text">
    <h2>Was ist dein Ziel</h2>

    <v-container fluid grid-list-xl>
      Wähle das Ziel, das am besten zu dir passt.
    </v-container>

    <v-radio-group v-model="selected_goal" column>
      <v-radio v-for="goal in moduleGoals" :key="goal.id" :label="goal.text" :value="goal.level">{{goal.text}}</v-radio>
    </v-radio-group>

    <!--<div v-for="goal in moduleGoals" :key="goal.id">{{goal.text}}</div>-->
    <p></p>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn @click="$emit('proceed')">Ziel speichern</v-btn>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    name: 'my-goal',

    data() {
      return {
        selected_goal: null
      }
    },

    computed: {
      ...mapGetters({
        moduleGoals: 'getModuleGoals'
      })
    },

    created() {
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
