<template>
  <v-card>
    <v-card-text>
      <div class="grey--text">Mastering Complexity – Vernetztes Denken</div>
      <v-btn>Details anzeigen</v-btn>
      <h3 class="heading">Partnering for Success</h3>
      <div>Erfolgreiche Führung von Partnerschaften</div>
      

      
    </v-card-text>
      <v-container fluid grid-list-xl class="pt-0 test">
        <v-layout row wrap>
          <v-flex xs12 sm6 class="pa-1">
            <h4 class="mb-1 mt-2">Nächste Schritte</h4>
            <ModuleStep v-for="(item, index) in steps" v-bind:key="index" class="mb-1"/>
          </v-flex>
          <v-flex xs12 sm6 class="pa-0">
            <img v-bind:src="'http://mountain.org/wp-content/uploads/Miraflores-Peru_TMI.jpg'">
          </v-flex>
        </v-layout>
      </v-container>

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
        steps: [1, 2]
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

  .container {
  background: #EBF6EA;
  }

  .heading {
    font-size: 44px;
    font-weight: bold;
  }

  h4 {
    font-size: 16pt;
    font-weight: bold;
    padding-bottom: 5px;
  }

  .test {
    padding: 0 12px;
  }

</style>
