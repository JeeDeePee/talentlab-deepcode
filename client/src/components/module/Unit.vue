<template>
  <div>
    <router-link :to="{name: 'unit', params: {slug: unit.slug}}" exact router>
      <v-card>

        <v-card-title primary-title>
          <h3 class="h4">{{unit.title}}</h3>
        </v-card-title>

        <v-card-text>
          <div class="mt-2 mb-4">
            {{unit.teaser}}
          </div>
          <div>
            <!--
            <v-btn v-if="booked && !unitBooked" @click="startUnitProgress(unit.slug, module.slug)">Buchen</v-btn>
            <v-btn v-if="booked && unitBooked">Bewerten</v-btn>
            -->

            <v-icon>play_arrow</v-icon>
            {{unit.type}}
            <v-icon class="ml-3">filter_none</v-icon>
            {{unit.count}}
            <v-icon class="ml-3"> schedule</v-icon>
            {{unit.duration}}
          </div>
        </v-card-text>
      </v-card>
    </router-link>
  </div>
</template>

<script>
  import START_UNIT_PROGRESS from '@/graphql/gql/progress/startUnitProgress.gql'

  export default {
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
        this.$apollo.mutate({
          mutation: START_UNIT_PROGRESS,
          variables: {
            unitSlug: unitSlug,
            moduleSlug: moduleSlug
          },
          update: (store, {data}) => {
            this.unitBooked = data.startUnitProgress.created
          }
        }).then((data) => {
          // Result
        }).catch((error) => {
          // Error
          console.error(error)
          // We restore the initial user input
          // this.newTag = newTag
        })
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  .v-card {
    box-shadow: none;
  }

</style>
