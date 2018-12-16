import {
  decToHex,
} from '@/utils/helpers'

export default [
  {
    name: 'id',
    text: 'Basic Block ID',
  },

  {
    name: 'address',
    text: 'Basic Block Address',
    formatter: decToHex,
  },

  {
    name: 'parent_function',
    text: 'Parent Function Address',
    formatter: decToHex,
  },
]
