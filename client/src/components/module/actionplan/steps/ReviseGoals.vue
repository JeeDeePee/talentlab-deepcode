<template>
  <div class="text-xs-center small--content">
    <h1 class="text--violet text-xs-center">Dein Ziel</h1>
    <p class="mt-4 mb-5 lead">Zu Beginn des Moduls hast du folgendes Ziel formuliert. Passe es bei Bedarf noch einmal
      an.</p>

    <TextBox class="mt-5" :placeholder="'Text erfassen'" v-model="moduleUserGoal.text"></TextBox>

    <div class="mt-5">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'StartActionPlan')">Zurück</v-btn>
      <v-btn class="btn-primary ml-2" @click="$emit('proceed', 'Learnings')">Weiter</v-btn>
    </div>
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
        moduleUserGoal: 'getModuleUserGoal',
        user: 'getUser'
      }),
      moduleTitle() {
        return this.moduleUserGoal.module ? this.moduleUserGoal.module.title : ''
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../../../styles/var";
</style>
