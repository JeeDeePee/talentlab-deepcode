<template>
  <v-container class="learn-unit">
  <div>
    <div>
      <v-breadcrumbs class="pl-0 mt-2">
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
      <h2 class="pb-4 mt-3" v-html="unit.description"></h2>
      <v-btn class="mb-5 ml-0 mt-0">Lernmodul buchen</v-btn>

      <h3>Dieser Kurs gehört zum Lernmodul «{{unit.moduleTitle}}».</h3>

        <div class="grey--text float-l position-top">
          <v-btn class="btn--dark mb-4 ml-0 mr-3 mt-4">
            <v-icon class="pr-2 beige--text">school</v-icon> <p class="beige--text mb-0">Kurs</p>
          </v-btn>

            <v-icon class="ml-3">event_note</v-icon> {{unit.count}}
            <v-icon class="ml-3"> schedule</v-icon> {{unit.duration}}

            <v-btn class="mb-4 ml-3 mr-3 mt-4" :to="{ name: 'fokus'}" exact router>
              <v-icon class="pr-2">share</v-icon>
              Share
            </v-btn>
        </div>

        <div class="panel-style mt-5 mb-5 pl-0">
          <v-expansion-panel focusable>
            <v-expansion-panel-content>
              <div slot="header">Details</div>
              <v-card>
                <v-card-text class="pl-0">
                <h2>Lernziele & Kompetenzen</h2>
                <ul>
                  <li>Die richtige Einstellung und das nötige Handwerkszeug zur effektiven Verhandlungsführung</li>
                  <li>Strategien und Methoden, um optimale Verhandlungsergebnisse zu erzielen</li>
                  <li>Die Fähigkeit, auch dann Geschäfte abzuschließen, wenn die Verhandlungspartner weiterhin unterschiedliche Standpunkte vertreten</li>
                  <li>Die Fähigkeit, taktische und psychologische Verhandlungsfallen zu erkennen und zu vermeiden</li>
                  <li>Selbstvertrauen beim Umgang mit komplexen und aufreibenden Situationen</li>
                  <li>Gekonnter Umgang mit Kräfteungleichgewichten und schwierigen Persönlichkeiten</li>
                  <li>Verbesserte Fähigkeiten in puncto Einflussnahme, Werteinforderung und Einschätzung des Verhandlungspartners</li>
                  <li>Stärkere Führungsqualitäten durch Schulung des Verhandlungsgeschicks</li>
                </ul>	

                <h2>Inhalte</h2>
                  Das gesamte Programm ist interaktiv gestaltet und legt großen Wert auf sofortige praktische Anwendbarkeit. Anhand interessanter Fallstudien aus dem Geschäftsalltag werden Methoden trainiert und besprochen. Sie erlernen und erproben Taktiken, um auch dann die Oberhand zu behalten, wenn Risiken und Unsicherheiten auftauchen. Darüber hinaus wird Ihnen mithilfe verschiedener Methoden vermittelt, wie Sie die Persönlichkeitstypen ihrer Verhandlungspartner erkennen und Ihre verbale und nonverbale Kommunikation effektiv einsetzen können.
Besonders im Fokus stehen Lösungsansätze für schwierige Verhandlungssituationen, wenn z. B. Verhandlungspartner ablehnend reagieren, mit harten Bandagen verhandelt wird oder die Lage extrem angespannt ist. Durch Rollenspiele und praktische Übungen können Sie die erlernten Methoden sofort umsetzen und trainieren und gewinnen damit Vertrauen in Ihre Verhandlungsstärke.</v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </div>
        
      </div>
    </div>
  </v-container>
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

  .application.theme--light {
    background-color: $beige !important;
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

  .position-top {
    margin-top: 12px;
  }

  .beige--text {
    color: $beige !important;
  }

  .theme--light .v-expansion-panel .v-expansion-panel__container {
    color: $orange;
  }

  .theme--light .v-expansion-panel .v-expansion-panel__container .v-expansion-panel__header .v-expansion-panel__header__icon .v-icon{
    color: $orange !important;
  }

  .panel-style {
    border-top: $orange 1px solid;
  }

  .v-expansion-panel {
    box-shadow: none !important;
    background-color: $beige !important;
  }

  .v-expansion-panel__container {
    box-shadow: none !important;
    background-color: $beige !important;
  }

  .theme--light .v-card {
    background-color: $beige;
  }

  .theme--light .v-btn.btn--dark {
    background-color: $grey-9;
    border: none;
  }
</style>
