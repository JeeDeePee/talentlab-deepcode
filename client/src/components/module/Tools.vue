<template>
  <div class="pa-2">
    <div v-for="(item, index) in tools" :key="index" class="pb-3 pt-3 tool-item">
      <v-icon v-if="item.type=='link'">link</v-icon>
      <v-icon v-else>insert_drive_file</v-icon>
      <a class="link" target="_blank" :href="item.value.url ? item.value.url: item.value.document">{{item.value.description}}</a>
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
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  a.link {
    color: $text-color;
  }

  .tool-item {
    border-top: 1px solid $grey-4;
  }
</style>
