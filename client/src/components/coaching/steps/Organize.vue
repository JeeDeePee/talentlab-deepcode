<template>
  <div>
    <div class="h2 mt-3">Organisiere Deine Coaching-Sessions. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna.</div>

    <div class="mt-5 text-xs-center">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'Coaches')">Zurück</v-btn>
      <v-btn @click="save" class="ml-2">Weiter</v-btn>
    </div>
  </div>
</template>

<script>

  export default {
    components: {},

    methods: {
      save() {
        this.$emit('proceed', 'Summary')
      }
    }
  }
</script>

