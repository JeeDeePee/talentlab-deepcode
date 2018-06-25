<template>
  <v-container class="mt-3">
    <h2 class="grey--text">Meine Ziele</h2>
    <Goal class="mb-4"/>

    <h2 class="grey--text">Meine Lernmodule</h2>
    <v-btn>
      <v-icon>star</v-icon>
      Lernmodule auswählen
    </v-btn>

    <Module v-for="(item, index) in modules" v-bind:key="index" class="mb-4"/>

    <h3 class="grey--text">Vorgeschlagene Lernmodule</h3>
    <v-container fluid grid-list-md>
      <v-layout row wrap>
        <v-flex v-for="(item, index) in recomendations" v-bind:key="index" xs12 sm6 class="mb-1">
          <Recomendation/>
        </v-flex>
      </v-layout>
    </v-container>

  </v-container>
</template>

<script>
  import Goal from '@/components/development/Goal'
  import Module from '@/components/development/Module'
  import Recomendation from '@/components/development/Recomendation'

  export default {
    name: 'page-container',
    components: {
      Goal,
      Module,
      Recomendation
    },
    data() {
      return {
        modules: [1, 2],
        recomendations: [1, 2]
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  img {
    max-width: 100%;
  }

  h2 {
    font-size: 44px;
  }

  h3 {
    font-size: 24px;
    margin-bottom: 12px;
  }

  .video-thumbnail {
    max-width: 200px;
  }

  .hero-bg {
    background-color: $blue;
  }

  .description {
    font-size: 18px;
    font-weight: bold;
  }

</style>
