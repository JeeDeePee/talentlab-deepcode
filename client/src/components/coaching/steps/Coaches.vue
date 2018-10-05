<template>
  <div>
    <div class="h2 mt-3">Finde Deinen Coach. Folgende Coaches haben Erfahrung mit den gewählten Themen:</div>

    <div class="mt-5 text-xs-center">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'Topics')">Zurück</v-btn>
      <v-btn @click="save" class="ml-2">Weiter</v-btn>
    </div>
  </div>
</template>

<script>

  export default {
    components: {},

    methods: {
      save() {
        this.$emit('proceed', 'Organize')
      }
    }
  }
</script>
