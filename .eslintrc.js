module.exports = {
  root: true,

  parserOptions: {
    parser: 'babel-eslint',
  },

  extends: [
    'plugin:vue/strongly-recommended',
    'standard',
  ],

  rules: {
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'comma-dangle': ['error', 'always-multiline'],
  },

  globals: {
    '$': true,
  },
}
