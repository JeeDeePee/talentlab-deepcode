import Vue from 'vue'
import Router from 'vue-router'
import StartPage from '@/pages/StartPage'
import Categories from '@/pages/PageCategories'
import Module from '@/pages/PageModule'
import Unit from '@/pages/PageUnit'
import Development from '@/pages/PageDevelopment'
import Dashboard from '@/pages/PageExperiments'
import NotFound from '@/pages/PageNotFound'

const routerOptions = [
  {path: '/', name: 'start', component: StartPage, meta: {showFooter: true}},
  {path: '/categories', name: 'categories', component: Categories, meta: {showFooter: true}},
  {path: '/module/:slug', name: 'module', component: Module, props: true},
  {path: '/unit/:slug', name: 'unit', component: Unit, props: true},
  {path: '/development', name: 'development', component: Development},
  {path: '/experiments', name: 'experiments', component: Dashboard},
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
  {path: '*', component: NotFound}
]

const routes = routerOptions.map(route => {
  return {
    ...route
    // TODO: maersu nice..
    // component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
