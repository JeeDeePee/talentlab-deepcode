import apolloClient from '@/graphql/client'
import MODULE_GOALS_QUERY from '@/graphql/gql/moduleGoals/moduleGoalsQuery.gql'

const moduleGoalWizard = {
  state: {
    moduleGoals: [],
    moduleGoalWizard: 'my-motivation'
  },

  mutations: {
    setModuleGoals(state, moduleGoals) {
      state.moduleGoals = moduleGoals
    },

    setModuleGoalWizardState(state, moduleGoalState) {
      state.moduleGoalWizard = moduleGoalState
    }
  },

  actions: {
    async fetchModuleGoals({state, commit}, { moduleSlug }) {
      const response = await apolloClient.query({
        query: MODULE_GOALS_QUERY,
        variables: {
          slug: moduleSlug
        }
      });

      const goals = response.data.modules.edges[0].node.goalSet.edges.map(goal => ({...goal.node}))
      commit('setModuleGoals', goals);
    },

    newModuleGoalWizardState_MyMotivation({ state, commit }) {
      commit('setModuleGoalWizardState', 'my-motivation')
    },

    newModuleGoalWizardState_MyGoal({ state, commit }) {
      commit('setModuleGoalWizardState', 'my-goal')
    }
  },

  getters: {
    getModuleGoals: state => state.moduleGoals,
    isMyMotivation: state => state.moduleGoalWizard === 'my-motivation',
    isMyGoal: state => state.moduleGoalWizard === 'my-goal'
  }
}

export default moduleGoalWizard
