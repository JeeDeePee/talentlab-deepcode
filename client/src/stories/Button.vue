<template>
  <div>
    <button class="wr-button" :style="{color: color, borderColor: color}" @click="handleClick" :class="{rounded: rounded}"><slot></slot>!</button>
    <v-btn>hello</v-btn>
  </div>
</template>

<script>
  export default {
    props: {
      rounded: Boolean,
      handleClick: {
        default: () => () => null
      },
      color: {
        default: '#42b983'
      }
    }
  };
</script>

<style lang="scss" scoped>
  @import "../styles/main";

  .rounded {
    border-radius: 10px;
  }

  .wr-button {
    border: 3px solid;
    padding: 10px 20px;
    background-color: white;
    outline: none;
  }
</style>
