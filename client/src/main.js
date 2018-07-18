import 'babel-polyfill'
import Vue from 'vue'
import 'vuetify/dist/vuetify.min.css'
import Vuetify from 'vuetify'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueApollo from 'vue-apollo'
import lodash from 'lodash'
import VueVimeoPlayer from 'vue-vimeo-player'
import VueIntercom from 'vue-intercom'

import App from './App'
import router from './router'
import apolloClient from './graphql/client'
import store from '@/store/index'

Vue.config.productionTip = false

Object.defineProperty(Vue.prototype, '$lodash', { value: lodash })

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

Vue.use(VueApollo)
Vue.use(VueAxios, axios)
Vue.use(Vuetify)
Vue.use(VueVimeoPlayer)
Vue.use(VueIntercom, { appId: 'aec9le28' })

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  provide: apolloProvider.provide(),
  render: h => h(App)
})
