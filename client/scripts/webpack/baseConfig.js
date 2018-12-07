const utils = require('../utils')
const webpack = require('webpack')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const VueLoaderPlugin = require('vue-loader/lib/plugin')

const webpackBaseConfig = {
  context: utils.path.root(),
  entry: {
    app: './src/main.js'
  },
  output: {
    path: utils.path.dist(),
    filename: utils.path.assets('js/[name].[chunkhash:8].js'),
    publicPath: '/'
  },
  resolve: {
    extensions: ['.js', '.vue'],
    alias: {
      '@': utils.path.src()
    }
  },
  module: {
    rules: [
      {
        enforce: 'pre',
        test: /\.(js|vue)$/,
        loader: 'eslint-loader',
        exclude: /node_modules/,
        options: {
          fix: true,
          formatter: require('eslint-friendly-formatter')
        }
      },

      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          // `vue-loader` options
        }
      },

      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: ['@vue/babel-preset-app']
            }
          }
        ]
      },

      {
        test: /\.css$/,
        use: [
          ...utils.useCommonStyleLoaders()
        ]
      },

      {
        test: /\.scss$/,
        use: [
          ...utils.useCommonStyleLoaders(),
          'sass-loader'
        ]
      },

      {
        test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/i,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.path.assets('fonts/[name].[hash:8].[ext]')
        }
      },

      {
        test: /\.(png|jpe?g|gif)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: utils.path.assets('img/[name].[hash:8].[ext]')
        }
      },

      {
        test: /\.(svg)(\?.*)?$/,
        loader: 'file-loader',
        options: {
          name: utils.path.assets('img/[name].[hash:8].[ext]')
        }
      }
    ]
  },
  plugins: [
    // Necessary for vue-loader v15+
    new VueLoaderPlugin(),

    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.html',
      inject: true
    }),

    // Copy the static files from static dir
    new CopyWebpackPlugin([
      {
        from: utils.path.root('static'),
        to: utils.path.dist('static'),
        ignore: ['.*']
      }
    ]),

    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    })
  ],
  node: {
    setImmediate: false,
    global: false,
    process: false,
    dgram: 'empty',
    fs: 'empty',
    net: 'empty',
    tls: 'empty',
    child_process: 'empty'
  }
}

module.exports = webpackBaseConfig
