<template>
  <router-link :to="{name: 'module', params: {slug: module.slug}}">
    <v-card>
      <v-card-title primary-title>
        <div>
          <span class="grey--text">{{module.skill}}</span><br>
          <h2>{{module.title}}</h2>
        </div>
      </v-card-title>

      <v-card-text>
        {{module.teaser}}
      </v-card-text>
      <v-card-media v-bind:src="module.heroImage" height="200px"></v-card-media>
    </v-card>
  </router-link>
</template>

<script>
  export default {
    name: 'module-teaser',
    props: {
      module: {
        required: true,
        type: Object
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  a {
    text-decoration: none;
  }

  h2 {
    padding-top: 16px;
  }

  .card {
    border-radius: 11px;
  }

  .card__title {
    padding: 16px 16px 0px 16px
  }

  .card__text {
    padding: 0px 16px 16px 16px
  }
</style>
