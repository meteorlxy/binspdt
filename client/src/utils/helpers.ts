import format from 'date-fns/format'
import filesize from 'filesize'

export const decToHex: (str: string | number) => string = str => Number(str).toString(16).toUpperCase()

export const formatDateTime: (str: string) => string = str => format(str, 'YYYY-MM-DD HH:mm:ss')

export const floatToPercent: (str: string | number) => string = str => `${(Number(str) * 100).toFixed(2)}%`

export const noop: (_: any) => void = () => {}

export default {
  decToHex,
  filesize,
  floatToPercent,
  formatDateTime,
  noop,
}
