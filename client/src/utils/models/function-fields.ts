import {
  decToHex,
} from '@/utils/helpers'

export default [
  {
    name: 'address',
    text: 'Function Address',
    formatter: decToHex,
  },

  {
    name: 'name',
    text: 'Function Name',
  },

  {
    name: 'demangled_name',
    text: 'Demangled Name',
  },

  {
    name: 'has_real_name',
    text: 'Has Real Name',
  },

  {
    name: 'type',
    text: 'Type',
  },

  {
    name: 'module_name',
    text: 'Module Name',
  },

  {
    name: 'stack_frame',
    text: 'Stack Frame',
  },

  {
    name: 'prototype',
    text: 'Prototype',
  },
]
