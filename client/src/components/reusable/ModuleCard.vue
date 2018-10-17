<template>
  <router-link :to="{name: 'module', params: {slug: module.slug}}">
    <v-card :class="{'module-card--minimal': minimal}">

      <div v-if="progress">

        <v-layout row wrap>
          <v-flex xs12 sm8 class="py-0">

            <v-card-title primary-title>
              <div>
                <span class="text--light uppercase">{{module.skill}}</span><br>
                <h3 class="mt-2 mb-1">{{module.title}}</h3>
              </div>
            </v-card-title>

            <v-card-text>
              {{module.teaser}}
            </v-card-text>

          </v-flex>
          <v-flex xs12 sm4 class="pa-4 text-sm-right">
            <v-progress-circular
              :rotate="360"
              :size="100"
              :width="15"
              :value="80"
              color="teal"
            >
              80
            </v-progress-circular>
          </v-flex>
        </v-layout>

      </div>


      <div v-else>
        <v-card-title primary-title>
          <div>
            <span class="text--light uppercase">{{module.skill}}</span><br>
            <h3 class="mt-2 mb-1">{{module.title}}</h3>
          </div>
        </v-card-title>

        <v-card-text>
          {{module.teaser}}
        </v-card-text>

        <v-img class="module-card---image" v-if="!minimal" :src="module.heroImage">
          <div v-if="module.status && !minimal">
            <v-icon class="module--booked">done</v-icon>
          </div>
        </v-img>

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

      progress: {
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

    &.module-card--minimal {
      background: $violet-light;
      border: none;
    }

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
