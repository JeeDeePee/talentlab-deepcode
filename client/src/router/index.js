import Vue from 'vue'
import Router from 'vue-router'
import Categories from '@/pages/PageCategories'
import Containers from '@/pages/PageContainers'
import Container from '@/pages/PageContainer'
import About from '@/pages/PageAbout'
import NotFound from '@/pages/PageNotFound'

const routerOptions = [
  { path: '/', name: 'categories', component: Categories },
  { path: '/containers', name: 'containers', component: Containers },
  { path: '/container/:id', name: 'container', component: Container, props: true },
  { path: '/about', name: 'about', component: About },
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
