<template>
  <div>
    <p></p>

    <FokusStart v-on:proceed="proceedAfterStart($event)" v-if="isFokusStart"></FokusStart>
    <FokusDetail v-on:proceed="proceedAfterDetail($event)" v-if="isFokusDetail"></FokusDetail>
    <FokusFinish v-on:proceed="proceedAfterFinish($event)" v-if="isFokusFinish"></FokusFinish>

  </div>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  import FokusStart from '@/components/fokus/FokusStart'
  import FokusDetail from '@/components/fokus/FokusDetail'
  import FokusFinish from '@/components/fokus/FokusFinish'

  export default {
    name: 'page-fokus',

    components: {
      FokusDetail,
      FokusStart,
      FokusFinish
    },

    data() {
      return {
        module: null,
        moduleBooked: false
      }
    },

    computed: {
      ...mapGetters({
        userFokusState: 'userFokusState',
        isFokusStart: 'isFokusStart',
        isFokusDetail: 'isFokusDetail',
        isFokusFinish: 'isFokusFinish'
      })
    },

    methods: {
      ...mapActions({
        newFokusWizardState: 'newFokusWizardState'
      }),

      proceedAfterStart() {
        this.newFokusWizardState('detail')
      },

      proceedAfterDetail() {
        this.newFokusWizardState('finish')
      },

      proceedAfterFinish() {
        this.newFokusWizardState('start')
        this.$router.push('development')
      }
    }
  }
</script>

<style lang="scss" scoped>
</style>
