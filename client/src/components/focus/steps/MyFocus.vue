<template>
  <div class="grey--text">
    <h2>Selbstbeurteilung</h2>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex xs4>
          <h3>Fokus Kompetenzen</h3>
          <p>Diese Kompetnezen hast du asugewählt</p>
        </v-flex>

        <v-flex xs4>
          <h3>Wo stehst du heute?</h3>
          <p>Schiebe den Regler zum einstellen deiner Kompetenzstuffe</p>
        </v-flex>

        <v-flex xs4>
          <h3>Nächste Beurteilung</h3>
          <p>Bis wann willst du dein Ziel erreichen</p>
        </v-flex>

      </v-layout>
    </v-container>

    <v-container fluid grid-list-xl>
      <v-layout row wrap v-for="(item, index) in selectedFocus" :key="index">
        <v-flex xs4>
          {{item.title}}
        </v-flex>

        <v-flex xs4>
          <v-slider v-model="item.currentLevel" thumb-label="always" max="10" min="1"></v-slider>
        </v-flex>

        <v-flex xs4>
          <v-menu :nudge-right="40" lazy transition="scale-transition" offset-y full-width min-width="290px">
            <v-text-field slot="activator" v-model="item.nextEvaluation" prepend-icon="event" readonly></v-text-field>
            <v-date-picker
              v-model="item.nextEvaluation"
            ></v-date-picker>
          </v-menu>
        </v-flex>

      </v-layout>
    </v-container>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn v-on:click="proceed">Selbstbeurteilung speichern</v-btn>
  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  export default {
    name: 'my-focus',

    props: ['items'],

    methods: {
      ...mapActions({
        newUserFocus: 'newUserFocus'
      }),
      proceed: function (event) {
        this.newUserFocus(this.selectedFocus);
        this.$emit('proceed')
      }
    },

    computed: {
      ...mapGetters({
          'selectedFocus': 'getUserFocusCache'
        }
      )
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../styles/var";
</style>
