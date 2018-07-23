<template>
  <div v-if="module">
    <ModuleDetailBooked v-if="moduleBooked" :module="module" v-on:delete-module-progress="deleteModuleProgress($event)"></ModuleDetailBooked>
    <ModuleDetail v-if="!moduleBooked" :module="module" v-on:start-module-progress="startModuleProgress($event)"></ModuleDetail>
  </div>
</template>

<script>
  import MODULE_QUERY from '@/graphql/gql/moduleAndModuleProgress.gql'

  import START_MODULE_PROGRESS from '@/graphql/gql/mutations/startModuleProgress.gql'
  import DELETE_MODULE_PROGRESS from '@/graphql/gql/mutations/deleteModuleProgress.gql'

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

    methods: {
      startModuleProgress(moduleSlug) {
        console.log(`startModuleProgress(${moduleSlug})`)

        this.$apollo.mutate({
          mutation: START_MODULE_PROGRESS,
          variables: {
            username: 'test',
            moduleSlug: moduleSlug
          },
          update: (store, { data }) => {
            this.moduleBooked = data.startModuleProgress.created
          }
        }).then((data) => {
          // Result
          console.log(data)
        }).catch((error) => {
          // Error
          console.error(error)
          // We restore the initial user input
          // this.newTag = newTag
        })
      },

      deleteModuleProgress(moduleSlug) {
        console.log(`deleteModuleProgress(${moduleSlug})`)

        this.$apollo.mutate({
          mutation: DELETE_MODULE_PROGRESS,
          variables: {
            username: 'test',
            moduleSlug: moduleSlug
          },
          update: (store, { data }) => {
            this.moduleBooked = !data.deleteModuleProgress.deleted
          }
        }).then((data) => {
          // Result
          console.log(data)
        }).catch((error) => {
          // Error
          console.error(error)
          // We restore the initial user input
          // this.newTag = newTag
        })
      }
    },

    created() {
      this.$apollo.addSmartQuery('container', {
        query: MODULE_QUERY,
        variables: {
          slug: this.slug,
          username: 'test'
        },
        fetchPolicy: 'network-only',
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
            console.log(`Module Booked: ${this.moduleBooked}`)
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
