import apolloClient from '../../../graphql/client';
import ACTION_PLAN_QUERY from '@/graphql/gql/actionPlan/actionPlanQuery.gql'

export default {
  state: {
    moduleUserGoal: {}
  },

  mutations: {
    setModuleUserGoal(state, moduleUserGoal) {
      state.moduleUserGoal = moduleUserGoal
    }
  },

  actions: {
    async fetchModuleUserGoal({state, commit}) {
      const {data: {moduleUserGoal}} = await apolloClient.query({
        query: ACTION_PLAN_QUERY,
        fetchPolicy: 'network-only',
        variables: {
          slug: 'partnering-for-success'
        }
      });

      if (moduleUserGoal.goal) {
        commit('setModuleUserGoal', moduleUserGoal.goal);
      }
    }
  },

  getters: {
    getModuleUserGoal: state => state.moduleUserGoal
  }
}
