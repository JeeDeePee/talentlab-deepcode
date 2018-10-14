<template>
  <div class="pa-3">
    <router-link :to="{name: 'unit', params: {slug: unit.slug}}" exact router>
      <div class="text--color">
        <h4 class="h4">{{unit.title}}</h4>

        <div class="mt-2 mb-4">
          {{unit.teaser}}
        </div>
        <div>
          <!--
          <v-btn v-if="booked && !unitBooked" @click="startUnitProgress(unit.slug, module.slug)">Buchen</v-btn>
          <v-btn v-if="booked && unitBooked">Bewerten</v-btn>
          -->

          <v-icon>play_arrow</v-icon>
          <span class="bold">{{unit.type}}</span>
          <v-icon class="ml-4 mr-1">filter_none</v-icon>
          <span class="text--light">{{unit.count}}</span>
          <v-icon class="ml-4 mr-1"> schedule</v-icon>
          <span class="text--light">{{unit.duration}}</span>
        </div>
      </div>

    </router-link>
  </div>
</template>

<script>
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
    }
  }
</script>s
