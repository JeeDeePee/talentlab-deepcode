import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  {path: '/', name: 'start', component: 'PageStart'},
  {path: '/modules', name: 'modules', component: 'PageModules'},
  {path: '/module/:slug', name: 'module', component: 'PageModule', props: true},
  {path: '/unit/:slug', name: 'unit', component: 'PageUnit', props: true},
  {path: '/development', name: 'development', component: 'PageDevelopment'},
  {path: '/experiments', name: 'experiments', component: 'PageExperiments'},
  {path: '/coaching', name: 'coaching', component: 'PageCoaching'},
  {
    path: '/login',
    name: 'login',
    beforeEnter() {
      location.href = '/accounts/login/?next=/development'
    }
  },
  {
    path: '/logout',
    name: 'logout',
    beforeEnter() {
      location.href = '/logout/'
    }
  },
  {path: '*', component: 'NotFound'}
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/pages/${route.component}.vue`)
  }
})

Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
