<template>
  <div class="grey--text">

    <h2>Wo willst du in deiner Entwicklung den Fokus setzen</h2>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex xs4 v-for="(category, categoryKey) in items" :key="categoryKey">
          <img :src="'https://talentlab-web.s3.amazonaws.com/original_images/category2_Al9ARbs.png'"><br>
          <h3 class="text-center">{{category.title}}</h3>

          <p>{{category.teaser}}</p>

          <v-checkbox
            v-for="(competence, competenceKey) in category.competences" :key="competenceKey"
            v-model="selectedFocus"
            v-bind:label="competence.title"
            v-bind:value="competence.slug"
          ></v-checkbox>

        </v-flex>
      </v-layout>
    </v-container>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn v-on:click="proceed">Weiter</v-btn>
  </div>
</template>

<script>
  import {mapActions} from 'vuex'
  import FOCUS_COMPETENCE_QUERY from '@/graphql/gql/focus/focusCompetences.gql'

  export default {
    name: 'determine-focus',
    methods: {
      ...mapActions({
        setFocus: 'setFocus'
      }),
      proceed: function (event) {
        this.$emit('proceed')
      }
    },

    created () {
      this.$store.dispatch('fetchFocusCompetences')
    },

    apollo: {
      categories: {
        query: FOCUS_COMPETENCE_QUERY,
        fetchPolicy: 'network-only'
      }
    },
    computed: {
      items: function () {
        if (this.categories) {
          return this.categories.edges.map(category => ({
              title: category.node.title,
              teaser: 'Gewinne Leichtigkeit im Umgang mit Veränderungen',
              competences: category.node.competenceSet.edges.map(compentence => ({
                    title: compentence.node.title,
                    slug: compentence.node.slug
                  }
                )
              )
            })
          )
        }
        return []
      },
      selectedFocus: {
        set(focus) {
          this.setFocus(focus)
        },
        get() {
          return this.$store.getters.getFocus
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";
</style>
