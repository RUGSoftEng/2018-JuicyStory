<template>
  <div id="statList" v-cloak>
      <label>Filter from <datepicker class="datepicker" v-model="state.date1" name="From"></datepicker> to <datepicker class="datepicker" v-model="state.date2" name="To"></datepicker></label>
      <button class="btn btn-sm btn-primary">GO!</button>
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
/* eslint-disable */
  import Datepicker from "vuejs-datepicker/dist/vuejs-datepicker.esm.js";
  import * as lang from "vuejs-datepicker/src/locale";

const state = {
  date1: new Date(),
  date2: new Date()
};

export default {
  name: 'report',
  components: {
    Datepicker
  },
  data () {
    return {
      stats: [
        {type: 'Impressions', stat: '400', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Reach', stat: '600', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Completion rate', stat: '80%', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Taps Back', stat: '800', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Replies', stat: '500', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'},
        {type: 'Followers', stat: '200', date: '01-01-2017', url: 'http://www.clker.com/cliparts/3/H/q/L/N/5/simple-graph-th.png'}
      ],
      format: "d MMMM yyyy",
      disabledDates: {},
      disabledFn: {
        customPredictor(date) {
          if (date.getDate() % 3 === 0) {
            return true;
          }
        }
      },
      highlightedFn: {
        customPredictor(date) {
          if (date.getDate() % 4 === 0) {
            return true;
          }
        }
      },
      highlighted: {},
      placeholder: "Test",
      eventMsg: null,
      state: state,
      language: "en",
      languages: lang,
      vModelExample: null
    };
  }
}
</script>

<style>
ul {
  margin-top: 2%;
  color: #CE2655;
}

label {
  font-size: 18px;
}

.datepicker {
  text-align: center;
  display: inline-block;
  color: DarkGray;
}
#statList {
    display: inline-block;
    margin-top: 4%;
    font-family: 'Lato' sans-serif;
    color: Gray;
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
  display: inline-block;
  left: 400px;
  padding: 4px;
  font-style: normal;
}
#dateSelect2 {
  position: absolute;
  display: inline-block;
  left: 700px;
  padding: 4px;
  font-style: normal;
}
</style>
