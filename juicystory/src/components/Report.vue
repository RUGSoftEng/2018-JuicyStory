<template>
  <div id="statList" v-cloak>
    <div>
      <div></div>
      Filter from dd/mm/yyyy to dd/mm/yyyy
    </div>
    <br>
    <br>
    <ul>
      <li v-for="stat in stats" :key="stat.type">
        <div id="statContainer">
          <div>
            <div class="divLeft">{{ stat.type }}</div>
            <div id="div2">{{ stat.stat}}</div>
          </div>
          <br>
          <br>
          <div class="row">
            <div class="col-sm">
              <div class="box">
                <img v-bind:src="stat.url">
              </div>
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'report',
  data () {
    return {
      stats: [
        {type: 'Impressions', stat: '400', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Reach', stat: '600', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Completion rate', stat: '80%', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Taps Back', stat: '800', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Replies', stat: '500', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Followers', stat: '200', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'}
      ]
    }
  }
}
</script>

<style>
#statList {
    display: inline-block;
}
.box {
  padding: 10px;
  border-radius: 20px;
}
#statContainer {
  width: 400px;
  padding-top: 20px;
  padding-bottom: 20px;
  box-shadow: 2px 2px 2px 2px silver;
  background-color: white;
  border-radius: 5px;
}
.divLeft {
  float: left;
  padding-left: 15px;
  font-style: normal;
  font-size: large;
}
#div2 {
  float: right;
  padding-right: 15px;
  font-style: normal;
  font-size: x-large;
}
#dateSelect {
  position: absolute;
  left: 100px;
  padding: 4px;
  font-style: normal;
}
</style>
