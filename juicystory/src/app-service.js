
import axios from 'axios'
/* eslint-disable */
axios.default.baseURL = 'http://localhost:8000'

axios.interceptors.request.use(request => {
  console.log('Starting Request', request)
  return request
})

axios.interceptors.response.use(response => {
  console.log('Response: ', response)
  return response
})

const appService = {
  logInUser(username, password) {
    return new Promise((resolve) => {
      axios.post('http://localhost:8000/api/login-user/',
        {
          'username': `${username}`,
          'password': `${password}`
        })
        .then(response => {
          resolve(response.data)
        })
    })
  },
  getArrayOfImages(username, token) {
    return new Promise((resolve) => {
      axios.get(`http://localhost:8000/api/story/${username}/`,
        {
          headers: {
            'Authorization': `JWT ${token}`
          }
        }
      )
        .then(response => {
          resolve(response.data)
        })
    })
  },
  getStoryStats(username, token) {
    return new Promise((resolve) => {
      axios.get(`http://localhost:8000/api/metrics/${username}/`,
        {
          headers: {
            'Authorization': `JWT ${token}`
          }
        }
      )
        .then(response => {
          resolve(response.data)
        })
    })
  },
  getIncoming(username, token) {
    return new Promise((resolve) => {
      axios.get(`http://localhost:8000/api/get-dms/${username}/`,
        {
          headers: {
            'Authorization': `JWT ${token}`
          }
        }
      )
        .then(response => {
          resolve(response.data)
        })
    })
  },
  postStory(username, token) {
    return new Promise((resolve) => {
      axios.post(`http://localhost:8000/api/post-story/`,
        {
          headers: {
            'Authorization': `JWT ${token}`
          },
          iusername: '${username}',
          photo_url: "http://www.personal.psu.edu/jyc5774/jpg.html"
        }
      )
        .then(response => {
          resolve(response.data)
        })
    })
  }
}

export default appService
