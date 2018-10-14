<template>
  <div>

    <v-list class="background--transparent v-list--adjust pa-0">
      <div v-for="(item,i) in items" :key="i">
        <v-list-tile class="module--list-tile">
          <v-list-tile-action class="module--list-action">
            <v-icon v-if="item.type==='calendar'" class="material-icons text--orange">calendar_today</v-icon>
            <v-icon v-else-if="item.type==='message'" if="item.type=='calendar'"
                    class="material-icons text--orange">
              mail_outline
            </v-icon>
            <v-icon class="material-icons text--orange" v-else>link</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-sub-title class="text--light">{{item.text}}</v-list-tile-sub-title>
          </v-list-tile-content>
        </v-list-tile>
      </div>
    </v-list>

  </div>
</template>

<script>
  export default {
    props: ['items']
  }
</script>


<style lang="scss" scoped>
  @import "../../styles/var";

  .module--list-action {
    min-width: initial;
    padding-right: 10px;
  }

  .module--list-tile {
    border-bottom: 1px solid $orange;
  }


</style>
