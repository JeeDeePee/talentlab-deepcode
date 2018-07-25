<template>
  <div>
    <v-card>
      <router-link class="link" :to="{name: 'unit', params: {slug: unit.slug}}" exact router>
        <v-card-title primary-title>
          <h4>{{unit.title}}</h4>
        </v-card-title>
      </router-link>
      <v-card-text>
        <div>
          {{unit.teaser}}
        </div>
        <div class="grey--text">

          <v-chip>{{unit.type}}</v-chip>
          <v-icon class="ml-3">filter_none</v-icon> {{unit.count}}
          <v-icon class="ml-3"> schedule</v-icon> {{unit.duration}}
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
  import UNIT_QUERY from '@/graphql/gql/unit.gql'

  export default {
    name: 'page-unit',

    props: {
      slug: {
        required: true,
        type: String
      }
    },

    components: {
    },

    data() {
      return {
        unit: {
        }
      }
    },

    methods: {
    },

    apollo: {
      unit: {
        query: UNIT_QUERY,
        variables() {
          return {
            slug: this.slug
          }
        },
        manual: true,
        result(data, loading, networkStatus) {
          if (!loading) {
            this.unit = data.data.unit.edges[0].node
          }
        }
      }
    },

    created() {
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  .link {
    color: $text-color;
  }
</style>
