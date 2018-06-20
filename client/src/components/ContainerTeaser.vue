<template>
  <router-link :to="{name: 'container', params: {slug: container.slug}}">
    <v-card>
      <v-card-title primary-title>
        <div>
          <span class="grey--text">{{container.skill}}</span><br>
          <h2>{{container.title}}</h2>
        </div>
      </v-card-title>

      <v-card-text>
        {{container.teaser}}
      </v-card-text>
      <v-card-media v-bind:src="container.heroImage" height="200px"></v-card-media>
    </v-card>
  </router-link>
</template>

<script>
  export default {
    name: 'container-teaser',
    props: {
      container: {
        required: true,
        type: Object
      }
    }
  }
</script>

<style scoped>
  a {
    text-decoration: none;
  }
</style>
