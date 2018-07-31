<template>
  <div class="grey--text">
    <h2>Selbstbeurteilung</h2>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex xs4>
          <h3 class="text-center">Fokus Kompetenzen</h3>
          <p>Diese Kompetnezen hast du asugewählt</p>

        </v-flex>

        <v-flex xs4>
          <h3 class="text-center">Wo stehst du heute?</h3>
          <p>Schiebe den Regler zum einstellen deiner Kompetenzstuffe</p>
        </v-flex>

        <v-flex xs4>
          <h3 class="text-center">Nächste Beurteilung</h3>
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
          <v-slider
            v-model="selectedFocus[index].currentLevel"
            thumb-label="always"
          ></v-slider>
        </v-flex>

        <v-flex xs4>
          <v-menu
            :close-on-content-click="false"
            v-model="selectedFocus[index].nextEvaluation"
            :nudge-right="40"
            lazy
            transition="scale-transition"
            offset-y
            full-width
            min-width="290px"
          >
            <v-text-field
              slot="activator"
              v-model="selectedFocus[index].nextEvaluation"
              prepend-icon="event"
              readonly
            ></v-text-field>
            <v-date-picker v-model="selectedFocus[index].nextEvaluation"></v-date-picker>

          </v-menu>
        </v-flex>

      </v-layout>
    </v-container>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn @click="$emit('proceed')">Selbstbeurteilung speichern</v-btn>
  </div>
</template>

<script>
  export default {
    name: 'my-focus',
    props: ['items'],
    // https://github.com/vuetifyjs/vuetify/issues/3466
    // https://stackoverflow.com/questions/50218773/typeerror-vm-refs-dialog-save-is-not-a-function-in-vuetifyjs

    methods: {},
    data() {
      return {

        // date: [],
      }
    },
    computed: {
      selectedFocus: function () {
        return this.$store.getters.getFocus
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";
</style>
