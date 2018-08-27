import apolloClient from '@/graphql/client'
import MODULE_GOALS_QUERY from '@/graphql/gql/moduleGoals/moduleGoalsQuery.gql'

export default {
  state: {
    moduleGoals: [],
    currentGoal: {
      level: -1
    }
  },

  mutations: {
    setModuleGoals(state, moduleGoals) {
      state.moduleGoals = moduleGoals
    },
    setCurrentGoal(state, currentGoal) {
      state.currentGoal = currentGoal
    }
  },

  actions: {
    async fetchModuleGoals({state, commit}, {moduleSlug}) {
      const response = await apolloClient.query({
        query: MODULE_GOALS_QUERY,
        variables: {
          slug: moduleSlug
        }
      });

      const goals = response.data.module.goalSet.edges.map(goal => ({...goal.node}))
      commit('setModuleGoals', goals);

      if (response.data.allUserGoals.edges.length === 1) {
        const currentGoal = response.data.allUserGoals.edges[0].node.goal
        commit('setCurrentGoal', currentGoal);
      }
    }
  },

  getters: {
    getModuleGoals: state => state.moduleGoals,
    getCurrentGoal: state => state.currentGoal
  }
}
