import Vuex from 'vuex'
import Vue from 'vue'
import actionPlanData from '@/store/module/actionPlan/actionPlanData'
import focusWizard from '@/store/module/focus/FocusWizard'
import userFocus from '@/store/module/focus/UserFocus'
import user from '@/store/module/user/user'
import moduleGoalWizard from '@/store/module/goal/ModuleGoalWizard'
import wizardGenerator from '@/store/wizardGenerator';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    user: user,
    focusWizard: focusWizard,
    userFocus: userFocus,
    moduleGoalWizard: moduleGoalWizard,
    actionPlanData: actionPlanData,
    actionPlanWizard: wizardGenerator('ActionPlan', 'StartActionPlan')
  },

  state: {},

  getters: {},

  actions: {},

  mutations: {}
})
