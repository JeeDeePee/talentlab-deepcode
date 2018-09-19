<template>
  <div class="text-xs-center">
    <h1>Selbstbeurteilung</h1>

    <div class="mt-4 mb-5">Beurteile deine Fitness für bestehende und künftige Herausforderungen</div>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex xs4>
          <h2>Fokus Kompetenzen</h2>
          <div class="mt-4 mb-2">Diese Kompetnezen hast du asugewählt</div>
        </v-flex>

        <v-flex xs4>
          <h2>Wo stehst du heute?</h2>
          <div class="mt-4 mb-2">Bewege den Regler (1 = gering bis 10 = hoch)</div>
        </v-flex>

        <v-flex xs4>
          <h2>Nächste Beurteilung</h2>
          <div class="mt-4 mb-2">Bis wann willst du dein Ziel erreichen</div>
        </v-flex>

      </v-layout>
    </v-container>

    <v-container fluid grid-list-xl>
      <v-layout row wrap v-for="(item, index) in selectedFocus" :key="index" class="pt-0 pb-1 background--white-opacity my-3">
        <v-flex xs4 class="text--white v-align--center text-xs-left">
          {{item.title}}
        </v-flex>

        <v-flex xs4 class="pt-3">
          <v-slider hide-details v-model="item.currentLevel" thumb-label="always" :thumb-size="18" max="10"
                    min="1"></v-slider>
        </v-flex>

        <v-flex xs4 class="v-align--center">
          <v-menu :nudge-right="40" lazy transition="scale-transition" offset-y full-width min-width="290px">
            <v-text-field hide-details slot="activator" v-model="item.nextEvaluation" prepend-icon="event"
                          class="ma-0 pa-0"
                          readonly></v-text-field>
            <v-date-picker v-model="item.nextEvaluation"></v-date-picker>
          </v-menu>
        </v-flex>

      </v-layout>
    </v-container>

    <div class="mt-5">
      <v-btn class="btn-secondary mr-2" @click="$emit('back')">Zurück</v-btn>
      <v-btn class="ml-2" v-on:click="proceed">Selbstbeurteilung speichern</v-btn>
    </div>

  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  export default {
    props: ['items'],

    methods: {
      ...mapActions({
        newUserFocus: 'newUserFocus'
      }),
      proceed(event) {
        this.newUserFocus(this.selectedFocus);
        this.$emit('proceed')
      }
    },

    computed: {
      ...mapGetters({
          selectedFocus: 'getUserFocusCache'
        }
      )
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";


  .container.grid-list-xl .layout .flex {
    padding: 0 16px;
  }

</style>
