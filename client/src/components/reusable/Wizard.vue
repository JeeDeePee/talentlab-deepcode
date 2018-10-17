<template>
  <v-layout row justify-center>
    <v-dialog v-model='show' fullscreen hide-overlay>
      <v-card class="background--beige">

        <v-card-actions class="dialog--header px-0 mx-4">

          <v-breadcrumbs>
            <v-icon slot='divider'>chevron_right</v-icon>
            <v-breadcrumbs-item v-for='step in processSteps'
                                :key='step.text'
                                :disabled='step.disabled'
                                class='breadcrumbs-item'>
              {{ step.text }}
            </v-breadcrumbs-item>
          </v-breadcrumbs>

          <v-spacer></v-spacer>

          <v-btn large flat icon @click.stop='show=false'>
            <v-icon class="text--orange">close</v-icon>
          </v-btn>
        </v-card-actions>


        <v-container grid-list-xl class='dialog--content'>
          <slot></slot>
        </v-container>
      </v-card>
    </v-dialog>
  </v-layout>
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
