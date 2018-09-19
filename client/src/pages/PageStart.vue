<template>
  <div>
    <section class="background--violet text-xs-center pt-5">
      <v-container grid-list-xl class="pb-0">
        <h1>talent<b>lab</b> ist der digitale Begleiter für Karriere- und
          Potenzialentwicklung</h1>
        <div class="my-4 lead">Nutze dein Potenzial und stärke deine Kompetenzen zielorientiert und wirksam!</div>
        <v-btn @click="$vuetify.goTo('#learn-more', {duration: 200, offset: -50})" class="btn-secondary">
          mehr erfahren
        </v-btn>
        <v-btn router exact :to="{ name: 'modules'}">
          jetzt starten
        </v-btn>
        <v-img :src="require(`@/assets/img/marketing_buro_frau-computer_viola.png`)" class="mt-4 hero--image"></v-img>
      </v-container>
    </section>

    <section class="text-xs-center background--beige py-5" id="learn-more">
      <v-container grid-list-xl class="py-0">

        <div class="h3 mb-4">Dein Potenzial > Deine Kompetenzen > Deine Entwicklung</div>

        <v-layout row wrap>
          <v-flex v-for="category in categories" :key="category.id" xs12 sm4 class="text-xs-center">
            <div>
              <component :is="category.iconComponent"/>
            </div>
            <div class="h2 my-3">{{category.title}}</div>
            <p>{{category.teaser}}</p>
          </v-flex>
        </v-layout>

      </v-container>
    </section>

    <section class="py-5">
      <v-container grid-list-xl class="py-0">

        <h2 class="h1 text-xs-center ">Mit digitalen Angeboten gezielt und flexibel Potenziale entwickeln!</h2>
        <div class="text-xs-center lead my-5">talent<b>lab</b> bietet eine auf die Bedürfnisse abgestimmte und flexibel
          erweiterbare Auswahl an Modulen zu aktuellen Themen
        </div>

        <v-layout row wrap>
          <v-flex xs12 sm6 v-for="module in modules" :key="module.id" class="mb-1">
            <ModuleCard :module="module"/>
          </v-flex>
        </v-layout>

      </v-container>
    </section>

    <section class="text-xs-center background--beige py-5">
      <v-container class="py-0 slider">
        <h2 class="h3">talent<b>lab</b> ist der digitale Begleiter für Karriere- und Potenzialentwicklung</h2>

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

      </v-container>
    </section>

    <section class="text-xs-center background--violet py-5">
      <v-container grid-list-xl class="py-0 agents">
        <div class="speech-bubble">
          <h2 class="lead">Möchtest Du mehr erfahren?</h2>
          <div class="mt-2">Wir beraten Dich gerne individuell</div>
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
            <div>
              {{agent.title}}
            </div>
          </v-flex>
        </v-layout>

        <v-btn router exact class="mt-5" @click="$openChat">
          Chat starten
        </v-btn>

      </v-container>
    </section>

    <section class="background--white py-5">
      <v-container grid-list-xl class="py-0">
        <h2 class="h1 text-xs-center mb-5">Das sagen unsere Kunden</h2>

        <v-layout row wrap>
          <v-flex xs12 sm4 v-for="(review,i) in reviews" :key="i">
            <h4 class="text--orange mb-3">
              <v-icon lass="text--orange">person_outline</v-icon>
              <span class="ml-1">{{review.name}}</span>
            </h4>
            <div>
              «{{review.text}}»
            </div>
          </v-flex>
        </v-layout>

      </v-container>
    </section>

    <section class="text-xs-center background--beige py-5">
      <v-container grid-list-xl>
        <h2 class="h1">Wer steht hinter talent<b>lab</b>?</h2>
        <div class="lead my-4">Vereinte Erfahrung und Passion in Sachen Personalanalytik, Lernen und IT</div>

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
  import CATEGORIES_QUERY from '@/graphql/gql/categories.gql'
  import ModuleCard from '@/components/reusable/ModuleCard'

  import GrowingAsALeader from '@/assets/img/Growing-as-a-Leader.svg'
  import MasteringComplexity from '@/assets/img/Mastering-Complexity.svg'
  import MasteringRelations from '@/assets/img/Mastering-Relations.svg'

  export default {
    components: {
      GrowingAsALeader,
      MasteringComplexity,
      MasteringRelations,
      ModuleCard
    },

    data() {
      return {
        initialQuery: CATEGORIES_QUERY,
        categories: [],
        modules: [],
        agents: [
          {
            'name': 'Nina Hagemann',
            'title': 'talentlab Advisor',
            'avatar': require(`@/assets/img/people/delia-werro-piave.jpg`)
          },
          {
            'name': 'Paul Markwarth',
            'title': 'talentlab Advisor',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`)
          }
        ],
        facts: [
          {
            'heading': 'Personalisiert',
            'text': 'Talentlab ist auf individuelle Entwicklungsbedürfnisse zugeschnitten.'
          },
          {
            'heading': 'flexibel',
            'text': 'talentlab ermöglicht autonomes Lernen nach eigenem Rhythmus.'
          },
          {
            'heading': 'effizient',
            'text': 'talentlab ist intuitiv zu bedienen.'
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
            'text': 'Seit wir talentlab einsetzen können wir unseren Kadern und Nachwuchsführungs-kräften ein umfassendes\n' +
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

  .container.slider {
    max-width: 600px;
  }

  .container.agents {
    max-width: 500px;
  }


</style>
