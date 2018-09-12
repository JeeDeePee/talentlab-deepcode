import 'babel-polyfill'
import 'vuetify/dist/vuetify.min.css'
import '@/styles/main.scss'
import Vue from 'vue'
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

// TODO: Move into a separate project
//
function getRidOfEdges(collection) {
  if (typeof collection === 'object' && collection) {
    let newObj = {}
    for (const k in collection) {
      if (k === 'edges') {
        return collection.edges.map(edge => getRidOfEdges(edge.node));
      } else {
        newObj[k] = getRidOfEdges(collection[k])
        if (newObj[k]) {
          delete newObj[k]['__typename']
        }
      }
    }
    return newObj
  } else {
    return collection
  }
}

Object.defineProperty(Vue.prototype, '$getRidOfEdges', {value: getRidOfEdges})
Object.defineProperty(Vue.prototype, '$lodash', {value: lodash})

Window.$getRidOfEdges = getRidOfEdges

Vue.use(VueApollo)
Vue.use(VueAxios, axios)

Vue.use(Vuetify, {
  theme: {
    primary: '#FD6E22',
    secondary: '#59006F'
  }
});

Vue.use(VueVimeoPlayer)
Vue.use(VueIntercom, {appId: 'aec9le28'})

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

Vue.filter('formatDate', function(value) {
  if (!value) return ''
  var m = value.getMonth() + 1;
  var d = value.getDate();
  return '' + (d < 10 ? '0' : '') + d + '.' + (m < 10 ? '0' : '') + m + '.' + value.getFullYear();
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  provide: apolloProvider.provide(),
  render: h => h(App)
})
