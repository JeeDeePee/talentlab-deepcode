import apolloClient from '@/graphql/client'
import MODULE_GOALS_QUERY from '@/graphql/gql/moduleGoals/moduleGoalsQuery.gql'

const moduleGoalWizard = {
  state: {
    moduleGoals: []
  },

  mutations: {
    setModuleGoals(state, moduleGoals) {
      state.moduleGoals = moduleGoals
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
    }
  },

  getters: {
    getModuleGoals: state => state.moduleGoals
  }
}

export default moduleGoalWizard
