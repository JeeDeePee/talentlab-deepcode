<template>
  <div>

    <h1 class="text--violet text-xs-center">Welches Abonnement passt zu dir?</h1>

    <div class="lead text-xs-center mt-3">
      Wähle ein Package
    </div>

    <div class="small--content">
      <v-layout>
        <v-flex xs6>

          <h3 class="my-5">Coach</h3>

          <v-avatar size=100 class="v-avatar--responsive">
            <v-img
              :src="coach.avatar"
              :alt="coach.name"
            ></v-img>
          </v-avatar>
          <span class="ml-2">
          {{coach.name}}
          </span>
        </v-flex>
        <v-flex xs6>
          <div>
            <h3 class="my-5">Abonnement wählen</h3>

            <v-radio-group v-model="selected">
              <v-radio
                v-for="(item,i) in subscriptions"
                :key="i"
                :label="item"
                :value="i"
              ></v-radio>
            </v-radio-group>

          </div>
        </v-flex>
      </v-layout>
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
        coach: {
          'name': 'Peter Naumann',
          'avatar': require(`@/assets/img/people/samuel-ryser.jpg`)
        },
        subscriptions: [
          '1 Stunde Coaching',
          '2 Stunden Coaching',
          '3 Stunden Coaching'
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

