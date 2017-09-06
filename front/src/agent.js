import superagentPromise from 'superagent-promise'
import _superagent from 'superagent'

const superagent = superagentPromise(
    _superagent, global.Promise
)

const API_ROOT = 'http://127.0.0.1:5000/api'
const encode = encodeURIComponent
const responseBody = res => res.body

let token = null
const tokenPlugin = req => {
    if (token) {
        res.set('authorization', `Token ${token}`)
    }
}

const requests = {
    del: url =>
        superagent.del(`${API_ROOT}${url}`).use(tokenPlugin).then(responseBody),
    get: url =>
        superagent.get(`${API_ROOT}${url}`).use(tokenPlugin).then(responseBody),
    put: (url, body) =>
        superagent.put(`${API_ROOT}${url}`, body).use(tokenPlugin).then(responseBody),
    post: (url, body) =>
        superagent.post(`${API_ROOT}${url}`, body).use(tokenPlugin).then(responseBody)
}

const Papers = {
    all: () => requests.get('/papers'),
    upload: papers => requests.post('/papers', { papers })
}


export default {
    Papers,
    setToken: _token => { token: _token }
}