
const moduleGoalWizard = {
  state: {
    moduleGoalWizard: 'my-motivation'
  },

  mutations: {
    setModuleGoalWizardState(state, moduleGoalState) {
      state.moduleGoalWizard = moduleGoalState
    }
  },

  actions: {
    newModuleGoalWizardState_MyMotivation({ state, commit }) {
      commit('setModuleGoalWizardState', 'my-motivation')
    },

    newModuleGoalWizardState_MyGoal({ state, commit }) {
      commit('setModuleGoalWizardState', 'my-goal')
    }
  },

  getters: {
    isMyMotivation(state, getters) {
      return state.moduleGoalWizard === 'my-motivation'
    },

    isMyGoal(state, getters) {
      return state.moduleGoalWizard === 'my-goal'
    }
  }
}

export default moduleGoalWizard
