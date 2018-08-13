import apolloClient from '../../../graphql/client';
import USER_FOCUS from '@/graphql/gql/focus/userFocus.gql'

export default {
  state: {
    userFocus: [],
    userFocusCreated: null
  },

  mutations: {
    setUserFocus(state, userFocus) {
      state.userFocus = userFocus
    },
    setUserFocusCreated(state, created) {
      state.userFocusCreated = new Date(created)
    }
  },

  actions: {
    async fetchUserFocus({state, commit}) {
      const response = await apolloClient.query({
        query: USER_FOCUS,
        fetchPolicy: 'network-only'
      });
      var created;
      if (response.data.userFocus && response.data.userFocus.edges.length > 0) {
        let result = response.data.userFocus.edges.reduce(
          function (a, b) {
            created = b.node.created;
            return a.concat(b.node.competenceentrySet.edges.map(x => x.node))
          }, []);
        commit('setUserFocus', result);
        commit('setUserFocusCreated', created);
      }
    }
  },
  getters: {
    getUserFocus: state => state.userFocus,
    getUserFocusCreated: state => state.userFocusCreated
  }
}
