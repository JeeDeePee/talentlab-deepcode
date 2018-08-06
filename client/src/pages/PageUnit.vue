<template>
  <div class="learn-unit">
    <div class="wrapper">
      <v-breadcrumbs>
        <v-icon slot="divider">chevron_right</v-icon>

        <v-breadcrumbs-item
          v-for="item in items"
          :disabled="item.disabled"
          :key="item.text"
        >
          {{ item.text }}
        </v-breadcrumbs-item>
      </v-breadcrumbs>
      <router-link class="link" :to="{name: 'unit', params: {slug: unit.slug}}" exact router>

      </router-link>
        <h1 class="mt-4">Erfolgreich verhandeln</h1>
        <h2 class="pb-4 mt-3">Dieses Programm stattet Sie mit den erforderlichen Fähigkeiten aus, um Verhandlungen auch unter schwierigsten Bedingungen erfolgreich zu führen. Es bietet eine Vielzahl von Strategien und Instrumenten, um die unterschiedlichsten Verhandlungssituationen mit externen wie internen Geschäftspartnern erfolgreich zu meistern.</h2>
        <v-btn class="mb-5 ml-0 mt-0" :to="{ name: 'fokus'}" exact router>
        Lernmodul buchen
        </v-btn>

        <h3>Dieser Kurs gehört zum Lernmodul «Partnering for Success».</h3>
        <v-btn class="mb-4 ml-0 mr-3 mt-4 floating" :to="{ name: 'fokus'}" exact router>
          <v-icon class="pr-2">school</v-icon>
          Kurs
        </v-btn>
        <div class="grey--text floating position-top">
          <v-icon class="ml-3">event_note</v-icon> {{unit.count}}
          <v-icon class="ml-3"> schedule</v-icon> {{unit.duration}}
          <v-btn class="mb-4 mt-0 " :to="{ name: 'fokus'}" exact router>
            <v-icon class="pr-2">share</v-icon>
            Share
          </v-btn>
        </div>
      </div>
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
        },
        items: [
          {
            text: 'Breadcrumb 1 Bern',
            disabled: false
          },
          {
            text: 'Breadcrumb 2 Züri',
            disabled: false
          },
          {
            text: 'Breadcrumb 3 Thun',
            disabled: true
          }
        ]
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

  .learn-unit {
    background-color: $learn-unit-bg-color;
  }

  .wrapper {
  max-width: 1100px;
  margin-left: auto;
  margin-right: auto;
  content: "";
  clear: both;
  display: table;
  }

  .wrapper:after, {
  content: "";
  clear: both;
  display: table;
  }

  h1 {
    font-size: 44px
  }

  h2 {
    font-size: 18px;
  }

  h3 {
    font-size: 15px;
  }

  .floating {
    float: left;
  }

  .position-top {
    margin-top: 12px;
  }
</style>
