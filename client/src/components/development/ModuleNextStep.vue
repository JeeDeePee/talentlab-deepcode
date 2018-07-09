<template>
  <div>
    <div class="mb-1">
      <h5>{{ unitProgress.type }}: {{ unitProgress.title }}</h5>
      <h6>> Nächste Lektion starten</h6>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'module-next-step',

    props: {
      unitProgress: {
        required: true,
        type: Object
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "../../styles/var";

  img {
    max-width: 100%;
  }

  h5 {
    border-top: 1px solid $grey-2;
    font-size: 15px;
    font-weight: 400;
    padding-top: 5px;
    max-width: 320px;
  }

  h6 {
    font-size: 15px;
    font-weight: bold;
    padding-bottom: 10px;
  }
</style>
