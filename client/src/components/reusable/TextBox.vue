<template>
  <div class="text-area">
    <v-textarea
      :label="message"
      class="background--white"
      @input="handleInput"
      v-model="content"
      auto-grow
      full-width
      single-line
      hide-details
      :placeholder="placeholder">
    </v-textarea>
    <v-icon class="edit">edit</v-icon>
  </div>
</template>

<script>
  export default {
    props: ['message', 'value', 'placeholder'],

    data() {
      return {
        content: this.value
      }
    },

    // TODO: review is this really necessary to implement reactivity into custom components with v-model?
    watch: {
      value() {
        this.content = this.value
      }
    },

    methods: {
      handleInput() {
        this.$emit('input', this.content)
      }
    }
  }
</script>

<style lang="scss" scoped>

  .text-area {
    position: relative;
  }

  .edit {
    position: absolute;
    top: 10px;
    right: 10px;
  }
</style>
