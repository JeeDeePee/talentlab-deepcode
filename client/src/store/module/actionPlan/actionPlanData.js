import apolloClient from '../../../graphql/client';
import ACTION_PLAN_QUERY from '@/graphql/gql/actionPlan/actionPlanQuery.gql'
import DEFINE_ACTION_PLAN from '@/graphql/gql/progress/defineActionPlan.gql'

export default {
  state: {
    currentModule: {},
    moduleUserGoal: {},
    actionPlan: {}
  },

  mutations: {
    setCurrentModule(state, currentModule) {
      state.currentModule = currentModule
    },
    setModuleUserGoal(state, moduleUserGoal) {
      state.moduleUserGoal = moduleUserGoal
    },
    setActionPlan(state, actionPlan) {
      state.actionPlan = actionPlan
    }
  },

  actions: {
    async fetchModuleUserGoal({ state, commit }) {
      const { data: { moduleUserGoal, userProgress } } = await apolloClient.query({
        query: ACTION_PLAN_QUERY,
        fetchPolicy: 'network-only',
        variables: {
          slug: state.currentModule.slug
        }
      });

      if (moduleUserGoal.goal) {
        commit('setModuleUserGoal', moduleUserGoal.goal);
      }

      const actionPlan = Window.$getRidOfEdges(userProgress).usermoduleprogressSet[0]
      // debugger
      commit('setActionPlan', actionPlan)
    },
    newCurrentModule({ state, commit }, newCurrentModule) {
      commit('setCurrentModule', newCurrentModule)
    }
  },

  startModuleProgress({ state, commit }) {
    apolloClient.mutate({
      mutation: DEFINE_ACTION_PLAN,
      variables: {
        'input':
          {
            'moduleSlug': state.currentModule.slug,
            'measurementText': ''
          }
      }
    })
  },

  getters: {
    getCurrentModule: state => state.currentModule,
    getModuleUserGoal: state => state.moduleUserGoal,
    getActionPlan: state => state.actionPlan
  }
}
