import Vuex from 'vuex'
import Vue from 'vue'
import apolloClient from '../graphql/client'
import FOCUS_COMPETENCE_QUERY from '@/graphql/gql/focus/focusCompetences.gql'

import moduleGoalWizard from '@/store/module/goal/ModuleGoalWizard'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    moduleGoalWizard: moduleGoalWizard
  },

  state: { // = data
    userid: null,
    username: null,
    moduleId: null,
    focus: [],
    userState: {
      focus: {
        state: 'determine'
      }
    }
  },

  getters: { // = computed properties
    userFocusState(state, getters) {
      return state.userState.focus.state
    },

    isMyFocus(state, getters) {
      return state.userState.focus.state === 'my-focus'
    },

    isDetermineFocus(state, getters) {
      return state.userState.focus.state === 'determine'
    },

    getFocus(state, getters) {
      return state.focus
    }
  },

  actions: { // = methods

    async fetchFocusCompetences({commit}) {
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

      console.info(items);
    },

    fetchUserProgress({commit}) {
      return new Promise((resolve, reject) => {
        // debugger

        // shop.getProducts(products => {
        //   commit('setProducts', products);
        //   resolve();
        // })
      })
    },

    startModuleProgress({state, commit}, moduleId) {
      // debugger

      // call graphql createUserModuleMutation

      // mutation createUserModuleMutation {
      //   createUserModule(moduleId:"anotherFooBar123") {
      //     ok
      //     moduleId
      //   }
      // }
    },

    deleteModuleProgress({state, commit}, moduleId) {
      // debugger

      // call graphql createUserModuleMutation

      // mutation createUserModuleMutation {
      //   createUserModule(moduleId:"anotherFooBar123") {
      //     ok
      //     moduleId
      //   }
      // }
    },

    newFocusWizardState({state, commit}, newState) {
      commit('setFocusWizardState', newState)
    },

    setFocus({state, commit}, focus) {
      commit('mutateFocus', focus)
    }

    // fetchProducts({ commit }) {
    //   return new Promise((resolve, reject) => {
    //     shop.getProducts(products => {
    //       commit('setProducts', products);
    //       resolve();
    //     })
    //   })
    // },

    // addProductToCart({ state, getters, commit }, product) {
    //   if (getters.productIsInStock(product)) {
    //     const cartItem = state.cart.find(item => item.id === product.id);
    //     if (!cartItem) {
    //       commit('pushProductToCart', product.id)
    //     } else {
    //       commit('incrementItemQuantity', cartItem)
    //     }
    //   }
    //   commit('decrementProductInventory', product)
    // },

    // checkout({ state, commit }) {
    //   shop.buyProducts(state.cart,
    //     () => {
    //       commit('emptyCart');
    //       commit('setCheckoutStatus', 'success')
    //     },
    //     () => {
    //       commit('setCheckoutStatus', 'fail')
    //     })
    // }
  },

  mutations: {
    setUserState(state, userState) {
      state.userState = userState
    },

    setFocusWizardState(state, focusState) {
      state.userState.focus.state = focusState
    },

    mutateFocus(state, focus) {
      state.focus = focus
    }

    // setProducts(state, products) {
    //   // update products
    //   state.products = products;
    // },
    //
    // pushProductToCart(state, productId) {
    //   state.cart.push({ id: productId, quantity: 1 })
    // },
    //
    // incrementItemQuantity(state, cartItem) {
    //   cartItem.quantity++;
    // },
    //
    // decrementProductInventory(state, product) {
    //   product.inventory--;
    // },
    //
    // setCheckoutStatus(state, status) {
    //   state.checkoutStatus = status
    // },
    //
    // emptyCart(state) {
    //   state.cart = []
    // }
  }
})
