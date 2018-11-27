<template>
  <div>
    <section class="background--violet pt-5">
      <v-container grid-list-xl class="pb-0 text-xs-center">
        <h1 class="mb-5">Deine Entwicklung im Überblick</h1>
        <v-img :src="require(`@/assets/img/moods/compi_2.png`)" class="mt-4 hero--image"></v-img>
      </v-container>
    </section>

    <section class="background--beige py-5">
      <v-container grid-list-xl>
        <h2 class="mb-4 text--violet text-xs-center">Deine Kompetenzen</h2>

        <v-layout row wrap>
          <v-flex v-for="category in categories" :key="category.id" xs12 sm4 class="text-xs-center">
            <div>
              <component :is="category.iconComponent"/>
            </div>
            <h3 class="my-3">{{category.title}}</h3>
            <p class="paragraph mb-5">{{category.teaser}}</p>
          </v-flex>
        </v-layout>

        <MyFocus class="mb-4"/>

      </v-container>
    </section>

    <section class="py-5">
      <v-container grid-list-xl>
        <h2 class="mb-5 text--violet text-xs-center">Dein Fortschritt</h2>
        <div class="mb-4" v-for="(module, index) in userModules" :key="index">
          <ModuleCard :module="module" minimal progress/>
        </div>
        <div class="mt-5 paragraph">Basierend auf deinem Entwicklungsfokus haben wir weitere Module für dich
          zusammengestellt:
        </div>

        <v-layout row wrap>
          <v-flex xs12 sm6 class="mb-1" v-for="(module, index) in suggestions" :key="index">
            <ModuleCard :module="module" minimal/>
          </v-flex>
        </v-layout>

      </v-container>
    </section>

    <section class="background--beige py-5">
      <v-container grid-list-xl>
        <h2 class="mb-4 text--violet text-xs-center">Deine Agenda</h2>

        <v-layout row wrap>
          <v-flex xs12 sm4>
            <div class="pa-4 background--white full-height">
              <h3 class="underline">Coaching & Mentoring</h3>
              <Agenda :items="coachingMentoringAgenda"></Agenda>
            </div>

          </v-flex>

          <v-flex xs12 sm4>
            <div class="pa-4 background--white full-height">
              <h3 class="underline">Sparing mit Peers</h3>
              <Agenda :items="peerAgenda"></Agenda>
            </div>
          </v-flex>

          <v-flex xs12 sm4>
            <div class="pa-4 background--white full-height">
              <h3 class="underline">Un-Conference</h3>
              <Agenda :items="conferenceAgenda"></Agenda>
            </div>
          </v-flex>

        </v-layout>
        <v-layout row wrap>

          <v-flex xs12 sm4>
            <div class="text-xs-center">
              <v-btn router exact class="mt-4" :to="{ name: 'coaching'}">
                Coach buchen
              </v-btn>
            </div>
          </v-flex>

          <v-flex xs12 sm4>
            <div class="text-xs-center">
              <v-btn class="mt-4">
                Peer suchen
              </v-btn>
            </div>
          </v-flex>

          <v-flex xs12 sm4>
            <div class="text-xs-center">
              <v-btn router exact class="mt-4" :to="{ name: 'modules'}">
                Neue Angebote
              </v-btn>
            </div>
          </v-flex>
        </v-layout>

      </v-container>
    </section>

  </div>
</template>

<script>
  import USER_DEVELOPMENT_QUERY from '@/graphql/gql/userDevelopment.gql'
  import CATEGORIES_QUERY from '@/graphql/gql/categories.gql'

  import {mapActions} from 'vuex'

  import MyFocus from '@/components/focus/MyFocus.vue'
  import ModuleCard from '@/components/reusable/ModuleCard'
  import Agenda from '@/components/reusable/Agenda'
  import GrowingAsALeader from '@/assets/img/icons/growing-as-a-leader-grey.svg'
  import MasteringComplexity from '@/assets/img/icons/mastering-complexity-grey.svg'
  import MasteringRelations from '@/assets/img/icons/mastering-relations-grey.svg'

  export default {
    components: {
      MyFocus,
      ModuleCard,
      GrowingAsALeader,
      MasteringComplexity,
      MasteringRelations,
      Agenda
    },

    data() {
      return {
        loading: true,
        suggestions: [],
        categories: [],

        dummyCurrentProcess: {
          'closedTasks': 18,
          'nextTasks': [
            'Kommunikation und Führung auf Distanz',
            'Leading through Disruption'
          ]
        },
        coachingMentoringAgenda: [
          {'type': 'message', 'text': 'Samuel Ryser'},
          {
            'type': 'calendar',
            'text': 'Montag, 17/09/2018, 12:00 Uhr\n' +
            'Mittwoch, 24/08/2018, 16:30 Uhr\n' +
            'Freitag, 30/11/2018, 17:00 Uhr'
          },
          {'type': 'message', 'text': 'Fritz Renggli'},
          {'type': 'calendar', 'text': 'Montag, 27/09/2018, 12:00 Uhr'}
        ],
        conferenceAgenda: [
          {
            'type': 'calendar',
            'text': 'Montag, 17/09/2018, 12:00 Uhr'
          },
          {
            'type': 'event',
            'text': 'Führung von Führungskräften \n' +
            'KeyNote: Kurt Wenger (CEO ABC Group)\n' +
            'Moderation: Clea Bauch (talentlab)'
          }
        ],
        peerAgenda: [
          {'type': 'message', 'text': 'Fritz Rengli'},
          {
            'type': 'calendar',
            'text': 'Montag, 20/10/2018, 10:00 Uhr'
          }
        ]
      }
    },

    apollo: {
      user: {
        query: USER_DEVELOPMENT_QUERY,
        fetchPolicy: 'network-only'
      },
      categories: {
        query: CATEGORIES_QUERY,
        variables: {
          numModules: 4
        },
        fetchPolicy: 'network-only',
        manual: true,
        result({data, loading, networkStatus}) {
          if (!loading) {
            this.categories = data.categories.edges.map(entry => entry.node)
            this.suggestions = data.userModules.edges.map(entry => ({'status': entry.node.status, ...entry.node.module})).slice(0, 2)
          }
        }
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
