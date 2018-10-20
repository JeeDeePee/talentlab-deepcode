<template>
  <div>
    <div v-if="userFocus.length > 0">

      <v-layout row wrap class="text-xs-center">
        <v-flex v-for="(item, index) in userFocus" :key="index" xs12 sm4>
          <h4>{{item.competence.title}}</h4>

          <div class="px-2">
            <div class="focus--background mt-5">
              <div class="focus--self bold" :style="{ left: item.currentLevel*10 + '%' }">
                {{item.currentLevel}}
              </div>
              <div class="focus--peer bold" :style="{ left: item.currenPeerLevel*10 + '%' }">
                {{item.currenPeerLevel}}
              </div>
              <div class="focus--benchmark bold"
                   :style="{ left: item.currenPeerLevel*10 + '%', width: item.benchmarkWidth*10 + '%'}"></div>
            </div>
          </div>

        </v-flex>
      </v-layout>

      <div class="mt-4">
        <div class="focus--legend background--violet mr-2"></div>
        Selbsteinschätzung
      </div>
      <div>
        <div class="focus--legend background--orange mr-2"></div>
        Peerbewertung
      </div>
      <div>
        <div class="focus--legend background--orange-50 mr-2"></div>
        Benchmark
      </div>

      <v-btn @click.stop="showFocusDialog=true" flat class="mt-4 ml-0 pl-0">
        <v-icon left dark>add</v-icon>
        Neuen Fokus setzen
      </v-btn>


    </div>
    <div v-else>
      <v-btn flat @click.stop="showFocusDialog=true" class="ml-0 pl-0">
        <v-icon dark class="mr-0">add</v-icon>
        Mein Fokus setzen
      </v-btn>
    </div>
    <FocusWizard :visible="showFocusDialog" @close="showFocusDialog=false"/>
  </div>
</template>

<script>
  import FocusWizard from '@/components/focus/FocusWizard'
  import {mapActions, mapGetters} from 'vuex'

  export default {
    components: {
      FocusWizard
    },

    data() {
      return {
        showFocusDialog: this.$lodash.isEmpty(this.$route.params) ? false : this.$route.params.showFocusDialog
      }
    },

    computed: {
      ...mapGetters({
        userFocus: 'getUserFocus',
        userFocusCreated: 'getUserFocusCreated'
      })
    },

    methods: {
      ...mapActions({
        fetchUserFocus: 'fetchUserFocus'
      })
    },

    created() {
      this.fetchUserFocus()
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  $focus--value-size: 25px;

  .focus--background {
    width: 100%;
    height: 10px;
    background-color: white;
  }

  .focus--self {
    float: left;
    width: $focus--value-size;
    padding: 4px;
    background-color: $violet;
    color: white;
    position: relative;
    top: -10px;
    margin-left: $focus--value-size *-1;
    z-index: 10;
  }

  .focus--peer {
    float: left;
    width: $focus--value-size;
    padding: 4px;
    background-color: $orange;
    position: relative;
    top: -10px;
    margin-left: $focus--value-size *-1;
    z-index: 5;
  }

  .focus--benchmark {
    height: 10px;
    background-color: rgba($orange, 0.5);
    position: relative;
    z-index: 1;
  }

  .focus--legend {
    height: 10px;
    width: 100px;
    display: inline-block;
  }

</style>
