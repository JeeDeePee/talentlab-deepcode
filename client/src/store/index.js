import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

export default new Vuex.Store({
  state: { // = data
    userid: null,
    username: null,
    moduleId: null,
    userState: {
      fokus: {
        state: 'start'
      }
    }
  },

  getters: { // = computed properties
    userFokusState(state, getters) {
      return state.userState.fokus.state
    },

    isFokusStart(state, getters) {
      return state.userState.fokus.state === 'start'
    },

    isFokusDetail(state, getters) {
      return state.userState.fokus.state === 'detail'
    },

    isFokusFinish(state, getters) {
      return state.userState.fokus.state === 'finish'
    }
  },

  actions: { // = methods
    fetchUserProgress({ commit }) {
      return new Promise((resolve, reject) => {
        // debugger

        // shop.getProducts(products => {
        //   commit('setProducts', products);
        //   resolve();
        // })
      })
    },

    startModuleProgress({ state, commit }, moduleId) {
      // debugger

      // call graphql createUserModuleMutation

      // mutation createUserModuleMutation {
      //   createUserModule(moduleId:"anotherFooBar123") {
      //     ok
      //     moduleId
      //   }
      // }
    },

    deleteModuleProgress({ state, commit }, moduleId) {
      // debugger

      // call graphql createUserModuleMutation

      // mutation createUserModuleMutation {
      //   createUserModule(moduleId:"anotherFooBar123") {
      //     ok
      //     moduleId
      //   }
      // }
    },

    newFokusWizardState({ state, commit }, newState) {
      commit('setFokusWizardState', newState)
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

    setFokusWizardState(state, fokusState) {
      state.userState.fokus.state = fokusState
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
