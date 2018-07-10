<template>
  <v-card>
    <v-card-text>
      <span class="grey--text pr-4">Mastering Complexity – Vernetztes Denken</span>
      <span class="grey--text">22.11.2017 – 1.7.2018</span>

      <h3 class="my-2">Ziel 1: Unternehmensübergreifende Projekte zum Erfolg führen</h3>

      <v-container fluid grid-list-md>
        <v-layout row wrap>
          <v-flex xs12 sm4 pb-3>
            <h4>Selbsteinschätzung</h4>
            <v-progress-linear v-model="valueDeterminate"></v-progress-linear>
            <div class="grey--text">Stufe 7 von 10 erreicht</div>
          </v-flex>
          <v-flex xs12 sm4 pb-3>
            <h4>Action-Plan</h4>
            <v-progress-linear v-model="valueDeterminate"></v-progress-linear>
            <div class="grey--text">1 von 3 Actions erledigt</div>
          </v-flex>
          <v-flex xs12 sm4 pb-3>
            <h4>Lernmodule</h4>
            <v-progress-linear v-model="valueDeterminate"></v-progress-linear>
            <div class="grey--text">0 von 1 Lernmodulen erledigt</div>
          </v-flex>
        </v-layout>
      </v-container>

      <v-btn class="ml-0 mr-3">Selbsteinschätzung starten</v-btn>
      <v-btn class="ml-0">Feedback einholen</v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'goal',

    data() {
      return {
        valueDeterminate: 10
      }
    }
  }
</script>

<style scoped>
  .card {
    border-radius: 11px;
  }

  h3 {
    font-size: 20px;
  }
</style>
