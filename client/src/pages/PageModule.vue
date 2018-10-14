<template>
  <div v-if="module">
    <div>
      <v-container class="pt-5">
        <h1 class="mb-1 mt-1 text--violet">{{module.title}}</h1>
        <div class="lead">{{module.lead}}</div>
        <span v-if="user && moduleBooked" class="text-sm-left text-md-center">
          <v-btn class="btn-secondary btn-minimal" @click="deleteModuleProgress(module.slug)">
            <v-icon>close</v-icon>
          </v-btn>
        </span>
      </v-container>

      <div>
        <v-container grid-list-xl>
          <v-layout row wrap>
            <v-flex xs12 sm5 md6>
              <img :src="module.heroImage"/>
            </v-flex>
            <v-flex xs12 sm7 md6>
              <div v-html="module.description" class="mb-2 mt-1 paragraph"></div>

              <div class="mt-4" v-if="!moduleBooked">
                <v-btn v-if="user" @click="startModuleProgress(module.slug)">
                  Modul buchen
                </v-btn>
                <v-btn v-else :to="{ name: 'login'}" exact router>
                  Modul buchen
                </v-btn>
              </div>

              <div v-if="module.videoId" class="mt-5 mb-1">
                <v-layout row wrap>
                  <v-flex xs12 sm5 md5>
                    <a href="#" @click.stop="showVideoPlayer=true">
                      <img class="video-thumbnail" :src="module.videoThumbnailData.thumbnail_url_with_play_button"/>
                    </a>
                    <VideoPlayer :visible="showVideoPlayer" :videoId="module.videoId" @close="showVideoPlayer=false"/>
                  </v-flex>
                  <v-flex xs12 sm7 md7>
                    <div v-html="module.videoDescription" class="text--light"></div>
                  </v-flex>
                </v-layout>

              </div>
            </v-flex>
          </v-layout>
        </v-container>
      </div>

      <section v-if="moduleBooked">
        <v-container class="py-2">
          <div class="mt-5 mb-2">Finde heraus wo du stehst</div>
        </v-container>

        <div class="background--orange">
          <div class="container-process-bg text--white">
            <v-container grid-list-md class="py-3">
              <v-btn flat class="module--action-button" @click.stop="showModuleGoalDialog=true">
                <v-icon class="mr-2">play_circle_filled</v-icon>
                Ziele
              </v-btn>
              <v-btn flat class="module--action-button" @click.stop="showLearningsDialog=true">
                <v-icon class="mr-2">play_circle_filled</v-icon>
                Learnings
              </v-btn>
              <v-btn flat class="module--action-button" @click.stop="showActionPlanDialog=true">
                <v-icon class="mr-2">play_circle_filled</v-icon>
                Action Plan
              </v-btn>
            </v-container>

            <ModuleGoalWizard :visible="showModuleGoalDialog" @close="showModuleGoalDialog=false" :module="module"/>
            <LearningsWizard :visible="showLearningsDialog" @close="showLearningsDialog=false" :module="module"/>
            <ActionPlanWizard :visible="showActionPlanDialog" @close="showActionPlanDialog=false" :module="module"/>
          </div>
        </div>
      </section>

      <section>
        <v-container grid-list-xl>
          <v-layout row wrap>
            <v-flex xs12 sm8 md8 lg8 xl8>
              <h2 v-if="contentUnits" class="h3 mb-3">Inhalte</h2>
              <Unit v-for="(item, index) in contentUnits"
                    :module="module"
                    :key="index"
                    :booked="moduleBooked"
                    :unit="item"
                    class="mb-4 background--violet-light">
              </Unit>

              <h2 v-if="interactiveUnits" class="mb-3 h3">Interaktiv</h2>
              <Unit v-for="(item, index) in interactiveUnits"
                    :module="module"
                    :key="index"
                    :booked="moduleBooked"
                    :unit="item"
                    class="mb-4 background--orange-light">
              </Unit>

            </v-flex>
            <v-flex xs12 sm4 md4 lg4 xl4>
              <h2 class="h3 underline">Ressourcen</h2>
              <div class="mb-3">
                <Tools v-if="moduleBooked" :tools="module.resources"/>
                <div class="mt-3 text--light" v-else>Hier findest Du bei Buchung weiterführende Artikel, Links und
                  mehr.
                </div>
              </div>

              <h2 class="h3 mt-5 underline">Tools & Templates</h2>
              <div class="mb-3">
                <Tools v-if="moduleBooked" :tools="module.tools"/>
                <div class="mt-3 text--light" v-else>Hier findest Du bei Buchung im Arbeitsalltag nützliche
                  Hilfestellungen.
                </div>
              </div>

              <h2 class="h3 mt-5 underline">Agenda</h2>
              <Agenda v-if="moduleBooked" :items="dummyAgenda"></Agenda>
              <div class="mt-3 text--light" v-else>Hier findest Du bei Buchung Termine & Kontaktinformationen</div>

            </v-flex>
          </v-layout>
        </v-container>
      </section>

    </div>
  </div>

</template>


<style lang="scss" scoped>
  @import "../styles/var";

  .module--action-button {
    font-size: 24px;
  }

</style>


<script>
  import {mapGetters} from 'vuex'

  import MODULE_QUERY from '@/graphql/gql/moduleAndModuleProgress.gql'
  import START_MODULE_PROGRESS from '@/graphql/gql/progress/startModuleProgress.gql'
  import DELETE_MODULE_PROGRESS from '@/graphql/gql/progress/deleteModuleProgress.gql'

  import Tools from '@/components/module/Tools'
  import VideoPlayer from '@/components/module/VideoPlayer'
  import Unit from '@/components/module/Unit'

  import ModuleGoalWizard from '@/components/module/goal/ModuleGoalWizard'
  import LearningsWizard from '@/components/module/learnings/LearningsWizard'
  import ActionPlanWizard from '@/components/module/actionplan/ActionPlanWizard'
  import Agenda from '@/components/reusable/Agenda'

  export default {
    props: {
      slug: {
        required: true,
        type: String
      }
    },

    computed: {
      ...mapGetters({
        user: 'getUser'
      })
    },

    components: {
      Tools,
      VideoPlayer,
      Unit,
      ActionPlanWizard,
      LearningsWizard,
      ModuleGoalWizard,
      Agenda
    },

    data() {
      return {
        module: null,
        moduleBooked: false,
        interactiveUnits: [],
        contentUnits: [],
        showVideoPlayer: false,
        showModuleGoalDialog: false,
        showLearningsDialog: false,
        showActionPlanDialog: false,
        dummyAgenda: [
          {'type': 'message', 'text': 'Samuel Ryser'},
          {
            'type': 'calendar',
            'text': 'Montag, 17/09/2018, 12:00 Uhr\n' +
            'Mittwoch, 24/08/2018, 16:30 Uhr\n' +
            'Freitag, 30/11/2018, 17:00 Uhr'
          },
          {'type': 'message', 'text': 'Fritz Renggli'},
          {'type': 'calendar', 'text': 'Montag, 27/09/2018, 12:00 Uhr'},
          {
            'type': 'event',
            'text': 'Führung von Führungskräften \n' +
            'KeyNote: Kurt Wenger (CEO ABC Group)\n' +
            'Moderation: Clea Bauch (talentlab)'
          },
          {
            'type': 'calendar',
            'text': 'Freitag, 28/09/2018'
          }
        ]
      }
    },

    methods: {
      startModuleProgress(moduleSlug) {
        this.$apollo.mutate({
          mutation: START_MODULE_PROGRESS,
          variables: {
            moduleSlug: moduleSlug
          },
          update: (store, {data}) => {
            this.moduleBooked = data.startModuleProgress.created
          }
        }).then((data) => {
          // Result
        }).catch((error) => {
          // Error
          console.error(error)
          // We restore the initial user input
          // this.newTag = newTag
        })
      },

      deleteModuleProgress(moduleSlug) {
        this.$apollo.mutate({
          mutation: DELETE_MODULE_PROGRESS,
          variables: {
            moduleSlug: moduleSlug
          },
          update: (store, {data}) => {
            this.moduleBooked = !data.deleteModuleProgress.deleted
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
    },

    created() {
      this.$apollo.addSmartQuery('module', {
        query: MODULE_QUERY,
        variables: {
          slug: this.slug
        },
        fetchPolicy: 'network-only',
        manual: true,
        result({data, loading, networkStatus}) {
          if (!loading) {
            if (data.module) {
              let _module = this.$lodash.clone(data.module)

              // TODO: code review
              _module.tools = JSON.parse(_module.tools)
              _module.resources = JSON.parse(_module.resources)
              _module.category = JSON.parse(_module.category)
              _module.videoThumbnailData = JSON.parse(_module.videoThumbnailData)


              this.module = _module
              document.title = _module.title

              // TODO: code review
              // debugger
              let bookedEntries = data.allModulesProgress.edges
              this.moduleBooked = bookedEntries && bookedEntries.length > 0
              // console.log(`Module Booked: ${this.moduleBooked}`)

              let units = data.userModuleUnits.edges.map(entry => ({'status': entry.node.status, ...entry.node.unit}))

              let contentType = ['INTERAKTIV']

              // TODO: filter on the server: split into types of units
              this.interactiveUnits = units.filter(x => contentType.includes(x.type))
              this.contentUnits = units.filter(x => !contentType.includes(x.type))
            } else {
              console.log('Data: data.modules not available..')
            }
          }
        }
      })
    }
  }
</script>
