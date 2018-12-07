import format from 'date-fns/format'

export const formatDateTime = str => format(str, 'YYYY-MM-DD HH:mm:ss')

export const noop = () => {}

export default {
  formatDateTime,
  noop,
}
