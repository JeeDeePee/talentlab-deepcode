<template>
  <div class="text-xs-center">
    <h1>Reflektiere was Du gelernt hast</h1>
    <p>Das sind Deine Learnings aus den verschiedenen Units. Passe bei Bedarf noch einmal an.</p>

    <TextBox :initial="firstLearningText" v-on:save="save"></TextBox>

    <v-btn class="btn-secondary" @click="$emit('back', 'ReviseGoals')">Zurück</v-btn>
    <v-btn @click="$emit('proceed', 'ActionPlanBusinessGoal')">Weiter</v-btn>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'
  import TextBox from '@/components/reusable/TextBox'

  export default {
    props: ['breadcrumbs'],

    components: {
      TextBox
    },

    computed: {
      ...mapGetters({})
    },

    data() {
      return {
        firstLearningText: 'Kommunikation auf Distanz\n' +
          '\n' +
          '1. Bewusste Kommunikation ist auf Distanz mindestens genauso wichtig wie in der Face-to-Face Kommunikation\n' +
          '2. Bei Emails muss auf die Sprache geachtet werden\n' +
          '3. Video-Konferenzen sollten sorgfältig vorbereitet werden\n',
      }
    },

    methods: {
      save(text) {
        console.log(`Saving text: ${text}`)
      }
    },

    created() {
      // this.breadcrumbs[2].disabled = true
      // console.log(this.$options._componentTag)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
