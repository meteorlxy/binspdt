import {
  decToHex,
} from '@/utils/helpers'

export default [
  {
    name: 'address',
    text: 'Instruction Address',
    formatter: decToHex,
  },

  {
    name: 'mnemonic',
    text: 'Mnemonic',
  },
]
