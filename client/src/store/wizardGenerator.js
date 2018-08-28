
export default function wizardGenerator(wizardName, defaultWizardStep) {
  let state = {}
  state[`${wizardName}WizardState`] = defaultWizardStep

  let mutations = {}
  mutations[`set${wizardName}WizardState`] = function(state, wizardState) {
    state[`${wizardName}WizardState`] = wizardState
  }

  let actions = {}
  actions[`new${wizardName}WizardState`] = function({state, commit}, newState) {
    commit(`set${wizardName}WizardState`, newState)
  }

  let getters = {}
  getters[`get${wizardName}WizardState`] = state => state[`${wizardName}WizardState`]

  return {
    state: state,
    mutations: mutations,
    actions: actions,
    getters: getters
  }
}
