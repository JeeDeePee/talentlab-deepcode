<template>
  <div v-if="module">
    <div>
      <v-container class="mt-2">
        <span class="grey--text">{{module.category.title}} - {{module.skill}}</span><br>
        <h1 class="mb-1 mt-1">{{module.title}}</h1>
        <div class="lead">{{module.description}}</div>
      </v-container>

      <div v-if="moduleBooked" class="background--violet">

        <div class="container-process-bg text--white">
          <v-container grid-list-md>
            <v-btn flat class="module--action-button lead" @click.stop="showModuleGoalDialog=true">
              <v-icon class="mr-2">play_circle_filled</v-icon>
              Ziele
            </v-btn>
            <v-btn flat class="module--action-button lead" @click.stop="showLearningsDialog=true">
              <v-icon class="mr-2">play_circle_filled</v-icon>
              Learnings
            </v-btn>
            <v-btn flat class="module--action-button lead" @click.stop="showActionPlanDialog=true">
              <v-icon class="mr-2">play_circle_filled</v-icon>
              Action Plan
            </v-btn>
          </v-container>

          <ModuleGoalWizard :visible="showModuleGoalDialog" @close="showModuleGoalDialog=false" :module="module"/>
          <LearningsWizard :visible="showLearningsDialog" @close="showLearningsDialog=false" :module="module"/>
          <ActionPlanWizard :visible="showActionPlanDialog" @close="showActionPlanDialog=false" :module="module"/>
        </div>

      </div>
      <div v-else>
        <v-container grid-list-xl>
          <v-layout row wrap>
            <v-flex xs12 sm5 md6>
              <img :src="module.heroImage"/>
            </v-flex>
            <v-flex xs12 sm7 md6>
              <div v-html="module.description" class="mb-2 mt-1 description"></div>

              <div v-if="module.videoId" class="mt-5 mb-1">
                <v-layout row wrap>
                  <v-flex xs12 sm5 md5>
                    <a href="#" @click.stop="showVideoPlayer=true">
                      <img class="video-thumbnail" :src="module.videoThumbnailData.thumbnail_url_with_play_button"/>
                    </a>
                    <VideoPlayer :visible="showVideoPlayer" :videoId="module.videoId" @close="showVideoPlayer=false"/>
                  </v-flex>
                  <v-flex xs12 sm7 md7>
                    <div v-html="module.videoDescription"></div>
                  </v-flex>
                </v-layout>

                <div class="text-sm-left text-md-center">
                  <v-btn class="mt-4" @click="$emit('start-module-progress', module.slug)">
                    Modul buchen
                  </v-btn>
                </div>

              </div>
            </v-flex>
          </v-layout>
        </v-container>
      </div>

      <section class="background--mint-opacity">
        <v-container grid-list-xl>
          <v-layout row wrap>
            <v-flex xs12 sm8 md8 lg8 xl8>
              <h2 class="mb-3">Inhalte</h2>
              <Unit v-for="(item, index) in contentUnits"
                    :module="module"
                    :key="index"
                    :booked="moduleBooked"
                    :unit="item"
                    class="mb-4">
              </Unit>
            </v-flex>
            <v-flex xs12 sm4 md4 lg4 xl4>
              <h2 class="mb-3">Ressourcen <i class="material-icons icon-color">library_books</i></h2>
              <div class="mt-1 mb-3">
                <Tools v-if="moduleBooked" :tools="module.resources"/>
                <div v-else>Hier findest Du bei Buchung weiterführende Artikel, Links und vieles mehr.</div>
              </div>

              <h2 class="mb-3 mt-5">Tools & Templates <i class="material-icons icon-color">library_books</i></h2>
              <div class="mt-1 mb-3">
                <Tools v-if="moduleBooked" :tools="module.tools"/>
                <div v-else>Hier findest Du bei Buchung im Arbeitsalltag nützliche Hilfestellungen.</div>
              </div>
            </v-flex>
          </v-layout>
        </v-container>
      </section>

      <section class="background--blue-opacity">
        <v-container grid-list-xl>
          <v-layout row wrap>
            <v-flex xs12 sm8 md8 lg8 xl8>
              <h2 class="mb-3">Interaktiv</h2>
              <Unit v-for="(item, index) in interactivUnits"
                    :module="module"
                    :key="index"
                    :booked="moduleBooked"
                    :unit="item"
                    class="mb-4">
              </Unit>
            </v-flex>
            <v-flex xs12 sm4 md4 lg4 xl4>
              <h2 class="mb-3">Agenda</h2>
              <v-list v-if="moduleBooked" class="background--transparent v-list--adjust">
                <div v-for="(item,i) in dummyAgenda" :key="i">
                  <v-list-tile>
                    <v-list-tile-action>
                      <v-icon v-if="item.type==='calendar'" class="material-icons">calendar_today</v-icon>
                      <v-icon v-else-if="item.type==='message'" if="item.type=='calendar'" class="material-icons">
                        mail_outline
                      </v-icon>
                      <v-icon v-else class="material-icons">link</v-icon>
                    </v-list-tile-action>

                    <v-list-tile-content>
                      <v-list-tile-sub-title>{{item.text}}</v-list-tile-sub-title>
                    </v-list-tile-content>
                  </v-list-tile>
                  <v-divider v-if="i < dummyAgenda.length -1 "></v-divider>
                </div>
              </v-list>
              <div v-else>Hier findest Du bei Buchung Termine & Kontaktinformationen</div>
            </v-flex>
          </v-layout>
        </v-container>
      </section>

    </div>
  </div>

</template>

<script>
  import MODULE_QUERY from '@/graphql/gql/moduleAndModuleProgress.gql'
  import START_MODULE_PROGRESS from '@/graphql/gql/progress/startModuleProgress.gql'
  import DELETE_MODULE_PROGRESS from '@/graphql/gql/progress/deleteModuleProgress.gql'

  import Tools from '@/components/module/Tools'
  import VideoPlayer from '@/components/module/VideoPlayer'
  import Unit from '@/components/module/Unit'

  import ModuleGoalWizard from '@/components/module/goal/ModuleGoalWizard'
  import LearningsWizard from '@/components/module/learnings/LearningsWizard'
  import ActionPlanWizard from '@/components/module/actionplan/ActionPlanWizard'

  export default {
    props: {
      slug: {
        required: true,
        type: String
      }
    },

    components: {
      Tools,
      VideoPlayer,
      Unit,
      ActionPlanWizard,
      LearningsWizard,
      ModuleGoalWizard
    },

    data() {
      return {
        module: null,
        moduleBooked: false,
        interactivUnits: [],
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
              let bookedEntries = data.allModulesProgress.edges
              this.moduleBooked = bookedEntries && bookedEntries.length > 0
              // console.log(`Module Booked: ${this.moduleBooked}`)

              let units = data.userModuleUnits.edges.map(entry => ({'status': entry.node.status, ...entry.node.unit}))


              let contentType = ['WEBINAR', 'LERNFILM']

              // TODO: filter on the server
              this.interactivUnits = units.filter(x => !contentType.includes(x.type))
              this.contentUnits = units.filter(x => contentType.includes(x.type))
            } else {
              console.log('Data: data.modules not available..')
            }
          }
        }
      })
    }
  }
</script>


<style lang="scss">
  @import "../styles/var";

  .module--action-button {
    font-size: $lead-font-size !important;
    color: rgba(255, 255, 255, 0.8) !important;
    text-transform: initial !important;
  }
</style>
