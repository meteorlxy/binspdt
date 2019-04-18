import {
  decToHex,
  formatDateTime,
} from '@/utils/helpers'

export default [
  {
    name: 'id',
    text: 'Module ID',
  },

  {
    name: 'name',
    text: 'Module Name',
  },

  {
    name: 'architecture',
    text: 'Architecture',
  },

  {
    name: 'import_time',
    text: 'Upload Time',
    formatter: formatDateTime,
  },

  {
    name: 'base_address',
    text: 'Base Address',
    formatter: decToHex,
  },

  {
    name: 'md5',
    text: 'MD5',
  },

  {
    name: 'sha1',
    text: 'SHA1',
  },

  {
    name: 'exporter',
    text: 'Exporter',
  },

  {
    name: 'comment',
    text: 'Comment',
  },

  {
    name: 'details.module_functions_count',
    text: 'Module Functions Count',
  },

  {
    name: 'details.external_functions_count',
    text: 'External Functions Count',
  },

  {
    name: 'details.basic_blocks_count',
    text: 'Basic Blocks Count',
  },

  {
    name: 'details.instructions_count',
    text: 'Instructions Count',
  },
]
