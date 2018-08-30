<template>
  <div class="text-xs-center">
    <h1>Definiere Deinen Action Plan - Business-Ziel</h1>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex sm6>
          <p>
            Was möchtest Du in Deiner Organisation im Bereich „Digital Communication & Virtual Collaboration“ bewirken?
            Beschreibe möglichst konkret den Zielzustand aus Business-Sicht.
            Welche Vorteile versprichst Du Dir davon?
          </p>
        </v-flex>
        <v-flex sm6>
          <p>
            Woran merkst Du, dass du erfolgreich bist?
          </p>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <TextBox :initial="impactText" v-on:save="save"></TextBox>
        <TextBox :initial="measureText" v-on:save="save"></TextBox>
      </v-layout>
    </v-container>

    <v-btn class="btn-secondary" @click="$emit('back', 'Learnings')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', 'ActionPlanMeasures')">Weiter</v-btn>
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
      ...mapGetters({})
    },

    data() {
      return {
        impactText: 'Wir brauchen mehr Klarheit in der Landschaft der eingesetzten digitalen Kommmunikationstools: Welche Tools werden für was eingesetzt.',
        measureText: 'Dies wird bewirken, dass wir effizienter und verbindlicher kommunizieren, intern wie auch mit unseren Geschäftspartnern. '
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
