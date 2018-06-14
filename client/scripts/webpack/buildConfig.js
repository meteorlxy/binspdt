const merge = require('webpack-merge')
const utils = require('../utils')
const webpackBaseConfig = require('./baseConfig')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')

const webpackBuildConfig = merge(webpackBaseConfig, {
  mode: 'production',
  devtool: false,
  optimization: {
    splitChunks: {
      maxInitialRequests: 10,
      cacheGroups: {
        element: {
          test: /[\\/]node_modules[\\/]element\-ui[\\/]/,
          name: 'vendor.element',
          chunks: 'all'
        },
        vue: {
          test: /[\\/]node_modules[\\/](vue|vue-router|vuex)[\\/]/,
          name: 'vendor.vue',
          chunks: 'all'
        },
        commons: {
          test: /[\\/]node_modules[\\/]/,
          priority: -10,
          name: 'vendor.commons',
          chunks: 'all'
        }
      }
    }
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: utils.path.assets('css/styles.[chunkhash:8].css')
    }),
    
    new OptimizeCssAssetsPlugin({
      canPrint: false,
      cssProcessorOptions: {
        safe: true,
        autoprefixer: { disable: true },
        mergeLonghand: false
      }
    })
  ]
})

module.exports = webpackBuildConfig
