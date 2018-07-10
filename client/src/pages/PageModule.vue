<template>
  <div v-if="module">
    <ModuleDetail v-if="moduleBooked" :module="module"></ModuleDetail>
    <ModuleDetailBooked v-if="!moduleBooked" :module="module"></ModuleDetailBooked>
  </div>
</template>

<script>
  // import MODULE_QUERY from '@/graphql/gql/module.gql'
  import MODULE_QUERY from '@/graphql/gql/moduleAndModuleProgress.gql'

  import ModuleDetail from '@/components/module/ModuleDetail'
  import ModuleDetailBooked from '@/components/module/ModuleDetailBooked'

  export default {
    name: 'page-module',

    props: {
      slug: {
        required: true,
        type: String
      }
    },

    components: {
      ModuleDetail,
      ModuleDetailBooked
    },

    data() {
      return {
        module: null,
        moduleBooked: false
      }
    },

    created() {
      this.$apollo.addSmartQuery('container', {
        query: MODULE_QUERY,
        variables: {
          slug: this.slug,
          userName: 'test'
        },
        manual: true,
        result(data, loading, networkStatus) {
          if (!loading) {
            let _module = this.$lodash.clone(data.data.modules.edges[0].node)

            _module.tools = JSON.parse(_module.tools)
            _module.resources = JSON.parse(_module.resources)
            _module.category = JSON.parse(_module.category)
            _module.videoThumbnailData = JSON.parse(_module.videoThumbnailData)

            this.module = _module
            document.title = _module.title

            // TODO: code review
            let bookedEntries = data.data.allModulesProgress.edges
            this.moduleBooked = bookedEntries && bookedEntries.length > 0
          }
        }
      })
    }
  }
</script>

<style lang="scss" scoped>
  @import "../styles/var";

  img {
    max-width: 100%;
  }

  h2 {
    font-size: 44px;
  }

  h3 {
    font-size: 24px;
    margin-bottom: 12px;
  }

  .video-thumbnail {
    max-width: 200px;
  }

  .hero-bg {
    background-color: $blue;
  }

  .description {
    font-size: 18px;
    font-weight: bold;
  }
</style>
