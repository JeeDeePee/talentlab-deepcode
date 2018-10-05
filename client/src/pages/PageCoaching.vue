<template>
  <div>
    <section class="background--violet pt-5">
      <v-container grid-list-xl>
        <h1 class="mb-2">Coaching-Abonnement</h1>
        <div class="h2 mb-5">Finde Antworten! Werde wirkungsvoller! Entfalte Dein Potential!</div>

        <v-layout row wrap>
          <v-flex xs12 sm6>
            <v-img :src="require(`@/assets/img/dashboard_career.png`)" class="hero--image"></v-img>
          </v-flex>
          <v-flex xs12 sm6>
            <div v-if="coaching.description" v-html="coaching.description" class="mb-2 mt-1 description"></div>
            <div v-if="coaching.videoId" class="mt-5 mb-1">
              <v-layout row wrap>
                <v-flex xs12 sm5 md5>
                  <a href="#" @click.stop="showVideoPlayer=true">
                    <img class="video-thumbnail" :src="coaching.videoThumbnailData.thumbnail_url_with_play_button"/>
                  </a>
                  <VideoPlayer :visible="showVideoPlayer" :videoId="coaching.videoId" @close="showVideoPlayer=false"/>
                </v-flex>
                <v-flex xs12 sm7 md7>
                  <div v-html="coaching.videoDescription"></div>
                </v-flex>
              </v-layout>

              <div class="mt-4">
                <v-btn @click="showCoachingWizard=true">
                  Themen auswählen
                </v-btn>
              </div>
            </div>

          </v-flex>
        </v-layout>
      </v-container>
    </section>

    <section class="pt-4 background--beige">
      <v-container grid-list-xl>
        <v-layout row wrap>

          <v-flex xs12 class="text-xs-center">
            <h2 class="h1 mb-4">Wie werden unsere Coaches ausgewählt?</h2>
            <div class="h2 mb-5">talentlab bietet eine auf die Bedürfnisse abgestimmte … lorem ipsum dolor lorem ipsum
              dolor…
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
              <div v-html="coach.description" class="text-xs-left"></div>
            </div>
          </v-flex>


        </v-layout>
      </v-container>
    </section>

    <section class="pt-4 background--beige">
      <v-container>
        <h2 class="h1 mb-4" id="how-to-find-a-coach">Wie kann ich den richtigen Coach für mich finden?</h2>
        <div class="h2 mb-5">Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem
          ipsum
          dolor sit amet.
        </div>

        <div class="panel-style background--white" v-for="(detail,i) in details" :key="i">
          <v-expansion-panel focusable>
            <v-expansion-panel-content>
              <div slot="header" class="h2">{{detail.title}}</div>
              <v-card>
                <v-card-text class="pa-3">
                  <div v-html="detail.description"></div>
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </div>

        <div class="mt-5 text-xs-center">
          <v-btn @click="showCoachingWizard=true">
            Coaching starten
          </v-btn>
        </div>

      </v-container>
    </section>

    <CoachingWizard :visible="showCoachingWizard" @close="showCoachingWizard=false"/>

  </div>
</template>

<script>
  import VideoPlayer from '@/components/module/VideoPlayer'
  import CoachingWizard from '@/components/coaching/CoachingWizard'

  export default {
    components: {
      VideoPlayer,
      CoachingWizard
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
            'name': 'Samuel Ryser',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
          },
          {
            'name': 'Samuel Ryser',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
          },
          {
            'name': 'Samuel Ryser',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
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
