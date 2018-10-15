<template>
  <div>
    <h1 class="text-xs-center text--violet">Dein Action Plan steht!</h1>

    <div class="mt-4 mb-5 pa-4 background--orange text--white">
      <v-layout row wrap>
        <v-flex xs8>
          <div class="speech-bubble speech-bubble--transparent speech-bubble--right--transparent speech-bubble--right">
            <h2>Talentlab wünscht Dir viel Spass und Erfolg bei der Umsetzung!</h2>
            Dein Learning Advisor wird Dich in den nächsten Tagen für einen Review des Action Plans kontaktieren und
            weitere Schritte mit Dir besprechen.
          </div>
        </v-flex>
        <v-flex xs4 class="text-xs-center">
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
    </div>

    <div class="medium--content">
      <div class="text-xs-center">
        <div>{{ currentModule.title }}</div>
        <div>Action Plan von {{ user.firstName }}&nbsp;{{ user.lastName }}</div>
      </div>

      <div class="text-xs-center mt-5">
        <h2 class="text--violet">Das werde ich in meiner Organisation bewirken:</h2>
        <div class="mt-2">{{ actionPlan.impactText }}</div>
      </div>

      <v-layout row wrap class="mt-5">
        <v-flex xs12 sm4>
          <h4 class="mb-3 paragraph">Massnahmen</h4>
          <div>{{ actionPlan.measuresText }}</div>
        </v-flex>
        <v-flex xs12 sm4>
          <h4 class="mb-3 paragraph">Erforderliche Ressourcen & Skills</h4>
          <div>{{ actionPlan.resourcesSkillsText }}</div>
        </v-flex>
        <v-flex xs12 sm4>
          <h4 class="mb-3 paragraph">Commitment & Support</h4>
          <div>{{ actionPlan.commitmentSupportText }}</div>
        </v-flex>
      </v-layout>
    </div>

    <div class="mt-5 text-xs-center">
      <v-btn class=" mr-2" @click="print">Drucken</v-btn>
      <v-btn class="btn-secondary mr-2" @click="$emit('proceed', 'StartActionPlan', true);">Beenden</v-btn>
    </div>

  </div>
</template>

<script>
  import {mapGetters} from 'vuex'

  export default {
    data() {
      return {
        agent:
          {
            'name': 'Samuel Ryser',
            'title': 'talentlab Advisor',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`)
          }
      }
    },

    methods: {
      print() {
        // FIXME implement print view
        window.print()
      }
    },

    computed: {
      ...mapGetters({
        actionPlan: 'getActionPlan',
        currentModule: 'getCurrentModule',
        user: 'getUser'
      })
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
