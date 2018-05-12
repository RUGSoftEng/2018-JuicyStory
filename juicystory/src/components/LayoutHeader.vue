<template>
      <div class="container">
      <div class="row">
        <div id="left" class="col-6 col-md-4"><ul><li style="color: #CE2655">Account Name</li></ul></div>
        <div id="middle" class="col-6 col-md-4">
          <img id="logo-pic" src="../assets/logo1.png" v-bind:alt="alt">
          </div>
        <div id="right" class="col-6 col-md-4">
          <ul>
            <li><router-link :to="{ name: 'Dashboard'}"><i class="glyphicon glyphicon-home"></i></router-link></li>
            <li>|</li>
            <li><router-link :to="{ name: 'MyAccount'}">My Account</router-link></li>
            <li>|</li>
            <li><router-link :to="{ name: '', params: {} }">Log Out</router-link></li>
          </ul>
          </div>
      </div>
    </div>
</template>

<script>
export default {
  name:'menu',
  data() {
    return {
    alt: 'Juicy Story Logo'
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

.container {
  width: 90%;
  padding-top: 20px;
  padding-bottom: 20px;
  box-shadow: 2px 2px 2px 2px silver;
  background-color: white;
}


.row {
  font-family: 'Lato', sans-serif;
  font-size: 1.2em;
  line-height: 1.7;
  font-weight: bold;
  margin: 0px;
  color: silver;
}
ul {
  margin: 0;
  padding: 0;
}

li {
  font-size: 1em;
  padding: 5px;
  margin-right: 10px;
  display: inline-block;
}

#left {
  text-align: left;
}

#middle {
  text-align: center;
}

#right {
  text-align: right;
}


</style>
