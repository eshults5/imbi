import { httpGet } from './utils'

export function fetchSettings(fetch, path, asOptions, onSuccess, onError) {
  httpGet(
    fetch,
    path,
    (data) => {
      if (asOptions) {
        const options = []
        data.map((projectType) => {
          options.push({
            label: projectType.name,
            value: projectType.name
          })
        })
        onSuccess(options)
      } else {
        onSuccess(data)
      }
    },
    onError
  )
}

export function fetchProjectTypes(fetch, asOptions, onSuccess, onError) {
  fetchSettings(fetch, '/settings/project_types', asOptions, onSuccess, onError)
}

export function fetchGroups(fetch, asOptions, onSuccess, onError) {
  fetchSettings(fetch, '/settings/groups', asOptions, onSuccess, onError)
}
