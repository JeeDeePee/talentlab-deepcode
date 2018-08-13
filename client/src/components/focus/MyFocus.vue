<template>
  <v-card>
    <v-card-text>
      <div v-if="userFocus.length > 0">
        <v-container fluid grid-list-md>
          <v-layout row wrap>
            <v-flex xs12 sm4 pb-3 v-for="(item, index) in userFocus" :key="index">
              <h4>{{item.competence.title}}</h4>
              <v-progress-linear :value="item.currentLevel*10"></v-progress-linear>
              <div class="grey--text">Stufe {{item.currentLevel}} von 10 erreicht</div>
              <div class="grey--text">Nächste Beurteilung {{item.nextEvaluation}}</div>
            </v-flex>
          </v-layout>
        </v-container>
      </div>

      <v-btn class="hidden-sm-and-down float-r" @click.stop="showFocusDialog=true">
        <v-icon>add</v-icon>
        Mein Fokus
      </v-btn>

      <v-btn class="hidden-sm-and-down float-r" @click.stop="load()">
        <v-icon>add</v-icon>
        Get Fokus
      </v-btn>

      <FocusWizard :visible="showFocusDialog" @close="showFocusDialog=false"/>
    </v-card-text>
  </v-card>
</template>

<script>
  import FocusWizard from '@/components/focus/FocusWizard'
  import {mapGetters} from 'vuex'

  export default {
    name: 'my-focus',
    components: {
      FocusWizard
    },
    data() {
      return {
        showFocusDialog: false,
      }
    },
    computed: {
      ...mapGetters({
        userFocus: 'getUserFocus'
      })
    },
    created() {
      this.$store.dispatch('fetchUserFocus')
    },
    methods: {
      load: function () {
        this.$store.dispatch('fetchUserFocus')
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  .card {
    border-radius: 11px;
  }

  h3 {
    font-size: 20px;
  }
</style>
