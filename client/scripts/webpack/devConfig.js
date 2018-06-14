const merge = require('webpack-merge')
const webpackBaseConfig = require('./baseConfig')

const webpackDevConfig = merge(webpackBaseConfig, {
  mode: 'development',
  devtool: 'cheap-module-eval-source-map'
})

module.exports = webpackDevConfig
