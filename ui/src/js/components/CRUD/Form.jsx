import { compare } from 'fast-json-patch'
import PropTypes from 'prop-types'
import React, { useContext, useState } from 'react'

import { Columns } from '../../schema'
import { FetchContext } from '../../contexts'
import { Form } from '..'
import { httpPost, httpPatch } from '../../utils'

function CrudForm({
  columns,
  errorStrings,
  isEdit,
  itemKey,
  itemPath,
  jsonSchema,
  onClose,
  savingTitle,
  title,
  values
}) {
  const fetchMethod = useContext(FetchContext)
  const [originalValues, _] = useState(values) // eslint-disable-line

  async function handleSubmit(formValues) {
    let result = null
    if (isEdit === true) {
      const patchValue = compare(originalValues, formValues)
      result = await httpPatch(
        fetchMethod,
        itemPath.replace(/{{value}}/, originalValues[itemKey]),
        patchValue
      )
    } else {
      result = await httpPost(fetchMethod, itemPath, formValues)
    }
    if (result.success === true) {
      onClose(formValues[itemKey])
    } else {
      return errorStrings[result.data] !== undefined
        ? errorStrings[result.data]
        : result.data
    }
  }

  return (
    <Form
      columns={columns}
      jsonSchema={jsonSchema}
      onClose={onClose}
      onSubmit={handleSubmit}
      savingTitle={savingTitle}
      title={title}
      values={values}
    />
  )
}

CrudForm.propTypes = {
  columns: Columns.isRequired,
  errorStrings: PropTypes.object.isRequired,
  isEdit: PropTypes.bool.isRequired,
  itemKey: PropTypes.string.isRequired,
  itemPath: PropTypes.string.isRequired,
  jsonSchema: PropTypes.object.isRequired,
  onClose: PropTypes.func.isRequired,
  savingTitle: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  values: PropTypes.object
}

export { CrudForm as Form }
