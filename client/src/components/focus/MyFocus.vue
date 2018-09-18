<template>
  <div>
    <div v-if="userFocus.length > 0">

      <div v-for="(item, index) in userFocus" :key="index" class="mb-4">
        <h4>{{item.competence.title}}</h4>
        <v-progress-linear :value="item.currentLevel*10" color="secondary"></v-progress-linear>
        <div class="grey--text">Stufe {{item.currentLevel}} von 10 erreicht</div>
        <div class="grey--text">Nächste Beurteilung {{item.nextEvaluation}}</div>
      </div>

      <div v-if="userFocusCreated">
        {{userFocusCreated|formatDate}}
      </div>
      <v-btn @click.stop="showFocusDialog=true" class="mt-4">
        Neuen Fokus erstellen
      </v-btn>

    </div>
    <div v-else>
      <v-btn @click.stop="showFocusDialog=true">
        Mein Fokus
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
        showFocusDialog: false
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
</style>
