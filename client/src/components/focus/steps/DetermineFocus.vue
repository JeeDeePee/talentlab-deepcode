<template>
  <div class="text-xs-center">
    <h1>Wo willst du in deiner Entwicklung den Fokus setzen</h1>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex xs4 v-for="(category, categoryKey) in focusCompetences" :key="categoryKey">
          <component :is="category.iconComponent"/>
          <h3>{{category.title}}</h3>

          <p>{{category.teaser}}</p>

          <v-checkbox
            v-for="(competence, competenceKey) in category.competences" :key="competenceKey"
            v-model="selectedFocus"
            :label="competence.title"
            :value="competence.slug">
          </v-checkbox>

        </v-flex>
      </v-layout>
    </v-container>

    <v-btn class="btn-secondary" @click="$emit('back')">Zurück</v-btn>
    <v-btn @click="$emit('proceed')">Weiter</v-btn>
  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import GrowingAsALeader from '@/assets/img/Growing-as-a-Leader.svg'
  import MasteringComplexity from '@/assets/img/Mastering-Complexity.svg'
  import MasteringRelations from '@/assets/img/Mastering-Relations.svg'

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
