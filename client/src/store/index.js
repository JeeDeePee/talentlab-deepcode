import Vuex from 'vuex'
import Vue from 'vue'
import focusWizard from '@/store/module/focus/FocusWizard'
import userFocus from '@/store/module/focus/UserFocus'
import moduleGoalWizard from '@/store/module/goal/ModuleGoalWizard'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    moduleGoalWizard: moduleGoalWizard,
    focusWizard: focusWizard,
    userFocus: userFocus
  },

  state: {},

  getters: {},

  actions: {},

  mutations: {}
})
