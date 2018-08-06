import apolloClient from '../../../graphql/client';
import FOCUS_COMPETENCE_QUERY from '@/graphql/gql/focus/focusCompetences.gql'
import CREATE_FOCUS_COMPETENCE_QUERY from '@/graphql/gql/focus/createFocus.gql'

export default {
  state: {
    focusCompetences: {},
    userFocus: [],
    focuslWizardState: 'determine'
  },

  mutations: {
    setFocusCompetences(state, focusCompetences) {
      state.focusCompetences = focusCompetences
    },

    setFocusWizardState(state, focuslWizardState) {
      state.focuslWizardState = focuslWizardState
    },
    setUserFocusBySlugs(state, userFocus) {
      // @todo keep existing configs
      // @todo map title
      state.userFocus = userFocus.map(x => ({title: x, slug: x, currentLevel: null, nextEvaluation: null}))
    },
    setUserFocus(state, userFocus) {
      state.userFocus = userFocus
    }
  },

  actions: {
    async fetchFocusCompetences({commit}) {
      // @todo error handling
      const response = await apolloClient.query({
        query: FOCUS_COMPETENCE_QUERY
      });

      let items = response.data.categories.edges.map(category => ({
          title: category.node.title,
          teaser: 'Gewinne Leichtigkeit im Umgang mit Veränderungen',
          competences: category.node.competenceSet.edges.map(compentence => ({
                title: compentence.node.title,
                slug: compentence.node.slug
              }
            )
          )
        })
      );
      commit('setFocusCompetences', items);
    },
    async storeFocusCompetences({state, commit}) {
      // @todo error handling
      await apolloClient.mutate({
        mutation: CREATE_FOCUS_COMPETENCE_QUERY,
        variables: {
          'input':
            {
              'input':
                {
                  'entries': state.userFocus.map(x => ({
                    slug: x.slug,
                    currentLevel: x.currentLevel,
                    nextEvaluation: x.nextEvaluation
                  }))

                }
            }
        }
      });
    },
    newFocusWizardState({state, commit}, newState) {
      commit('setFocusWizardState', newState)
    },
    newUserFocusBySlugs({state, commit}, focus) {
      commit('setUserFocusBySlugs', focus)
    },
    newUserFocus({state, commit}, focus) {
      commit('setUserFocus', focus)
    }
  },

  getters: {
    getFocusCompetences: state => state.focusCompetences,
    getUserFocusSlugs: state => state.userFocus.map(x => x.slug),
    getUserFocus: state => state.userFocus,
    isMyFocus: state => state.focuslWizardState === 'my-focus',
    isDetermineFocus: state => state.focuslWizardState === 'determine'
  }
}
