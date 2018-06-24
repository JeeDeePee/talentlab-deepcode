<template>
  <v-card>
    <v-card-text>
      <div class="grey--text">Mastering Complexity – Vernetztes Denken</div>
      <h3>Partnering for Success</h3>
      <div>Erfolgreiche Führung von Partnerschaften</div>
      <v-btn>Details anzeigen</v-btn>

      <h4 class="mb-1">Nächste Schritte</h4>

      <div class="mb-1">
        Webinar: Supply Chain Design<br>
        > Nächste Lektion starten
      </div>

      <div class="mb-1">
        Kurs: Erfolgreich verhandeln<br>
        > Anmelden
      </div>

      <img v-bind:src="'http://mountain.org/wp-content/uploads/Miraflores-Peru_TMI.jpg'">

    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'module'
  }
</script>

<style scoped>
  img {
    max-width: 100%;
  }

</style>
