import Vuex from 'vuex'
import Vue from 'vue'
import focusWizard from '@/store/module/focus/FocusWizard'
import userFocus from '@/store/module/focus/UserFocus'
import moduleGoalWizard from '@/store/module/goal/ModuleGoalWizard'
import wizardGenerator from '@/store/wizardGenerator';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    focusWizard: focusWizard,
    userFocus: userFocus,
    moduleGoalWizard: moduleGoalWizard,
    actionPlanWizard: wizardGenerator('ActionPlan', 'StartActionPlan')
  },

  state: {},

  getters: {},

  actions: {},

  mutations: {}
})
