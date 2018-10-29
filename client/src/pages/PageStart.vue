<template>
  <div>
    <section class="background--violet text-xs-center">
      <v-container grid-list-xl class="pb-0">
        <h1 class="py-5 text--limited">talentlab ist der digitale Begleiter für Karriere- und Potenzialentwicklung</h1>
        <v-btn @click="$vuetify.goTo('#learn-more', {duration: 200, offset: -50})" class="mx-2">
          mehr erfahren
        </v-btn>
        <v-btn v-if="user" router exact :to="{ name: 'modules'}" class="mx-2">
          jetzt starten
        </v-btn>
        <v-img :src="require(`@/assets/img/moods/mensch-maschine_3.png`)" class="mt-4 hero--image"></v-img>
      </v-container>
    </section>

    <section class="text-xs-center background--beige py-5" id="learn-more">
      <v-container grid-list-xl class="py-0">

        <h2 class="text--violet mb-5">
          Entdecke Deine Talente. Stärke deine Kompetenzen. Nutze Dein volles Potenzial!
        </h2>

        <v-layout row wrap>
          <v-flex v-for="category in categories" :key="category.id" xs12 sm4 class="text-xs-center">
            <div>
              <component :is="category.iconComponent"/>
            </div>
            <h3 class="my-3">{{category.title}}</h3>
            <p class="paragraph">{{category.teaser}}</p>
          </v-flex>
        </v-layout>

      </v-container>
    </section>

    <section class="py-5">
      <v-container grid-list-xl class="py-0">

        <h2 class="text-xs-center text--violet">Mit digitalen Angeboten zu aktuellen Themen gezielt und flexibel Kompetenzen stärken!</h2>
        <div class="text-xs-center lead my-5">talentlab schlägt dir ein auf Deine Bedürfnisse abgestimmtes und
          flexibel erweiterbares Programm vor
        </div>

        <v-layout row wrap>
          <v-flex xs12 sm6 v-for="module in modules" :key="module.id" class="mb-1">
            <ModuleCard :module="module"/>
          </v-flex>
        </v-layout>

      </v-container>
    </section>

    <section class="text-xs-center background--beige py-5">
      <v-container class="py-0">
        <h2 class="text--violet">talentlab ist der digitale Begleiter für Karriere- und Potenzialentwicklung</h2>

        <div class="text--limited">
          <v-carousel hide-delimiters class="slim height-200 secondary--controls">
            <v-carousel-item v-for="(fact,i) in facts" :key="i" class="pa-5">
              <div class="h1 pb-4">
                {{fact.heading}}
              </div>
              <div class="lead">
                {{fact.text}}
              </div>
            </v-carousel-item>
          </v-carousel>
        </div>

      </v-container>
    </section>

    <section class="text-xs-center background--orange py-5">
      <v-container grid-list-xl class="py-0 agents">
        <div class="speech-bubble speech-bubble--bottom speech-bubble--transparent">
          <h2 class="lead text--white">Möchtest Du mehr erfahren?</h2>
          <div class="mt-2 text--white">Wir beraten Dich gerne individuell</div>
        </div>
        <v-layout row wrap>
          <v-flex xs12 sm6 v-for="(agent,i) in agents" :key="i">
            <v-avatar size=115 class="v-avatar--responsive">
              <v-img
                :src="agent.avatar"
                :alt="agent.name"
              ></v-img>
            </v-avatar>
            <h4 class="my-2 headline text--white">{{agent.name}}</h4>
            <div class="text--white">
              {{agent.title}}
            </div>
          </v-flex>
        </v-layout>

        <v-btn router exact class="mt-5" outline @click="$openChat">
          Chat starten
        </v-btn>

      </v-container>
    </section>

    <section class="background--white py-5">
      <v-container grid-list-xl class="py-0">
        <h2 class="text-xs-center mb-5 text--violet">Das sagen unsere Kunden</h2>

        <v-layout row wrap>
          <v-flex xs12 sm4 v-for="(review,i) in reviews" :key="i">
            <h4 class="text--orange mb-3">
              <v-icon lass="text--orange">person_outline</v-icon>
              <span class="ml-1">{{review.name}}</span>
            </h4>
            <div class="review--text text--violet font-italic">
              «{{review.text}}»
            </div>
          </v-flex>
        </v-layout>

      </v-container>
    </section>

    <section class="text-xs-center background--beige py-5">
      <v-container grid-list-xl>
        <h2 class="text--violet">Wer steht hinter talentlab?</h2>
        <div class="lead my-4">Vereinte Erfahrung und Passion in Sachen Personalanalytik, Bildung und IT</div>

        <v-layout row wrap>
          <v-flex xs12 sm4 v-for="(member,i) in members" :key="i">
            <v-avatar size=115 class="v-avatar--responsive">
              <v-img
                :src="member.avatar"
                :alt="member.name"
              ></v-img>
            </v-avatar>
            <h4 class="my-2 headline">{{member.name}}</h4>
            <div>
              {{member.title}}
            </div>
          </v-flex>
        </v-layout>
      </v-container>
    </section>

  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  import CATEGORIES_QUERY from '@/graphql/gql/categories.gql'
  import ModuleCard from '@/components/reusable/ModuleCard'

  import GrowingAsALeader from '@/assets/img/icons/growing-as-a-leader-grey.svg'
  import MasteringComplexity from '@/assets/img/icons/mastering-complexity-grey.svg'
  import MasteringRelations from '@/assets/img/icons/mastering-relations-grey.svg'

  export default {
    components: {
      GrowingAsALeader,
      MasteringComplexity,
      MasteringRelations,
      ModuleCard
    },

    computed: {
      ...mapGetters({
        user: 'getUser'
      })
    },

    data() {
      return {
        initialQuery: CATEGORIES_QUERY,
        categories: [],
        modules: [],
        agents: [
          {
            'name': 'Clea Bauch',
            'title': 'talentlab Advisor',
            'avatar': require(`@/assets/img/people/clea-bauch.jpg`)
          },
          {
            'name': 'Pawel Kowalski',
            'title': 'talentlab Advisor',
            'avatar': require(`@/assets/img/people/pawel-kowalski.jpg`)
          }
        ],
        facts: [
          {
            'heading': 'personalisiert',
            'text': 'talentlab ist auf individuelle Entwicklungsbedürfnisse zugeschnitten'
          },
          {
            'heading': 'flexibel',
            'text': 'talentlab bietet einen Mix an zeitgemäss aufbereiteten Lernangeboten'
          },
          {
            'heading': 'effizient',
            'text': 'talentlab macht Potenzialentwicklung skalierbar'
          },
          {
            'heading': 'persönlich',
            'text': 'talentlab legt Wert auf persönliche Begleitung'
          },
          {
            'heading': 'zielorientiert',
            'text': 'talentlab ist gerichtet auf die Anforderungen der Arbeitswelt der Zukunft'
          },
          {
            'heading': 'wirksam',
            'text': 'talentlab hilft der Organisation am Ball zu bleiben'
          },
          {
            'heading': 'personalisiert',
            'text': 'talentlab bindet auf Wunsch firmeneigene Inhalte ein'
          },
          {
            'heading': 'flexibel',
            'text': 'talentlab ermöglicht autonomes Lernen nach eigenem Rhythmus'
          },
          {
            'heading': 'effizient',
            'text': 'talentlab ist nahtlos und sicher in bestehende HR-Prozesse integrierbar'
          },
          {
            'heading': 'persönlich',
            'text': 'talentlab motiviert zur Vernetzung von Wissen und Erfahrung'
          },
          {
            'heading': 'zielorientiert',
            'text': 'talentlab bezieht Deine zu entwickelnden Kompetenzen ein'
          },
          {
            'heading': 'wirksam',
            'text': 'talentlab bezieht Deine zu entwickelnden Kompetenzen ein'
          },
          {
            'heading': 'personalisiert',
            'text': 'talentlab berücksichtigt unternehmensspezifische Schwerpunkte bei der Potenzialentwicklung'
          },
          {
            'heading': 'flexibel',
            'text': 'talentlab ermöglicht in den Arbeitsalltag integriertes Lernen'
          },
          {
            'heading': 'effizient',
            'text': 'talentlab ist intuitiv zu bedienen'
          },
          {
            'heading': 'zielorientiert',
            'text': 'talentlab verhilft zu Potenzialentwicklung mit klarem Strategiebezug'
          },
          {
            'heading': 'persönlich',
            'text': 'talentlab erlaubt massgeschneiderte Auswertungen'
          },
          {
            'heading': 'wirksam',
            'text': 'talentlab macht Potenzialentwicklung sichtbar'
          }
        ],
        members: [
          {
            'name': 'Daniel Fahrni',
            'title': 'VRP & CMO',
            'avatar': require(`@/assets/img/people/daniel-fahrni.jpg`)
          },
          {
            'name': 'Clea Bauch',
            'title': 'CEO',
            'avatar': require(`@/assets/img/people/clea-bauch.jpg`)
          },
          {
            'name': 'Pawel Kowalski',
            'title': 'CTO',
            'avatar': require(`@/assets/img/people/pawel-kowalski.jpg`)
          }
        ],
        reviews: [
          {
            'name': 'Anja, Projektleiterin',
            'text': 'Mit talentlab konnte ich mich effizient auf die Herausforderungen in meiner neuen Funktion vorbereiten\n' +
            '              und mich im Bereich agiles Projektmanagement fit machen.'
          },
          {
            'name': 'Martin, Head of HR',
            'text': 'Seit wir talentlab einsetzen, können wir unseren Kadern und Nachwuchsführungskräften ein umfassendes\n' +
            '              Angebot für ihre persönliche Entwicklung bieten.'
          },
          {
            'name': 'Jasmin, CEO',
            'text': 'talentlab ermöglicht es mir, die Kompetenzen in der Organisation gezielt zu fördern und die Wirkung\n' +
            '              unserer Massnahmen zur Potenzialentwicklung zu messen.'
          }
        ]
      }
    },

    apollo: {
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
            this.modules = data.userModules.edges.map(entry => ({'status': entry.node.status, ...entry.node.module}))
          }
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  .hero--image {
    max-width: 736px;
    margin: auto;
  }

  .container.agents {
    max-width: 500px;
  }


  .review--text {
    padding-left: 32px;
  }
</style>
