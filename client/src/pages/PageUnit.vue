<template>
  <div class="background--mint-opacity">
    <v-container>
      <div v-if="unit">
        <div>
          <v-breadcrumbs class="pl-0">
            <v-icon slot="divider">chevron_right</v-icon>
            <v-breadcrumbs-item class="link" :to="{name: 'modules'}" exact router>
              {{unit.categoryTitle}}
            </v-breadcrumbs-item>
            <v-breadcrumbs-item class="link" v-if="unit.moduleSlug"
                                :to="{name: 'module', params: {slug: unit.moduleSlug}}" exact router>
              {{unit.moduleTitle}}
            </v-breadcrumbs-item>
            <v-breadcrumbs-item :disabled="true">
              {{unit.title}}
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
                  :src="require(`@/assets/img/people/clea-bauch.jpg`)"
                  :alt="avatar"
                ></v-img>
              </v-avatar>
              <h4 class="my-2 text--orange h2">Dr. Clea Bauch</h4>

              <v-btn v-if="moduleBooked && !unitBooked" @click="startUnitProgress(unit.slug, unit.moduleSlug)">buchen</v-btn>
              <v-btn v-if="moduleBooked && unitBooked" class="btn-secondary">bewerten</v-btn>

            </v-flex>
          </v-layout>

          <div class="panel-style mt-5 mb-2 background--transparent">
            <v-expansion-panel focusable>
              <v-expansion-panel-content>
                <div slot="header">Was wir vermitteln</div>
                <v-card>
                  <v-card-text class="pa-3">
                    <h2 class="mb-1">Lernziele & Kompetenzen</h2>
                    <div v-html="unit.objectives"></div>

                    <h2 class="mt-5 mb-1">Inhalte</h2>
                    <div v-html="unit.content"></div>
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
                    <div v-html="unit.teacher"></div>
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
                    <div v-html="unit.requirements"></div>
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
  import START_UNIT_PROGRESS from '@/graphql/gql/progress/startUnitProgress.gql'

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

    computed: {
      unitBooked: () => this.unit ? this.unit.status : false,
      moduleBooked: () => true
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
    },

    methods: {
      startUnitProgress(unitSlug, moduleSlug) {
        this.$apollo.mutate({
          mutation: START_UNIT_PROGRESS,
          variables: {
            unitSlug: unitSlug,
            moduleSlug: moduleSlug
          },
          update: (store, {data}) => {
            // this.unitBooked = data.startUnitProgress.created
            this.unit.status = data.startUnitProgress.created
          }
        }).then((data) => {
          // Result
        }).catch((error) => {
          // Error
          console.error(error)
          // We restore the initial user input
          // this.newTag = newTag
        })
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
