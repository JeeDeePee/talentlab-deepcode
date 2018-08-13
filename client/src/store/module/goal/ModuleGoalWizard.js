import apolloClient from '@/graphql/client'
import MODULE_GOALS_QUERY from '@/graphql/gql/moduleGoals/moduleGoalsQuery.gql'

const moduleGoalWizard = {
  state: {
    moduleGoalWizard: 'my-motivation'
  },

  mutations: {
    setModuleGoals(state, moduleGoals) {
      debugger
      state.moduleGoals = moduleGoals
    },

    setModuleGoalWizardState(state, moduleGoalState) {
      state.moduleGoalWizard = moduleGoalState
    }
  },

  actions: {
    async fetchModuleGoals({state, commit}, { moduleSlug }) {
      debugger
      const response = await apolloClient.query({
        query: MODULE_GOALS_QUERY,
        variables: {
          slug: moduleSlug
        }
      });

      // let items = response.data.modules.edges.map(module => ({
      //     title: category.node.title,
      //     teaser: 'Gewinne Leichtigkeit im Umgang mit Veränderungen',
      //     competences: category.node.competenceSet.edges.map(
      //       function (compentence) {
      //         commit('addToFocusCache', compentence.node);
      //         return {
      //           title: compentence.node.title,
      //           slug: compentence.node.slug
      //         }
      //       })
      //   })
      // );

      // for (const moduleNode of response.data.modules.edges) {
      //   console.log(moduleNode)
      // }

      debugger
      let goals = response.data.modules.edges.map(module => (
        module.goalSet.edges.map(goal => goal.node)
      ))

      //  module.goalSet.edges.map(goal => return {...goal})
      // )

      commit('setModuleGoals', goals !== undefined ? goals : {});
    },

    newModuleGoalWizardState_MyMotivation({ state, commit }) {
      commit('setModuleGoalWizardState', 'my-motivation')
    },

    newModuleGoalWizardState_MyGoal({ state, commit }) {
      commit('setModuleGoalWizardState', 'my-goal')
    }
  },

  getters: {
    isMyMotivation: state => state.moduleGoalWizard === 'my-motivation',
    isMyGoal: state => state.moduleGoalWizard === 'my-goal'
  }
}

export default moduleGoalWizard
