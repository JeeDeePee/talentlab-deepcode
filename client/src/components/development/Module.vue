<template>
  <v-card>
    <v-card-text>
      <div class="grey--text">Mastering Complexity – Vernetztes Denken</div>
      <h3>Partnering for Success</h3>
      <div>Erfolgreiche Führung von Partnerschaften</div>
      <v-btn>Details anzeigen</v-btn>

      <h4 class="mb-1 mt-2">Nächste Schritte</h4>

      <v-container fluid grid-list-md>
        <v-layout row wrap>
          <v-flex xs12 sm6 class="mb-1">
            <ModuleStep v-for="(item, index) in steps" v-bind:key="index" class="mb-1"/>
          </v-flex>
          <v-flex xs12 sm6 class="mb-1">
            <img v-bind:src="'http://mountain.org/wp-content/uploads/Miraflores-Peru_TMI.jpg'">
          </v-flex>
        </v-layout>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
  import ModuleStep from '@/components/development/ModuleStep'

  export default {
    name: 'ModuleSteps',
    components: {
      ModuleStep
    },
    data() {
      return {
        steps: [1, 2, 3]
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  img {
    max-width: 100%;
  }

  .card {
    border-radius: 11px;
  }

</style>
