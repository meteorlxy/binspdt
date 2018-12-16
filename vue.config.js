const path = require('path')
const CopyWebpackPlugin = require('copy-webpack-plugin')

const pathResolve = (...args) => path.resolve(__dirname, ...args)

module.exports = {
  outputDir: pathResolve('client/public'),

  assetsDir: 'static',

  lintOnSave: process.env.NODE_ENV === 'development',

  configureWebpack: {
    plugins: [
      new CopyWebpackPlugin([{
        from: pathResolve('client/src/assets/public'),
        to: pathResolve('client/public'),
      }]),
    ],
  },

  chainWebpack: config => {
    config.resolve.alias
      .set('@', pathResolve('client/src'))

    config
      .plugin('html')
      .tap(args => {
        args[0].template = pathResolve('client/src/index.html')
        return args
      })

    if (process.env.NODE_ENV === 'development') {
      config.module
        .rule('eslint')
        .use('eslint-loader')
        .loader('eslint-loader')
        .tap(options => {
          options.fix = true
          return options
        })
    }
  },

  devServer: {
    proxy: {
      '^/api': {
        target: process.env.API_HOST,
        ws: true,
        changeOrigin: true,
      },
    },
  },
}
