import apolloClient from '@/graphql/client'
import USER_QUERY from '@/graphql/gql/user.gql'

export default {
  state: {
    user: {}
  },

  mutations: {
    setUser(state, user) {
      state.user = user
    }
  },

  actions: {
    async fetchUser({ state, commit }) {
      const { data: { user } } = await apolloClient.query({
        query: USER_QUERY
      });
      commit('setUser', user);
    }
  },

  getters: {
    getUser: state => state.user
  }
}
