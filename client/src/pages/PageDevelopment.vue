<template>
  <v-container class="mt-3">
    <h2 class="grey--text mb-3">Meine Ziele</h2>
    <Goal class="mb-4"/>

    <div class="clearfix">
        <v-btn class="hidden-sm-and-down float-r">
          <v-icon>add</v-icon>
          Lernmodule auswählen
        </v-btn>

      <h2 class="grey--text mb-3">Meine Lernmodule</h2>

          <v-btn class="mb-4 ml-0 mt-0 hidden-md-and-up">
            <v-icon>add</v-icon>
            Lernmodule auswählen
          </v-btn>
  
    </div>


    <Module v-for="(item, index) in modules" v-bind:key="index" class="mb-4"/>

    <h3 class="title-recomendations pt-3">Vorgeschlagene Lernmodule</h3>
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
    name: 'page-development',
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
    font-size: 24px;
    font-weight: 400;
  }

  h3 {
    font-size: 24px;
    margin-bottom: 12px;
  }

  .title-recomendations {
    font-size: 15px;
    font-weight: 400;
    text-transform: uppercase;
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

 .clearfix::after {
  content: "";
  clear: both;
  display: table;
}

.float-l {
  float: left;
}

.float-r {
  float: right;
  margin-top: -5px;
}


</style>
