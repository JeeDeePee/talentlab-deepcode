<template>
  <div>
    <section class="background--white">
      <v-container class="pb-0">
        <h1>Wähle die passenden Module!</h1>
        <div class="my-4 lead">talentlab schlägt dir je nach Fokus deiner Entwicklung die geeigneten Module vor.</div>
        <div class="text-xs-center">
          <v-btn router exact>
            mehr erfahren
          </v-btn>
          <v-btn router exact>
            jetzt starten
          </v-btn>
        </div>
      </v-container>

      <v-img :src="require(`@/assets/img/meine-module_talk-communication.jpg`)" class="mt-4 hero--image"></v-img>
    </section>

    <v-container grid-list-xl class="pt-4">

      <v-layout row wrap>
        <v-flex v-for="category in categories" :key="category.id" xs4 class="text-xs-center">
          <!--<img :src="category.icon"><br>-->
          <component :is="category.iconComponent"/>
          <br>
          {{category.title}}

        </v-flex>
        <v-flex xs12 sm6 v-for="module in modules" :key="module.id" class="mb-1">
          <ModuleTeaser :module="module"/>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import CATEGORIES_QUERY from '@/graphql/gql/categories.gql'

  import GrowingAsALeader from '@/components/icons/GrowingAsALeader'
  import MasteringComplexity from '@/components/icons/MasteringComplexity'
  import MasteringRelations from '@/components/icons/MasteringRelations'

  import ModuleTeaser from '@/components/categories/ModuleTeaser'

  export default {
    components: {
      GrowingAsALeader,
      MasteringComplexity,
      MasteringRelations,
      ModuleTeaser
    },

    data() {
      return {
        initialQuery: CATEGORIES_QUERY,
        categories: [],
        modules: []
      }
    },

    created() {
      document.title = 'Modul'
    },

    apollo: {
      categories: {
        query: CATEGORIES_QUERY,
        fetchPolicy: 'network-only',
        manual: true,
        result({data, loading, networkStatus}) {
          // debugger
          if (!loading) {
            this.categories = data.categories.edges.map(entry => entry.node)
            this.modules = data.userModules.edges.map(entry => ({'status': entry.node.status, ...entry.node.module}))
          }
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  .category-wrapper {
    width: 100%;
  }

</style>
