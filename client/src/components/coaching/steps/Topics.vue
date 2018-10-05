<template>
  <div>
    <div class="h2 mt-3">Wähle Deine Coaching-Themen. Welche zwei der folgenden Themen bewegen Dich am meisten?</div>

    <div class="mt-5 text-xs-center">
      <v-btn @click="$emit('proceed', 'Coaches')" class="ml-2">Weiter</v-btn>
    </div>
  </div>
</template>

<script>

  export default {
    components: {}
  }
</script>
