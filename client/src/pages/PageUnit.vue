<template>
  <div class="learn-unit">
    <div class="wrapper">
      <v-breadcrumbs>
        <v-icon slot="divider">chevron_right</v-icon>
        <v-breadcrumbs-item :key="unit.categorySlug">
          <router-link class="link" :to="{name: 'categories'}" exact router>
            {{ unit.categoryTitle }}
          </router-link>
        </v-breadcrumbs-item>
        <v-breadcrumbs-item :key="unit.moduleSlug">
          <router-link class="link" :to="{name: 'module', params: {slug: unit.moduleSlug}}" exact router>
            {{ unit.moduleTitle }}
          </router-link>
        </v-breadcrumbs-item>
        <v-breadcrumbs-item :disabled="true" :key="unit.slug">
          {{ unit.title }}
        </v-breadcrumbs-item>
      </v-breadcrumbs>

      <h1 class="mt-4">{{unit.title}}</h1>
      <h2 class="pb-4 mt-3">{{unit.teaser}}</h2>
      <h2 class="pb-4 mt-3" v-html="unit.description"></h2>
      <v-btn class="mb-5 ml-0 mt-0">Lernmodul buchen</v-btn>

      <h3>Dieser Kurs gehört zum Lernmodul «{{unit.moduleTitle}}».</h3>
      <div class="grey--text floating position-top">
        <v-btn class="mb-4 ml-0 mr-3 mt-4">
          <v-icon class="pr-2">school</v-icon>Kurs
        </v-btn>
<<<<<<< HEAD
        <v-icon class="ml-3">event_note</v-icon> {{unit.count}}
        <v-icon class="ml-3">schedule</v-icon> {{unit.duration}}
        <v-icon class="ml-3">attach_money</v-icon> {{unit.price}}

        <!--<v-btn class="mb-4 mt-0 " :to="{ name: 'fokus'}" exact router>-->
        <!--<v-icon class="pr-2">share</v-icon>Share-->
        <!--</v-btn>-->
=======
        <div class="grey--text floating position-top">
          <v-icon class="ml-3">event_note</v-icon> {{unit.count}}
          <v-icon class="ml-3"> schedule</v-icon> {{unit.duration}}
               
          <v-btn class="mb-4 mt-0 " :to="{ name: 'fokus'}" exact router>
            <v-icon class="pr-2">share</v-icon>
            Share
          </v-btn> 
        </div>

          <v-expansion-panel focusable>
            <v-expansion-panel-content
              v-for="(item,i) in 5"
              :key="i"
            >
              <div slot="header">Details anzeigen</div>
              <v-card>
                <v-card-text class="grey lighten-3">
                  
                  Inhalte
                  Das gesamte Programm ist interaktiv gestaltet und legt großen Wert auf sofortige praktische Anwendbarkeit. Anhand interessanter Fallstudien aus dem Geschäftsalltag werden Methoden trainiert und besprochen. Sie erlernen und erproben Taktiken, um auch dann die Oberhand zu behalten, wenn Risiken und Unsicherheiten auftauchen. Darüber hinaus wird Ihnen mithilfe verschiedener Methoden vermittelt, wie Sie die Persönlichkeitstypen ihrer Verhandlungspartner erkennen und Ihre verbale und nonverbale Kommunikation effektiv einsetzen können.
Besonders im Fokus stehen Lösungsansätze für schwierige Verhandlungssituationen, wenn z. B. Verhandlungspartner ablehnend reagieren, mit harten Bandagen verhandelt wird oder die Lage extrem angespannt ist. Durch Rollenspiele und praktische Übungen können Sie die erlernten Methoden sofort umsetzen und trainieren und gewinnen damit Vertrauen in Ihre Verhandlungsstärke.</v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>

>>>>>>> added expansion panel for learnunit detail page
      </div>
    </div>
  </div>
</template>

<script>
  import UNIT_QUERY from '@/graphql/gql/unit.gql'

  export default {
    name: 'page-unit',

    props: {
      slug: {
        required: true,
        type: String
      }
    },

    components: {},

    data() {
      return {
        unit: {
          moduleTitle: ''
        }
      }
    },

    methods: {},

    apollo: {
      unit: {
        query: UNIT_QUERY,
        variables() {
          return {
            slug: this.slug
          }
        },
        manual: true,
        result(data, loading, networkStatus) {
          if (!loading) {
            this.unit = data.data.unit.edges[0].node
          }
        }
      }
    },

    created() {
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  .link {
    color: $text-color;
  }

  .learn-unit {
    background-color: $learn-unit-bg-color;
  }

  .wrapper {
    max-width: 1100px;
    margin-left: auto;
    margin-right: auto;
    content: "";
    clear: both;
    display: table;
  }

  .wrapper:after {
    content: "";
    clear: both;
    display: table;
  }

  h1 {
    font-size: 44px
  }

  h2 {
    font-size: 18px;
  }

  h3 {
    font-size: 15px;
  }

  .floating {
    float: left;
  }

  .position-top {
    margin-top: 12px;
  }
</style>
