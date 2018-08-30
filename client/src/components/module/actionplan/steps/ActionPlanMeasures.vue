<template>
  <div class="text-xs-center">
    <h1>Definiere Deinen Action Plan - Massnahmen</h1>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex sm6>
          <p>Welche Umsetzungsmassnahmen leitest Du ein?</p>
        </v-flex>
        <v-flex sm6>
          <p>Was ist Dein Zeitrahmen?</p>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <TextBox :initial="measuresText" v-on:save="save"></TextBox>
        <TextBox :initial="timeFrameText" v-on:save="save"></TextBox>
      </v-layout>

      <v-layout row wrap>
        <v-flex sm6>
          <p>Welche Ressourcen/Skills benötigst Du?</p>
        </v-flex>
        <v-flex sm6>
          <p>Von wem innerhalb oder ausserhalb der Organisation benötigst Du Commitment?</p>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <TextBox :initial="resourcesSkillsText" v-on:save="save"></TextBox>
        <TextBox :initial="committmentSupportText" v-on:save="save"></TextBox>
      </v-layout>
    </v-container>

    <v-btn class="btn-secondary" @click="$emit('back', 'ActionPlanBusinessGoal')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', 'ActionPlanOverview')">Weiter</v-btn>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'
  import TextBox from '@/components/reusable/TextBox'

  export default {
    components: {
      TextBox
    },

    computed: {
      ...mapGetters({
      })
    },

    data() {
      return {
        measuresText: 'Mustertext – Erforderliche Änderungen:\n' +
          '- Massnahmen auf der Sachebene\n' +
          '- eigene Verhaltensänderungen\n' +
          '- Rahmenbedingungen…',
        timeFrameText: '… Eintrag\n' +
          '… Eitnrag\n' +
          '… Eitnrag',
        resourcesSkillsText: 'finanzielle Mittel\n' +
          'Personelle Ressourcen\n' +
          'Skills',
        committmentSupportText: 'ZB. Support im eigenen Umfeld (Chef, Kollegen, Partner)'
      }
    },

    methods: {
      save(text) {
        console.log(`Saving text: ${text}`)
      }
    },

    created() {
      // console.log(this.$options._componentTag)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
