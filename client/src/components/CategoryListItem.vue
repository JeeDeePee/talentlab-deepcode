<template>
  <div class="forum-list">
    <h2 class="list-title">
      <router-link :to="{name: 'Category', params: {id: category['.key']}}">
        {{ category.name }}
      </router-link>
    </h2>
    <ForumList :forums="forums"/>
  </div>
</template>

<script>
  import sourceData from '@/data.json'
  import ForumList from '../components/ForumList'

  export default {
    name: 'category-list-item',
    components: {
      ForumList
    },

    props: {
      category: {
        required: true,
        type: Object
      }
    },

    computed: {
      forums() {
        // const forumIds = Object.values(category.forums)
        return Object.values(sourceData.forums).filter(forum => forum.id === this.category['.key'])
      }
    }
  }
</script>

<style scoped>

</style>
