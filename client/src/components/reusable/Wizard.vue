<template>
  <v-dialog v-model="show" fullscreen hide-overlay transition="dialog-bottom-transition" scrollable>
    <v-card class="background--violet white--text">

      <v-toolbar dark color="primary" class="ml-4 mr-4">
        <v-toolbar-title>{{ wizardName }}</v-toolbar-title>
        <div class="toolbar-accent"></div>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn large flat icon @click.stop="show=false">
            <v-icon>close</v-icon>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>

      <v-breadcrumbs class="ml-4 mr-4">
        <v-icon slot="divider">chevron_right</v-icon>
        <v-breadcrumbs-item v-for="step in processSteps"
                            :key="step.text"
                            :disabled="step.disabled"
                            class="breadcrumbs-item">
          {{ step.text }}
        </v-breadcrumbs-item>
      </v-breadcrumbs>

      <v-container>
        <v-layout align-center justify-center row fill-height>
          <v-flex xs12>

            <!-- here come the wizard steps -->
            <slot></slot>

          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
  export default {
    props: ['value', 'wizardName', 'processSteps'],

    computed: {
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

<style scoped>
</style>
