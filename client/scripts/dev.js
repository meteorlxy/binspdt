const rm = require('rimraf')
const utils = require('./utils')

process.env.NODE_ENV = 'development'

rm(utils.path.dist(), err => {
  if (err) throw err
  process.argv.push('--watch', '--progress', '--hide-modules', '--config', 'client/scripts/webpack/devConfig.js')
  require('webpack-cli')
})
