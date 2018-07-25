<template>
  <div class="grey--text">

    <h2>Wo willst du in deiner Entwicklung den Fokus setzen</h2>

    <v-container fluid grid-list-xl>
      <v-layout row wrap>
        <v-flex xs4 v-for="(item, index) in items" :key="index">
          <img :src="'https://talentlab-web.s3.amazonaws.com/original_images/category2_Al9ARbs.png'"><br>
          <h3 class="text-center">Mastering Complexity</h3>

          <p>Gewinne Leichtigkeit im Umgang mit Veränderungen</p>

          <v-checkbox
            v-model="checkedFocus"
            label="Vernetztes Denken"
            v-bind:value="item + '1'"
          ></v-checkbox>

          <v-checkbox
            v-model="checkedFocus"
            label="Agilität"
            v-bind:value="item + '2'"
          ></v-checkbox>

          <v-checkbox
            v-model="checkedFocus"
            label="Innovationsfähigkeit"
            v-bind:value="item + '3'"
          ></v-checkbox>

          <v-checkbox
            v-model="checkedFocus"
            label="Entscheidungsfähigkeit"
            v-bind:value="item + '4'"
          ></v-checkbox>

        </v-flex>
      </v-layout>
    </v-container>

    <v-btn @click="$emit('back')">Zurück</v-btn>
    <v-btn @click="$emit('proceed')">Proceed</v-btn>
  </div>
</template>

<script>
  export default {
    name: 'determine-focus',
    methods: {},
    data() {
      return {
        checkedFocus: [],
        items: [1, 2, 3]
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";
</style>
