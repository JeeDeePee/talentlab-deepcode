<template>
  <div class="pa-2">
      <h3>{{title}}</h3>

      <div v-for="(item, index) in tools" v-bind:key="index" class="mb-1">
        <a target="_blank" v-bind:href="item.value.url ? item.value.url: item.value.document">{{item.value.description}}</a>
        <hr>
      </div>
  </div>
</template>

<script>
  export default {
    name: 'tools',
    props: {
      tools: {
        required: true,
        type: Array
      },
      title: {
        required: true,
        type: String
      }
    }
  }
</script>
