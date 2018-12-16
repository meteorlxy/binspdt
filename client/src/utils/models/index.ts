const getValueFromFieldsArr = (data, fieldsArr) => {
  if (data === undefined) {
    return undefined
  }
  if (fieldsArr.length > 1) {
    return getValueFromFieldsArr(data[fieldsArr[0]], fieldsArr.slice(1))
  }
  return data[fieldsArr[0]]
}

export const getFieldValue = (data, field) => {
  return getValueFromFieldsArr(data, field.split('.'))
}

export const getFields = ({
  data,
  fields,
  fieldsShow = null,
  fieldsHide = [],
}: any = {}) => {
  let displayFields = fields
  if (fieldsShow !== null) {
    displayFields = displayFields.filter(item => fieldsShow.includes(item.name))
  } else {
    displayFields = displayFields.filter(item => !fieldsHide.includes(item.name))
  }

  return displayFields.map(field => {
    let value = getFieldValue(data, field.name)

    if (value === undefined) {
      return
    }

    if (typeof field.formatter === 'function') {
      value = field.formatter(value)
    }

    return {
      text: field.text,
      value,
    }
  })
}

export default {
  getFields,
  getFieldValue,
}
