<template>
  <div id="navigation" v-bind:class="navigationStyle" v-cloak>
      <ul>
        <li><router-link v-bind:class="" :to="{ name: 'Dashboard'}">Dashboard</router-link></li>
        <li>|</li>
        <li><router-link class="" :to="{ name: 'Incoming'}">Incoming</router-link></li>
        <li>|</li>
        <li><router-link class="" :to="{ name: 'Stories'}">Stories</router-link></li>
        <li>|</li>
        <li><router-link class="" :to="{ name: 'Report'}">Report</router-link></li>
        <li>|</li>
        <li><router-link class="" :to="{ name: 'StoryCreator'}">Story Creator</router-link></li>
      </ul>
    </div>
</template>

<script>
export default {
  name: 'navigation',
  data () {
    return {
      navigationStyle: 'navigation',
      currentPage: 'bold',
      link: 'link'
    }
  }
}
</script>

<style>

.bold {
  color: pink;
}

.navigation {
  font-family: 'Lato', sans-serif;
  font-size: 1.2em;
  line-height: 1.7;
  font-weight: bold;
  margin: 0px;
  color: silver;
  margin-top: 1%;
  text-align: center;
}

.navigation ul {
  margin: 0;
  padding: 0;
}

.navigation li {
  font-size: 1.25em;
  padding: 20px;
  display: inline-block;
}

</style>
