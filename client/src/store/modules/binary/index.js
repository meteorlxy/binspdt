import modulesModule from './modules'
import resultsModule from './results'

const binaryModule = {
  namespaced: true,

  modules: {
    modules: modulesModule,
    results: resultsModule
  }
}

export default binaryModule
