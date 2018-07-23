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
        <v-btn v-if="booked && !unit.status">Starten</v-btn>
        <v-btn v-if="booked && unit.status">Bewerten</v-btn>
        <v-chip>{{unit.type}}</v-chip>
        <v-icon class="ml-3">filter_none</v-icon> {{unit.count}}
        <v-icon class="ml-3"> schedule</v-icon> {{unit.duration}}
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'unit',

    props: {
      unit: {
        required: true,
        type: Object
      },
      booked: {
        required: true,
        type: Boolean
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
