import apolloClient from '../../../graphql/client';
import FOCUS_COMPETENCE_QUERY from '@/graphql/gql/focus/focusCompetences.gql'
import CREATE_FOCUS_COMPETENCE_QUERY from '@/graphql/gql/focus/createFocus.gql'

export default {
  state: {
    focusCompetences: {},
    focuslWizardState: 'determine',
    focusCache: []
  },

  mutations: {
    addToFocusCache(state, focus) {
      state.focusCache.push({
        title: focus.title,
        slug: focus.slug,
        currentLevel: null,
        nextEvaluation: null,
        selected: false
      })
    },
    setFocusCompetences(state, focusCompetences) {
      state.focusCompetences = focusCompetences
    },
    setFocusWizardState(state, focuslWizardState) {
      state.focuslWizardState = focuslWizardState
    },
    setUserFocusBySlugs(state, userFocus) {
      state.focusCache = state.focusCache.map(x => {
        x.selected = userFocus.indexOf(x.slug) > -1
        return x
      })
    },
    setUserFocus(state, userFocus) {
      for (const focus of userFocus) {
        state.focusCache[state.focusCache.findIndex(x => x.slug === focus.slug)] = {
          ...state.focusCache[focus.slug], ...focus
        }
      }
    }
  },

  actions: {
    async fetchFocusCompetences({state, commit}) {
      const response = await apolloClient.query({
        query: FOCUS_COMPETENCE_QUERY
      });

      let items = response.data.categories.edges.map(category => ({
          title: category.node.title,
          teaser: 'Gewinne Leichtigkeit im Umgang mit Veränderungen',
          competences: category.node.competenceSet.edges.map(
            function (compentence) {
              commit('addToFocusCache', compentence.node);
              return {
                title: compentence.node.title,
                slug: compentence.node.slug
              }
            })
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
                  'entries': state.focusCache.filter(x => x.selected).map(x => ({
                    slug: x.slug,
                    currentLevel: x.currentLevel,
                    nextEvaluation: x.nextEvaluation
                  }))
                }
            }
        }
      })
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
    getUserFocusSlugs: state => state.focusCache.filter(x => x.selected).map(x => x.slug),
    getUserFocus: state => state.focusCache.filter(x => x.selected),
    isMyFocus: state => state.focuslWizardState === 'my-focus',
    isDetermineFocus: state => state.focuslWizardState === 'determine'
  }
}
