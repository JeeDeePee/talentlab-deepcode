import 'babel-polyfill'
import Vue from 'vue'
import 'vuetify/dist/vuetify.min.css'
import Vuetify from 'vuetify'
import axios from 'axios'
import VueAxios from 'vue-axios'
import lodash from 'lodash'
import VueVimeoPlayer from 'vue-vimeo-player'
import VueIntercom from 'vue-intercom'
import apolloClient from './graphql/client'
import VueApollo from 'vue-apollo'
import App from './App'
import router from './router'
import store from '@/store/index'

Vue.config.productionTip = false

Object.defineProperty(Vue.prototype, '$lodash', { value: lodash })

Vue.use(VueApollo)

Vue.use(VueAxios, axios)
Vue.use(Vuetify)
Vue.use(VueVimeoPlayer)
Vue.use(VueIntercom, { appId: 'aec9le28' })

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  provide: apolloProvider.provide(),
  render: h => h(App)
})
