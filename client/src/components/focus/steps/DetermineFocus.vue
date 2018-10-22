<template>
  <div class="text-xs-center">
    <h1 class="text--violet text--violet">Welche Kompetenzen stehen bei deiner Entwicklung im Fokus?</h1>

    <div class="mt-4 mb-5 lead">Wähle maximal 3 Kompetenzen</div>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex xs12 sm12 md4 v-for="(category, categoryKey) in focusCompetences" :key="categoryKey">
          <component :is="category.iconComponent"/>
          <h2 class="text--violet">{{category.title}}</h2>
          <div class="mt-4 mb-1 three-line">{{category.teaser}}</div>

          <v-checkbox
            class="background--white pa-2"
            v-for="(competence, competenceKey) in category.competences" :key="competenceKey"
            v-model="selectedFocus"
            hide-details
            :label="competence.title"
            :value="competence.slug">
          </v-checkbox>

        </v-flex>
      </v-layout>
    </v-container>

    <div class="mt-5">
      <v-btn class="btn-secondary mr-2" @click="$emit('back')">Zurück</v-btn>
      <v-btn class="ml-2" @click="$emit('proceed')">Weiter</v-btn>
    </div>
  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import GrowingAsALeader from '@/assets/img/icons/growing-as-a-leader-grey.svg'
  import MasteringComplexity from '@/assets/img/icons/mastering-complexity-grey.svg'
  import MasteringRelations from '@/assets/img/icons/mastering-relations-grey.svg'


  export default {
    components: {
      GrowingAsALeader,
      MasteringComplexity,
      MasteringRelations
    },

    methods: {
      ...mapActions({
        newUserFocusBySlugs: 'newUserFocusBySlugs'
      })
    },

    computed: {
      ...mapGetters({
          'userFocusSlugs': 'getUserFocusCacheSlugs',
          'focusCompetences': 'getFocusCompetences'
        }
      ),
      selectedFocus: {
        set(focus) {
          this.newUserFocusBySlugs(focus)
        },
        get() {
          return this.userFocusSlugs
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";
</style>
