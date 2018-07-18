<template>
  <v-card>
    <v-card-text>
      <div class="grey--text">Fokus Detail
        <v-btn @click="$emit('proceed')">Proceed</v-btn>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'fokus-detail',

    methods: {}
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  .card {
    background: rgba(253, 110, 34, 0.15);
    border: 1px solid #F7C3A8;
    border-radius: 11px;
    padding: 0;
  }

  .heading {
    font-size: 24px;
    font-weight: bold;
  }
</style>
