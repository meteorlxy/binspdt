import format from 'date-fns/format'
import filesize from 'filesize'

export const formatDateTime: (str: string) => string = str => format(str, 'YYYY-MM-DD HH:mm:ss')

export const noop: (_: any) => void = () => {}

export default {
  filesize,
  formatDateTime,
  noop,
}
