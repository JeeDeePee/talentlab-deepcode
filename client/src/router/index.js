import Vue from 'vue'
import Router from 'vue-router'
import Categories from '@/pages/PageCategories'
import Container from '@/pages/PageContainer'
import Development from '@/pages/PageDevelopment'
import Dashboard from '@/pages/PageDashboard'
import NotFound from '@/pages/PageNotFound'

const routerOptions = [
  { path: '/', name: 'categories', component: Categories },
  { path: '/container/:slug', name: 'container', component: Container, props: true },
  { path: '/dashboard', name: 'dashboard', component: Dashboard },
  { path: '/development', name: 'development', component: Development },
  { path: '*', component: NotFound }
]
const routes = routerOptions.map(route => {
  return {
    ...route
    // TODO: nice..
    // component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
