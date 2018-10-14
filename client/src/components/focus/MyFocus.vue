<template>
  <div class="text-xs-center">
    <div v-if="userFocus.length > 0">

      <v-layout row wrap>
        <v-flex v-for="(item, index) in userFocus" :key="index" xs12 sm4>

          <h4>{{item.competence.title}}</h4>

          <v-progress-linear :value="item.currentLevel*10" color="secondary"></v-progress-linear>


        </v-flex>
      </v-layout>

      <v-btn @click.stop="showFocusDialog=true" class="mt-4">
        Neuen Fokus setzen
      </v-btn>

    </div>
    <div v-else>
      <v-btn @click.stop="showFocusDialog=true">
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
</style>
