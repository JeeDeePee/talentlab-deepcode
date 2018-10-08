<template>
  <div>
    <v-container>
      <v-layout
        column
        align-center
        justify-center
      >
        <h1 class="mb-3">Seite nicht gefunden</h1>

        <v-btn
          class="mt-5"
          large
          :to="{ name: 'start'}"
          router
          exact
        >
          Start
        </v-btn>

      </v-layout>
    </v-container>
  </div>
</template>

<script>

</script>

<style lang="scss" scoped>

</style>
