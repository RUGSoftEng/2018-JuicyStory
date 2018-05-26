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
	logInUser (username, password) {
		return new Promise((resolve) => {
			axios.post('http://localhost:8000/entry/login-user/',
			{	
				'username': [`${username}`],
				'password': [`${password}`]
			})
			.then(response => {
				resolve(response.data)
			})
		})
	}

}

export default appService
