<template>
  <div id="app">
    <div class="header">
      <layout-header></layout-header>
      <navbar class="navbar"></navbar>
    </div>
    <div class="router"><router-view/></div>
    <div><layout-footer></layout-footer></div>
  </div>
</template>

<script>
import LayoutHeader from './components/LayoutHeader.vue'
import LayoutFooter from './components/LayoutFooter.vue'
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    'layout-header': LayoutHeader,
    'layout-footer': LayoutFooter,
    'navbar': Navbar
  }
}
</script>

<style>
.router {
  margin-bottom: 60px;
  height: 100%;
}

.header {

}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #F8F8F8;
  background-size: cover;
  margin-top: 0px;
  height: 100%;
  width: 100%;
  min-height: 100%;
  min-width: 100%;
  overflow: auto;
  display: block;
  position: absolute;
}

.btn-primary {
  /*text-decoration-color: white;*/
  background-color: #CE2655 !important;
  color: white;
  border: none;
}

a {
  color:#CE2655;
  text-decoration: none;
}

a:focus {
  color: #CE2655;
  font-weight: bolder;
  text-decoration: none;
}

a:hover {
  text-decoration: none;
}
</style>
