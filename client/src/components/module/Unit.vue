<template>
  <v-card>
    <v-card-title primary-title>
      <h4>{{unit.title}}</h4>
    </v-card-title>
    <v-card-text>
      <div>
        {{unit.teaser}}
      </div>
      <div class="grey--text">
        <!--<v-btn class="button item2" @click="$emit('delete-module-progress', module.slug)">-->
          <!--Buchung löschen-->
        <!--</v-btn>-->

        <v-btn v-if="booked && !unitBooked" @click="startUnitProgress(unit.slug, module.slug)">Starten</v-btn>
        <v-btn v-if="booked && unitBooked">Bewerten</v-btn>

        <v-chip>{{unit.type}}</v-chip>
        <v-icon class="ml-3">filter_none</v-icon> {{unit.count}}
        <v-icon class="ml-3"> schedule</v-icon> {{unit.duration}}
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
  import START_UNIT_PROGRESS from '@/graphql/gql/progress/startUnitProgress.gql'

  export default {
    name: 'unit',

    props: {
      module: {
        required: true,
        type: Object
      },
      unit: {
        required: true,
        type: Object
      },
      booked: {
        required: true,
        type: Boolean
      }
    },

    data() {
      return {
        unitBooked: this.unit.status
      }
    },

    methods: {
      startUnitProgress(unitSlug, moduleSlug) {
        // console.log(`startUnitProgress(${unitSlug}-(${moduleSlug}))`)

        this.$apollo.mutate({
          mutation: START_UNIT_PROGRESS,
          variables: {
            username: 'test',
            unitSlug: unitSlug,
            moduleSlug: moduleSlug
          },
          update: (store, { data }) => {
            this.unitBooked = data.startUnitProgress.created
          }
        }).then((data) => {
          // Result
          // console.log(data)
        }).catch((error) => {
          // Error
          console.error(error)
          // We restore the initial user input
          // this.newTag = newTag
        })
      }
    },

    created() {
      // console.log(this.unit)
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  h4 {
    font-size: 18px;
  }

  .card {
    border-radius: 2px;
  }

  .card__title {
    padding: 16px 16px 0 16px
  }

  .card__text {
    padding: 0 16px 16px 16px
  }
</style>
