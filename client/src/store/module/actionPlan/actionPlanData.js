import apolloClient from '../../../graphql/client';
import ACTION_PLAN_QUERY from '@/graphql/gql/actionPlan/actionPlanQuery.gql'

export default {
  state: {
    moduleUserGoal: {},
    currentModule: {}
  },

  mutations: {
    setModuleUserGoal(state, moduleUserGoal) {
      state.moduleUserGoal = moduleUserGoal
    },
    setCurrentModule(state, currentModule) {
      state.currentModule = currentModule
    }
  },

  actions: {
    async fetchModuleUserGoal({ state, commit }) {
      const { data: { moduleUserGoal } } = await apolloClient.query({
        query: ACTION_PLAN_QUERY,
        fetchPolicy: 'network-only',
        variables: {
          slug: state.currentModule.slug
        }
      });

      if (moduleUserGoal.goal) {
        commit('setModuleUserGoal', moduleUserGoal.goal);
      }
    },
    newCurrentModule({state, commit}, newCurrentModule) {
      commit('setCurrentModule', newCurrentModule)
    }
  },

  getters: {
    getModuleUserGoal: state => state.moduleUserGoal,
    getCurrentModule: state => state.currentModule
  }
}
