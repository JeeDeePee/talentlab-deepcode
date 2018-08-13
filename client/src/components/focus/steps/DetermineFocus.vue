<template>
  <div class="grey--text">

    <h2>Wo willst du in deiner Entwicklung den Fokus setzen</h2>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex xs4 v-for="(category, categoryKey) in focusCompetences" :key="categoryKey">
          <img :src="'https://talentlab-web.s3.amazonaws.com/original_images/category2_Al9ARbs.png'"><br>
          <h3>{{category.title}}</h3>

          <p>{{category.teaser}}</p>

          <v-checkbox
            v-for="(competence, competenceKey) in category.competences" :key="competenceKey"
            v-model="selectedFocus"
            v-bind:label="competence.title"
            v-bind:value="competence.slug">
          </v-checkbox>

        </v-flex>
      </v-layout>
    </v-container>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn v-on:click="proceed">Weiter</v-btn>
  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  export default {
    name: 'determine-focus',

    methods: {
      ...mapActions({
        newUserFocusBySlugs: 'newUserFocusBySlugs'
      }),
      proceed: function (event) {
        this.$emit('proceed')
      }
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
