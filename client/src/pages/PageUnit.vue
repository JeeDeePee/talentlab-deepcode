<template>
  <div class="background--mint-opacity">
    <v-container>
      <div v-if="unit">
        <div>
          <v-breadcrumbs class="pl-0">
            <v-icon slot="divider">chevron_right</v-icon>
            <v-breadcrumbs-item class="link" :to="{name: 'modules'}" exact router>
              {{ unit.categoryTitle }}
            </v-breadcrumbs-item>
            <v-breadcrumbs-item class="link" v-if="unit.moduleSlug"
                                :to="{name: 'module', params: {slug: unit.moduleSlug}}" exact router>
              {{ unit.moduleTitle }}
            </v-breadcrumbs-item>
            <v-breadcrumbs-item :disabled="true">
              {{ unit.title }}
            </v-breadcrumbs-item>
          </v-breadcrumbs>

          <h1 class="mt-4">{{unit.title}}</h1>

          <v-layout row wrap>
            <v-flex xs12 sm8>
              <div class="pb-4 mt-3" v-html="unit.description"></div>

              <div>
                <v-icon>play_arrow</v-icon>
                {{unit.type}}
                <v-icon class="ml-3">event_note</v-icon>
                {{unit.count}}
                <v-icon class="ml-3"> schedule</v-icon>
                {{unit.duration}}
              </div>

            </v-flex>
            <v-flex xs12 sm4 class="text-xs-center">

              <v-avatar size=115 class="v-avatar--responsive">
                <v-img
                  :src="'https://cdn.vuetifyjs.com/images/lists/3.jpg'"
                  :alt="avatar"
                ></v-img>
              </v-avatar>
              <h4 class="my-2 text--orange h2">Dr. Clea Bauch</h4>

              <v-btn>buchen</v-btn>

            </v-flex>
          </v-layout>

          <div class="panel-style mt-5 mb-2 background--transparent">
            <v-expansion-panel focusable>
              <v-expansion-panel-content>
                <div slot="header">Was wir vermitteln</div>
                <v-card>
                  <v-card-text class="pa-3">
                    <h2 class="mb-1">Lernziele & Kompetenzen</h2>
                    <ul class="ml-0">
                      <li>Die richtige Einstellung und das nötige Handwerkszeug zur effektiven Verhandlungsführung</li>
                      <li>Strategien und Methoden, um optimale Verhandlungsergebnisse zu erzielen</li>
                      <li>Die Fähigkeit, auch dann Geschäfte abzuschließen, wenn die Verhandlungspartner weiterhin
                        unterschiedliche Standpunkte vertreten
                      </li>
                      <li>Die Fähigkeit, taktische und psychologische Verhandlungsfallen zu erkennen und zu vermeiden
                      </li>
                      <li>Selbstvertrauen beim Umgang mit komplexen und aufreibenden Situationen</li>
                      <li>Gekonnter Umgang mit Kräfteungleichgewichten und schwierigen Persönlichkeiten</li>
                      <li>Verbesserte Fähigkeiten in puncto Einflussnahme, Werteinforderung und Einschätzung des
                        Verhandlungspartners
                      </li>
                      <li>Stärkere Führungsqualitäten durch Schulung des Verhandlungsgeschicks</li>
                    </ul>

                    <h2 class="mt-5 mb-1">Inhalte</h2>
                    Das gesamte Programm ist interaktiv gestaltet und legt großen Wert auf sofortige praktische
                    Anwendbarkeit. Anhand interessanter Fallstudien aus dem Geschäftsalltag werden Methoden trainiert
                    und
                    besprochen. Sie erlernen und erproben Taktiken, um auch dann die Oberhand zu behalten, wenn Risiken
                    und Unsicherheiten auftauchen. Darüber hinaus wird Ihnen mithilfe verschiedener Methoden vermittelt,
                    wie Sie die Persönlichkeitstypen ihrer Verhandlungspartner erkennen und Ihre verbale und nonverbale
                    Kommunikation effektiv einsetzen können.
                    Besonders im Fokus stehen Lösungsansätze für schwierige Verhandlungssituationen, wenn z. B.
                    Verhandlungspartner ablehnend reagieren, mit harten Bandagen verhandelt wird oder die Lage extrem
                    angespannt ist. Durch Rollenspiele und praktische Übungen können Sie die erlernten Methoden sofort
                    umsetzen und trainieren und gewinnen damit Vertrauen in Ihre Verhandlungsstärke.
                  </v-card-text>
                </v-card>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </div>

          <div class="panel-style my-2 pl-0 background--transparent">
            <v-expansion-panel focusable>
              <v-expansion-panel-content>
                <div slot="header">Wer referiert</div>
                <v-card>
                  <v-card-text class="pa-3">
                    <p>
                      Clea hat lange Jahre Erfahrung in der Energiebranche in verschiedenen operativen und strategischen
                      Rollen. Heute ist sie in der Geschäftsleitung einer international tätigen Familienunternehmung,
                      führt verschiedene Verwaltungsrats- und Stiftungsratsmandate und ist CEO ihrer eigenen
                      Beratungsfirma.
                      Sie hat im Verlaufe ihrer bisherigen Karriere stets international gearbeitet und hat deshalb weit
                      reichende Erfahrung in Sachen Kommunikation und Führung auf Distanz.
                    </p>
                    <p>
                      Ihr Studium an der Universität Fribourg (CH) schloss sie mit dem Doktorat ab. Ihre
                      Board-Zertifizierung hat sie am Insead (FR) im Rahmen des International Directors Program erlangt.
                      Nebenberuflich unterrichtet Clea an verschiedenen Institutionen in der Schweiz und ist Learning
                      Coach am Insead.
                    </p>
                  </v-card-text>
                </v-card>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </div>

          <div class="panel-style my-2 pl-0 background--transparent">
            <v-expansion-panel focusable>
              <v-expansion-panel-content>
                <div slot="header">Was Du leistest</div>
                <v-card>
                  <v-card-text class="pa-3">
                    <ul>
                      <li>Bearbeitung aller Sessions</li>
                      <li>Quizzle zu den Tools für digitale Kommunikation</li>
                      <li>Quizzle zu den Tools für virtuelle Zusammenarbeit</li>
                      <li>Mini-Case-Study zur Kommunikation und Führung auf Distanz</li>
                    </ul>
                  </v-card-text>
                </v-card>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </div>

        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
  import UNIT_QUERY from '@/graphql/gql/unit.gql'

  export default {
    props: {
      slug: {
        required: true,
        type: String
      }
    },

    data() {
      return {
        avatar: ''
      }
    },

    apollo: {
      unit() {
        return {
          query: UNIT_QUERY,
          variables() {
            return {
              slug: this.slug
            }
          }
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  .theme--light .v-expansion-panel .v-expansion-panel__container {
    color: $orange;
  }

  .panel-style {
    border-top: $orange 1px solid;
    .v-expansion-panel__header {
      padding-left: 0 !important;
    }
  }

  .v-expansion-panel.v-expansion-panel--focusable {
    margin: 0;
    box-shadow: none;
  }

  .theme--light.v-expansion-panel .v-expansion-panel__container {
    background-color: transparent;
  }

</style>
