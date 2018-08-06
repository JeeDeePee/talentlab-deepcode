import Vuex from 'vuex'
import Vue from 'vue'
import focusWizard from '@/store/module/focus/FocusWizard'
import moduleGoalWizard from '@/store/module/goal/ModuleGoalWizard'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    moduleGoalWizard: moduleGoalWizard,
    focusWizard: focusWizard
  },

  state: {
    userid: null,
    username: null
  },

  getters: {},

  actions: {},

  mutations: {}
})
