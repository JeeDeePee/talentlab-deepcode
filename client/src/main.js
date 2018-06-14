import Vue from 'vue'
import VueApollo from 'vue-apollo'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import apolloClient from './graphql/client'
import axios from 'axios'
import VueAxios from 'vue-axios'
import lodash from 'lodash'

Vue.config.productionTip = false

Object.defineProperty(Vue.prototype, '$lodash', {value: lodash})

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

Vue.use(VueApollo)
Vue.use(VueAxios, axios)
Vue.use(Vuetify)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  provide: apolloProvider.provide(),
  render: h => h(App)
})
