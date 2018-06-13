import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Dashboard from '@/components/Dashboard'
import Incoming from '@/components/Incoming'
import Report from '@/components/Report'
import StoryCreator from '@/components/StoryCreator'
import Stories from '@/components/Stories'
import MyAccount from '@/components/MyAccount'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/incoming',
      name: 'Incoming',
      component: Incoming
    },
    {
      path: '/report',
      name: 'Report',
      component: Report
    },
    {
      path: '/storycreator',
      name: 'StoryCreator',
      component: StoryCreator
    },
    {
      path: '/stories',
      name: 'Stories',
      component: Stories
    },
    {
      path: '/myaccount',
      name: 'MyAccount',
      component: MyAccount
    }
  ]
})
