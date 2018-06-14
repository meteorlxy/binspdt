import format from 'date-fns/format'

const formatDateTime = str => format(str, 'YYYY-MM-DD HH:mm:ss')

export default {
  formatDateTime
}
