import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

export default new Vuex.Store({
  state: { // = data
    userId: null,
    moduleId: null,
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

    newFocusWizardState({ state, commit }, newState) {
      commit('setFocusWizardState', newState)
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
