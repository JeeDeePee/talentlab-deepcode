
export default {
  state: {
    actionPlanWizardState: 'StartActionPlan'
  },

  mutations: {
    setActionPlanWizardState(state, actionPlanWizardState) {
      state.actionPlanWizardState = actionPlanWizardState
    }
  },

  actions: {
    newActionPlanWizardState({state, commit}, newState) {
      commit('setActionPlanWizardState', newState)
    }
  },

  getters: {
    getActionPlanWizardState: state => state.actionPlanWizardState
    // isCurrentWizardState: uiState => state => uiState === state.actionPlanWizardState
  }
}
