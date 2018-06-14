import module from './module'
import analysis from './analysis'

const binary = {
  namespaced: true,
  modules: {
    module,
    analysis
  }
}

export default binary
