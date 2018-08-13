import apolloClient from '../../../graphql/client';
import USER_FOCUS from '@/graphql/gql/focus/userFocus.gql'

export default {
  state: {
    userFocus: []
  },

  mutations: {
    setUserFocus(state, userFocus) {
      state.userFocus = userFocus
    }
  },

  actions: {
    async fetchUserFocus({state, commit}) {
      const response = await apolloClient.query({
        query: USER_FOCUS,
        fetchPolicy: 'network-only'
      });
      if (response.data.userFocus && response.data.userFocus.edges.length > 0) {
        let result = response.data.userFocus.edges.reduce(
          (a, b) => a.concat(b.node.competenceentrySet.edges.map(x => x.node)), []
        );
        console.info(result)
        commit('setUserFocus', result);
      }
    }
  },
  getters: {
    getUserFocus: state => state.userFocus
  }
}
