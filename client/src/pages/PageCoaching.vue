<template>
  <div>
    <section class="background--violet pt-5">
      <v-container grid-list-xl class="pb-0 text-xs-center">
        <h1 class="py-5">Werde wirkungsvoller mit Coaching!</h1>

        <v-btn v-if="user" @click="showCoachingWizard=true">
          Coach finden
        </v-btn>
        <v-btn v-else :to="{ name: 'login'}" exact router>
          Coach finden
        </v-btn>

        <v-img :src="require(`@/assets/img/moods/moodboard_2.png`)" class="mt-5 hero--image"></v-img>
      </v-container>
    </section>

    <section class="py-5 background--white text-xs-center">
      <v-container grid-list-xl class="pb-0 text-xs-center">
        <CoachingSVG></CoachingSVG>
        <h2 class="text--violet">Coaching:<br>Finde Antworten! Entdecke Deine Talente!</h2>

        <p class="lead mt-4">Ein Coaching unterstützt Dich optimal in Deiner Entwicklung und stärkt Dich in der Bewältigung persönlicher Herausforderungen.</p>
      </v-container>
    </section>

    <section class="py-5 background--white text-xs-center">
      <v-container grid-list-xl class="text-xs-center">
        <h2 class="text--violet">Coaching-Abonnement:<br> flexibel, persönlich und digital!</h2>

        <p class="lead mt-4">Ortsunabhängig und zeitlich flexibel bearbeitest du deine beruflichen Fragestellungen
          online oder persönlich im praktischen Abonnement.<br>
          Wähle deinen Coach oder Mentor abhängig von Thema und Erfahrung.</p>
      </v-container>
    </section>

    <section class="pt-4 background--beige">
      <v-container grid-list-xl>
        <v-layout row wrap>

          <v-flex xs12 class="text-xs-center">
            <h2 class="my-4 text--violet">Wie werden unsere Coaches ausgewählt?</h2>
            <div class="lead mb-5">
              <p>
                talentlab arbeitet mit professionellen Coaches und erfahrenen Managern als Mentoren zusammen, die über
                einen weitreichenden Erfahrungsschatz in ihren jeweiligen Fachgebieten verfügen.
              </p>
              <p>
                Alle Coaches und Mentoren durchlaufen bei talentlab einen strengen Akkreditierungsprozess.
              </p>
            </div>
          </v-flex>

          <v-flex xs12 sm4 v-for="(coach,i) in featuredCoaches" :key="i">
            <div class="pa-4 background--white text-xs-center">

              <v-avatar size=115 class="v-avatar--responsive">
                <v-img
                  :src="coach.avatar"
                  :alt="coach.name"
                ></v-img>
              </v-avatar>
              <h4 class="my-3 headline text-xs-center">{{coach.name}}</h4>
              <div v-html="coach.description" class="text-xs-center"></div>
            </div>
          </v-flex>
        </v-layout>

        <div class="text-xs-center my-5">
          <v-btn v-if="user" @click="showCoachingWizard=true">
            Coach finden
          </v-btn>
          <v-btn v-else :to="{ name: 'login'}" exact router>
            Coach finden
          </v-btn>
        </div>

      </v-container>
    </section>


    <CoachingWizard :visible="showCoachingWizard" @close="showCoachingWizard=false"/>

  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  import VideoPlayer from '@/components/module/VideoPlayer'
  import CoachingWizard from '@/components/coaching/CoachingWizard'
  import CoachingSVG from '@/assets/img/icons/coaching-grey.svg'

  export default {
    components: {
      VideoPlayer,
      CoachingWizard,
      CoachingSVG
    },

    computed: {
      ...mapGetters({
        user: 'getUser'
      })
    },

    data() {
      return {
        loading: true,
        showVideoPlayer: false,
        showCoachingWizard: false,

        details: [
          {
            title: 'Wähle Deine Coaching-Themen',
            description: 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga'
          },
          {
            title: 'Finde Deinen Coach',
            description: 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga'
          },
          {
            title: 'Organisiere Deine Coaching-Sessions',
            description: 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga'
          }
        ],

        featuredCoaches: [
          {
            'name': 'Rahel Knecht',
            'avatar': require(`@/assets/img/people/rahel-knecht.jpg`),
            'description': '<p>"Im Zentrum steht die Stärkung der eigenen Wirksamkeit."</p></p></p>'
          },
          {
            'name': 'Samuel Ryser',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>"Bei Veränderungen und für die persönliche Entwicklung ist die Nutzung der eigenen Ressourcen und Potenziale imminent wichtig."</p>'
          },
          {
            'name': 'Daniel Fahrni',
            'avatar': require(`@/assets/img/people/daniel-fahrni.jpg`),
            'description': '<p>"Die Aufmerksamkeit bei den Kompetenzen fokussieren."</p></p></p>'
          }
        ],

        coaching: {
          description: '<p>talentlab bietet eine flexible Form von Coaching an – persönlich und digital!</p>' +
          'Ortsunabhängig und zeitlich flexibel bearbeitest Du Deine persönlichen beruflichen Fragestellungen online oder persönlich mit professionellen Coachs und erfahrenen Sparringpartnern.</p>' +
          '<p>Wähle Deinen Coach abhängig von Thema und Erfahrung und erweitere das Abonnement flexibel nach Deinen Bedürfnissen.</p>',
          videoId: '275716804',
          videoThumbnailData: {thumbnail_url_with_play_button: 'https://i.vimeocdn.com/filter/overlay?src0=https%3A%2F%2Fi.vimeocdn.com%2Fvideo%2F708592156_640.jpg&src1=http%3A%2F%2Ff.vimeocdn.com%2Fp%2Fimages%2Fcrawler_play.png'},
          videoDescription: '<h3>Samuel Ryser</h3><p>Unser Experte erläutert Nutzen und Ablauf eines professionellen Coachings auf talentlab.</p>'
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  .panel-style {
    border-top: $beige 2px solid;
    .v-expansion-panel__header {
      padding-left: 0 !important;
    }
    max-width: 600px;
    margin: auto;
  }

  .v-expansion-panel.v-expansion-panel--focusable {
    margin: 0;
    box-shadow: none;
  }

  .theme--light.v-expansion-panel .v-expansion-panel__container {
    background-color: transparent;
  }
</style>
