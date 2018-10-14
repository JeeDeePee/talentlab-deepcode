<template>
  <div>
    <div v-for="(item, index) in tools" :key="index" class="pb-3 pt-3 tool-item">
      <v-icon class="text--orange" v-if="item.type=='link'">link</v-icon>
      <v-icon class="text--orange" v-else>insert_drive_file</v-icon>
      <a class="text--light" target="_blank" :href="item.value.url ? item.value.url: item.value.document">{{item.value.description}}</a>
    </div>
  </div>
</template>

<script>
  export default {
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
    border-bottom: 1px solid $orange;
  }
</style>
