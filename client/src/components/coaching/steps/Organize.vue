<template>
  <div>

    <h1 class="text--violet text-xs-center">Welches Abonnement passt zu dir?</h1>

    <div class="lead text-xs-center mt-3">
      Wähle ein Package
    </div>

    <div class="small--content">
      <v-radio-group v-model="selected">
        <v-layout>
          <v-flex xs4 v-for="(item,i) in subscriptions" :key="i">
            <div class="background--white px-3 py-4 package">
              <v-radio
                :label="item.title"
                :value="i"
                class="package--label bold text--color"
              >
              </v-radio>
              <div class="package--description">
                {{item.description}}
              </div>
            </div>
          </v-flex>
        </v-layout>
      </v-radio-group>
    </div>

    <div class="mt-5 text-xs-center">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'Coaches')">Zurück</v-btn>
      <v-btn @click="save" class="ml-2">Coach buchen</v-btn>
    </div>
  </div>
</template>

<script>

  export default {
    components: {},

    data() {
      return {
        selected: 1,
        subscriptions: [
          {title: '3er Package', description: 'online'},
          {title: '6er Package', description: 'online +1 persönliches Treffen'},
          {title: '3er Package', description: 'online +2 persönliches Treffen'}
        ]
      }
    },

    methods: {
      save() {
        this.$emit('proceed', 'Summary', true)
      }
    }
  }
</script>


<style lang="scss" scoped>
  @import "../../../styles/var";

  .package--description {
    margin-left: 31px;
  }

  .package--label .v-label {
    color: $text-color !important;
  }

  .package {
    height: 100%;
  }

</style>


<style>

</style>
