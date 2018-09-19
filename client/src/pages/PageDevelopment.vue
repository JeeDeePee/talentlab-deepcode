<template>
  <div>
    <section class="background--violet pt-5">
      <v-container grid-list-xl>
        <h1 class="mb-5 text-xs-center">Dashboard – Deine Entwicklung</h1>
        <v-layout row wrap>
          <v-flex xs12 sm6>
            <v-img :src="require(`@/assets/img/dashboard_career.png`)" class="hero--image"></v-img>
          </v-flex>
          <v-flex xs12 sm6>
            Dein Potenzial - Deine Kompetenzen - Dein Entwicklung: Verfolge Deine Fortschritte und Aktivitäten. Per Schnellzugriff zu Deinen gebuchten Modulen und anstehenden Tasks und Terminen.
            <div class="text-xs-center mt-4">
              <v-btn :to="{ name: 'modules'}" exact router>
                Modul auswählen
              </v-btn>
            </div>
          </v-flex>
        </v-layout>
      </v-container>
    </section>

    <section class="pt-4">
      <v-container grid-list-xl>
        <v-layout row wrap>
          <v-flex xs12 sm7>
            <h2 class="mb-4">Meine Entwicklung</h2>
            <MyFocus class="mb-4"/>
          </v-flex>
          <v-flex xs12 sm5>
            <div class="pa-4 background--beige">
              <h2>Agenda</h2>
              <v-list class="background--beige v-list--adjust">
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
            </div>
          </v-flex>
        </v-layout>
      </v-container>
    </section>

    <section>
      <v-container grid-list-xl>
        <v-layout row wrap>
          <v-flex xs12 sm7>
            <div class="pa-4 background--orange-opacity">
              <h2>Aktueller Prozess</h2>

              <div>In den aktuellen Modulen sind folgende Tasks offen:</div>
              <ul class="mt-2 mb-4">
                <li v-for="(item,i) in dummyCurrentProcess.nextTasks" :key="i">{{item}}</li>
              </ul>
              Total {{dummyCurrentProcess.closedTasks}} abgeschlossene Tasks.
            </div>
          </v-flex>
          <v-flex xs12 sm5>
            <div class="pa-4 background--mint">
              <h2 class="body">Coaching-Abo</h2>
              <div>Bespreche Deine Entwicklung mit einem Coach oder Mentor.</div>
              <v-btn router exact class="mt-4" @click="$openChat">
                Coach buchen
              </v-btn>
            </div>
          </v-flex>
        </v-layout>
      </v-container>
    </section>

    <section>
      <v-container grid-list-xl>
        <h2 class="pb-4">Meine gebuchten Module</h2>
        <v-layout row wrap>
          <v-flex xs12 sm6 class="mb-1" v-for="(module, index) in userModules" :key="index">
            <ModuleCard :module="module" minimal/>
          </v-flex>
        </v-layout>
      </v-container>
    </section>

  </div>
</template>

<script>
  import USER_DEVELOPMENT_QUERY from '@/graphql/gql/userDevelopment.gql'

  import {mapActions} from 'vuex'

  import MyFocus from '@/components/focus/MyFocus.vue'
  import ModuleCard from '@/components/reusable/ModuleCard'

  export default {
    components: {
      MyFocus,
      ModuleCard
    },

    data() {
      return {
        loading: true,

        dummyCurrentProcess: {
          'closedTasks': 18,
          'nextTasks': [
            'Digital Communication & Virtual Collaboration',
            'Leading through Disruption'
          ]
        },
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

    apollo: {
      user: {
        query: USER_DEVELOPMENT_QUERY,
        fetchPolicy: 'network-only'
      }
    },

    computed: {
      userModules() {
        if (this.user) {
          let moduleProgress = this.user.usermoduleprogressSet.edges.map(entry => entry.node.module)
          return moduleProgress.map(function (entry) {
            const parsedCategory = JSON.parse(entry.category)
            return {...entry, category: {title: parsedCategory.title, slug: parsedCategory.slug}}
          })
        }
      }
    },

    methods: {
      ...mapActions({
        startModuleProgress: 'startModuleProgress'
      })
    }
  }
</script>
