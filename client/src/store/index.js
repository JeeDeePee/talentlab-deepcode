import Vuex from 'vuex'
import Vue from 'vue'
import focusWizard from '@/store/module/focus/FocusWizard'
import userFocus from '@/store/module/focus/UserFocus'
import moduleGoalWizard from '@/store/module/goal/ModuleGoalWizard'
import actionPlanWizard from '@/store/module/actionplan/ActionPlanWizard'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    focusWizard: focusWizard,
    userFocus: userFocus,
    moduleGoalWizard: moduleGoalWizard,
    actionPlanWizard: actionPlanWizard
  },

  state: {},

  getters: {},

  actions: {},

  mutations: {}
})
