<template>
  <div>
    <v-container class="mt-3">
      <span class="grey--text">{{module.category.title}} - {{module.skill}}</span><br>
      <h2 class="mb-1 mt-1">{{module.title}}</h2>
      <!--<v-btn @click="$emit('delete-module-progress', module.slug)">-->
        <!--Buchung löschen-->
      <!--</v-btn>-->
    </v-container>

    <div class="hero-bg">
      <v-container grid-list-md>
        <v-layout row wrap>
          <v-flex xs12 sm6 md6 lg6 xl6>
            <div v-html="module.description" class="mb-2 mt-1 description"></div>

            <div v-if="module.videoId" class="mt-5 mb-1">
              <a href="#" @click.stop="showVideoPlayer=true">
                <img class="video-thumbnail" :src="module.videoThumbnailData.thumbnail_url_with_play_button"/>
              </a>
              <div v-html="module.videoDescription"></div>
              <VideoPlayer :visible="showVideoPlayer" :videoId="module.videoId" @close="showVideoPlayer=false"/>
            </div>

          </v-flex>
          <v-flex xs12 sm6 md6 lg6 xl6>
            <img :src="module.heroImage"/>
          </v-flex>
        </v-layout>
      </v-container>
    </div>

    <div class="container-process-bg">
      <v-container grid-list-md>
        <v-btn class="button item2" @click.stop="showModuleGoalDialog=true">Ziele</v-btn>
        <v-btn class="button item2" @click.stop="showLearningsDialog=true">Learnings</v-btn>
        <v-btn class="button item2" @click.stop="showActionPlanDialog=true">Action Plan</v-btn>
      </v-container>

      <ModuleGoalWizard :visible="showModuleGoalDialog" @close="showModuleGoalDialog=false" :module="module"/>
      <LearningsWizard :visible="showLearningsDialog" @close="showLearningsDialog=false" :module="module"/>
      <ActionPlanWizard :visible="showActionPlanDialog" @close="showActionPlanDialog=false" :module="module"/>
    </div>

    <v-container grid-list-xl>
      <v-layout row wrap>
        <v-flex xs12 sm8 md8 lg8 xl8>
          <h3>Lernangebote</h3>
          <Unit v-for="(unit, index) in units" :key="index" :booked="true" :unit="unit" :module="module" class="mb-4"></Unit>
        </v-flex>
        <v-flex xs12 sm4 md4 lg4 xl4>
          <h3>Ressourcen</h3>
          <Tools :tools="module.resources"/>
          <h3>Tools & Templates</h3>
          <Tools :tools="module.tools"/>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import {mapActions} from 'vuex'

  import Tools from '@/components/module/Tools'
  import VideoPlayer from '@/components/module/VideoPlayer'
  import Unit from '@/components/module/Unit'
  import ModuleGoalWizard from '@/components/module/goal/ModuleGoalWizard'
  import LearningsWizard from '@/components/module/learnings/LearningsWizard'
  import ActionPlanWizard from '@/components/module/actionplan/ActionPlanWizard'

  export default {
    props: {
      module: { required: true, type: Object },
      units: { required: true, type: Array }
    },

    components: {
      ActionPlanWizard,
      Tools,
      VideoPlayer,
      Unit,
      LearningsWizard,
      ModuleGoalWizard
    },

    data() {
      return {
        showVideoPlayer: false,
        showModuleGoalDialog: false,
        showLearningsDialog: false,
        showActionPlanDialog: false
      }
    },

    methods: {
      ...mapActions({
        resetActionPlanWizardState: 'resetActionPlanWizardState'
      })
    },

    created() {
      this.resetActionPlanWizardState()
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  img {
    max-width: 100%;
  }

  h2 {
    font-size: 44px;
  }

  h3 {
    font-size: 24px;
    margin-bottom: 12px;
  }

  .button {
    color: $grey-1;
  }

  .video-thumbnail {
    max-width: 200px;
  }

  .hero-bg {
    background-color: $blue;
  }

  .container-process-bg {
    background-color: $grey-9;
  }

  .description {
    font-size: 18px;
    font-weight: bold;
  }
</style>
