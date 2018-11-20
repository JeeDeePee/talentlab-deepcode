<template>
  <div>

    <h1 class="text-xs-center text--violet">Welche Themen bewegen dich?</h1>
    <div class="lead mt-3 text-xs-center">Wähle maximal zwei Themen</div>

    <v-layout row wrap  class="background--white mb-3 mt-3">
      <v-flex xs12 sm6 class="mb-3">
        <v-checkbox
          v-for="(item,i) in topics.slice(0, 4)" :key="i"
          :label="item.title"
          v-model="selectedTopic"
          hide-details
        ></v-checkbox>
      </v-flex>
      <v-flex xs12 sm6>
        <v-checkbox
          v-for="(item,i) in topics.slice(4)" :key="i"
          :label="item.title"
          v-model="selectedTopic"
          hide-details
        ></v-checkbox>
      </v-flex>
    </v-layout>

    <div class="mt-5 text-xs-center">
      <v-btn class="btn-secondary mr-2" @click="$emit('proceed', 'Topics', true);">Zurück</v-btn>
      <v-btn @click="$emit('proceed', 'Coaches')" class="ml-2">weiter</v-btn>
    </div>
  </div>
</template>

<script>

  export default {
    components: {},

    data() {
      return {
        checked: [],
        topics: [
          {title: 'Standortbestimmung & Neuorientierung', id: 6},
          {title: 'Domain-Life-Balance', id: 9},
          {title: 'Frauen in Führungspositionen', id: 5},
          {title: 'Job Sharing', id: 10},
          {title: 'Persönliche oder berufliche Veränderungen und Krisen', id: 8},
          {title: 'Übernahme einer neuen Rolle', id: 4},
          {title: 'Übernahme einer Führungsfunktion', id: 1},
          {title: 'Führung von Führungskräften', id: 2},
          {title: 'Bewältigung anspruchsvoller Führungssituationen', id: 3},
          {title: 'Vorbereitung auf individuelle Herausforderungen', id: 7}
        ]
      }
    },
    computed: {
      selectedTopic: {
        set(focus) {
          // set in vuex
        },
        get() {
          // get from vuex
          return false
        }
      }
    }
  }
</script>
