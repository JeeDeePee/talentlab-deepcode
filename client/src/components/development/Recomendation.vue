<template>
  <v-card>
    <v-card-text>
      <div class="grey--text">Verhandlungsfähigkeit / Kooperationsfähigkeit</div>
      <h4 class="mt-3 heading">Effizient kommunizieren</h4>
      <div class="mt-1">Gezieltes Training für Führungsalltag und Verhandlung</div>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  .card {
    background: rgba(255, 160, 109, 0.15);
    border: 1px solid #F7C3A8;
    padding: 0;
  }

  .heading {
    font-size: 24px;
    font-weight: bold;
  }

  .grey--text {
    text-transform: uppercase;
    color: $grey-9;
    opacity: 50%;
  }
</style>
