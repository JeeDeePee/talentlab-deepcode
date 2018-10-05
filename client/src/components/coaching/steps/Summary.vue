<template>
  <div>
    <div class="h2 mt-3">Vielen Dank für die Buchungsanfrage.<br>
      Unser Coach wir sich mit dir in Verbindung setzten.</div>

    <div class="mt-5 text-xs-center">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'Organize')">Zurück</v-btn>
      <v-btn class="ml-2" @click="$emit('proceed', 'Topics', true);">Weiter</v-btn>
    </div>
  </div>
</template>



<script>

  export default {
    components: {}
  }
</script>

