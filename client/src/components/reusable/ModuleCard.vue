<template>
  <router-link :to="{name: 'module', params: {slug: module.slug}}">
    <v-card>
      <v-card-title primary-title>
        <div>
          <span class="h3">{{module.skill}}</span><br>
          <h2 class="mt-2 mb-1">{{module.title}}</h2>
        </div>
      </v-card-title>

      <v-card-text>
        {{module.teaser}}
        <v-chip v-if="module.status && !minimal">Gebucht</v-chip>
      </v-card-text>

      <v-img class="module-card---image" v-if="!minimal" :src="module.heroImage" height="200px"></v-img>
    </v-card>
  </router-link>
</template>

<script>
  export default {
    props: {
      minimal: {
        required: false,
        type: Boolean
      },
      module: {
        required: true,
        type: Object
      }
    }
  }
</script>


<style lang="scss" scoped>
  .v-card {
    height: 100%;
  }
  .module-card---image {
  }

</style>
