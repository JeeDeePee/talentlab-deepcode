<template>
  <v-dialog v-model='show' fullscreen hide-overlay transition='dialog-bottom-transition' scrollable>
    <v-card v-bind:class='wizzardClasses'>

      <v-toolbar v-if="wizardName" dark color='primary' class='ml-4 mr-4'>
        <v-toolbar-title>{{ wizardName }}</v-toolbar-title>
        <div class='toolbar-accent'></div>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn large flat icon @click.stop='show=false'>
            <v-icon>close</v-icon>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>

      <div v-else>
        <v-btn large flat icon @click.stop='show=false' style="float: right">
          <v-icon>close</v-icon>
        </v-btn>
      </div>

      <v-breadcrumbs class='ml-4 mr-4'>
        <v-icon slot='divider'>chevron_right</v-icon>
        <v-breadcrumbs-item v-for='step in processSteps'
                            :key='step.text'
                            :disabled='step.disabled'
                            class='breadcrumbs-item'>
          {{ step.text }}
        </v-breadcrumbs-item>
      </v-breadcrumbs>

      <v-container fluid grid-list-xl class='dialog--content'>
        <slot></slot>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
  export default {
    props: ['value', 'wizardName', 'processSteps', 'theme'],

    computed: {
      wizzardClasses: function () {
        return (this.theme === 'light' ? 'dialog-light' : 'background--violet')
      },

      show: {
        get() {
          return this.value
        },
        set(value) {
          if (!value) {
            this.$emit('close')
          }
        }
      }
    }
  }
</script>

<style lang='scss' scoped>
  .mygoal--selection {
    height: 100%;
  }
</style>
