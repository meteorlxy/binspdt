const rm = require('rimraf')
const utils = require('./utils')

process.env.NODE_ENV = 'production'

rm(utils.path.dist(), err => {
  if (err) throw err
  process.argv.push('--progress', '--hide-modules', '--config', 'client/scripts/webpack/buildConfig.js')
  require('webpack-cli')
})
