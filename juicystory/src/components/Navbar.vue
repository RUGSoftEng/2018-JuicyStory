<template>
  <div id="navigation" v-bind:class="navigationStyle" v-cloak>
      <ul>
        <li><router-link class="link" :to="{ name: 'Dashboard'}">Dashboard</router-link></li>
        <li>|</li>
        <li><router-link class="link" :to="{ name: 'Incoming'}">Incoming</router-link></li>
        <li>|</li>
        <li><router-link class="link" :to="{ name: 'Stories'}">Stories</router-link></li>
        <li>|</li>
        <li><router-link class="link" :to="{ name: 'Report'}">Report</router-link></li>
        <li>|</li>
        <li><router-link class="link" :to="{ name: 'StoryCreator'}">Story Creator</router-link></li>
      </ul>
    </div>
</template>

<script>
export default {
  name: 'navigation',
  data () {
    return {
      navigationStyle: 'navigation'
    }
  }
}
</script>

<style>

/*.link {
  color: #CE2655;
  text-decoration: none;
}

.router-link-exact-active {
  color: #CE2655;
  text-decoration: none;
}*/

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
