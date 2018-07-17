import "vuetify/dist/vuetify.css"

import {configure} from '@storybook/vue'
import Vue from 'vue'
import Vuex from 'vuex'
import Vuetify from 'vuetify'

// Install Vue plugins.
Vue.use(Vuex)
Vue.use(Vuetify)

function loadStories() {
  // You can require as many stories as you need.
  require('../src/stories')
}

configure(loadStories, module);
