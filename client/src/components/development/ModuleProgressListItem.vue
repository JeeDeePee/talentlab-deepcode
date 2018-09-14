<template>
  <v-card>
    <v-card-text class="text">
      <div class="grey--text mb-2">{{ moduleProgress.category.title }} – {{ moduleProgress.skill }}</div>
      <div class="grid-container">
        <h3 class="heading item1">{{ moduleProgress.title }}</h3>
        <v-btn :to="{name: 'module', params: {slug: moduleProgress.slug}}" class="button item2 hidden-sm-and-down">
          Details anzeigen
        </v-btn>
      </div>
      <div class="pb-3 mt-3">{{ moduleProgress.teaser }}</div>
      <v-btn :to="{name: 'module', params: {slug: moduleProgress.slug}}"
             class="button_xs mb-3 hidden-md-and-up btn-left">Details anzeigen
      </v-btn>
    </v-card-text>

    <v-container fluid grid-list-xl class="pt-0 test">
      <v-layout row wrap>
        <v-flex xs12 sm6 class="pa-3">
          <h4 class="mb-1 mt-2">Nächste Schritte</h4>
          <ModuleNextStep v-for="(unitProgress, index) in nextSteps" :unitProgress="unitProgress" :key="index"
                          class="mb-1"/>
        </v-flex>
        <v-flex xs12 sm6 class="pa-0">
          <img :src="moduleProgress.heroImage"><br>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
</template>

<script>
  import ModuleNextStep from '@/components/development/ModuleNextStep'

  export default {
    props: {
      moduleProgress: {
        required: true,
        type: Object
      }
    },

    components: {
      ModuleNextStep
    },

    computed: {
      nextSteps() {
        const unitProgress = this.moduleProgress.units.edges.map(entry => entry.node)
        return unitProgress
      }
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

  .grid-container {
    display: grid;
  }

  .item1 {
    grid-column: 1 / span 9;
  }

  .item2 {
    grid-column: 10 / span 12;
  }

  .button {
    float: right;
    margin-top: 14px;
  }

  .button-xs {
    margin-left: 0 !important;
  }

  .btn-left {
    margin-left: 0;
  }

  img {
    max-width: 100%;
    float: left;
  }

  .container {
    background: #EBF6EA;
  }

  .heading {
    font-size: 44px;
    font-weight: bold;
  }

  h3 {
    line-height: 1.15;
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
