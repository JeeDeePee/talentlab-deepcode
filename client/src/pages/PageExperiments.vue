<template>
  <div>
    <!--<h1 class="text-xs-center">Dashboard</h1>-->

    <v-container fluid grid-list-xl>
      <v-layout row wrap>

        <TextBox message="Message" v-on:save="save"></TextBox>
        <TextBox message="Feedback" v-on:save="save"></TextBox>
        <TextBox message="FooBar" v-on:save="save"></TextBox>

      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import TextBox from '@/components/reusable/TextBox'

  export default {
    components: {
      TextBox
    },

    data() {
      return {
        title: 'Hi,\nI just wanted to check in and see if you had any plans the upcoming weekend. We are thinking of heading up to Napa'
      }
    },

    methods: {
      save(text) {
        console.log(`client is saving.. text: ${text}`)
      }
    }
  }
</script>
<style lang="scss" scoped>
  @import "../styles/var";
</style>
