<template>
  <v-card>
    <div v-if="userFocus.length > 0">
      <v-card-text>
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
      </v-card-text>
      <v-card-actions>
        <div v-if="userFocusCreated">
          {{userFocusCreated|formatDate}}
        </div>
        <v-btn class="float-r" @click.stop="showFocusDialog=true">
          <v-icon>add</v-icon>
          Neuen Fokus erstellen
        </v-btn>
      </v-card-actions>
    </div>
    <div v-else>
      <v-btn class="float-r" @click.stop="showFocusDialog=true">
        <v-icon>add</v-icon>
        Mein Fokus
      </v-btn>
    </div>
    <FocusWizard :visible="showFocusDialog" @close="showFocusDialog=false"/>
  </v-card>
</template>

<script>
  import FocusWizard from '@/components/focus/FocusWizard'
  import {mapGetters} from 'vuex'

  export default {
    components: {
      FocusWizard
    },

    data() {
      return {
        showFocusDialog: false
      }
    },

    computed: {
      ...mapGetters({
        userFocus: 'getUserFocus',
        userFocusCreated: 'getUserFocusCreated'
      })
    },

    created() {
      this.$store.dispatch('fetchUserFocus')
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  .v-card__text {
    padding: 0;
  }

</style>
