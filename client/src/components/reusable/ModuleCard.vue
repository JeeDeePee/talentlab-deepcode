<template>
  <router-link :to="{name: 'module', params: {slug: module.slug}}">
    <v-card>
      <v-card-title primary-title>
        <div>
          <span class="light uppercase">{{module.skill}}</span><br>
          <h3 class="mt-2 mb-1">{{module.title}}</h3>
        </div>
      </v-card-title>

      <v-card-text>
        {{module.teaser}}
      </v-card-text>

      <v-img class="module-card---image" v-if="!minimal" :src="module.heroImage" height="200px"></v-img>

      <div v-if="module.status && !minimal">
        <v-icon class="module--booked">done</v-icon>
      </div>

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
  @import "../../styles/var";

  .v-card {
    height: 100%;
  }

  .module--booked {
    position: absolute;
    bottom: 16px;
    right: 16px;
    color: $white;
    background-color: $orange;
    border: 1px solid $white;
    padding: 4px;
  }
</style>
