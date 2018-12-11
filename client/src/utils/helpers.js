import format from 'date-fns/format'
import filesize from 'filesize'

export const formatDateTime = str => format(str, 'YYYY-MM-DD HH:mm:ss')

export const noop = () => {}

export default {
  filesize,
  formatDateTime,
  noop,
}
