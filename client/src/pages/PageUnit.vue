<template>
  <div>
    <v-container grid-list-xl>
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

          <v-layout row wrap>
            <v-flex xs12 sm8>

              <h1 class="text--violet">{{unit.title}}</h1>

              <div class="pb-4 mt-3 lead" v-html="unit.description"></div>

              <div>
                <v-icon>play_arrow</v-icon>
                <span class="bold uppercase">{{unit.type}}</span>
                <v-icon class="text--light ml-3">event_note</v-icon>
                <span class="text--light uppercase">{{unit.count}}</span>
                <v-icon class="text--light ml-3"> schedule</v-icon>
                <span class="text--light uppercase">{{unit.duration}}</span>
              </div>

            </v-flex>
            <v-flex xs12 sm4 class="text-xs-center">

              <v-avatar size=115 class="v-avatar--responsive">
                <v-img
                  :src="require(`@/assets/img/people/clea-bauch.jpg`)"
                  :alt="avatar"
                ></v-img>
              </v-avatar>
              <h4 class="my-2 uppercase paragraph">Dr. Clea Bauch</h4>

              <v-btn class="mt-5 mb-3" v-if="moduleBooked && !unitBooked" @click="startUnitProgress(unit.slug, unit.moduleSlug)">buchen
              </v-btn>

              <div v-if="moduleBooked && !unitBooked">{{unit.price}}</div>

              <v-btn v-if="moduleBooked && unitBooked" class="btn-secondary">bewerten</v-btn>

            </v-flex>
          </v-layout>

          <div class="panel-style mt-5 mb-2 background--transparent">
            <v-expansion-panel focusable>
              <v-expansion-panel-content>
                <div slot="header" class="paragraph text--color bold">Was wir vermitteln</div>
                <v-card class="flat">
                  <v-card-text class="pt-3 pb-5 px-0">
                    <v-layout row wrap>
                      <v-flex xs12 sm6>
                        <h3 class="full-width">Ziele</h3>
                        <div v-html="unit.objectives"></div>
                      </v-flex>
                      <v-flex xs12 sm6>
                        <h3 class="full-width">Inhalte</h3>
                        <div v-html="unit.content"></div>
                      </v-flex>
                    </v-layout>

                  </v-card-text>
                </v-card>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </div>

          <div class="panel-style my-2 pl-0 background--transparent">
            <v-expansion-panel focusable>
              <v-expansion-panel-content>
                <div slot="header" class="paragraph text--color bold">Wer referiert</div>
                <v-card class="flat">
                  <v-card-text class="pt-3 pb-5 px-0">
                    <div v-html="unit.teacher"></div>
                  </v-card-text>
                </v-card>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </div>

          <div class="panel-style my-2 pl-0 background--transparent">
            <v-expansion-panel focusable>
              <v-expansion-panel-content>
                <div slot="header" class="paragraph text--color bold">Was du leistest</div>
                <v-card class="flat">
                  <v-card-text class="pt-3 pb-5 px-0">
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
