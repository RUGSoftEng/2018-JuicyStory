<template>
  <div id="container">
    <div class="row">
      <div id="leftcol" class="col-sm-8">
        <div class="card">
          <h3>Impressions</h3>
          <p class="description">
            <i class="symbol glyphicon glyphicon-eye-open"></i>
            {{ impressions }}
          </p>
        </div>

        <div class="card">
          <h3>Reach</h3>
          <p class="description">
            <i class="symbol glyphicon glyphicon-check"></i>
            {{ reach }}
          </p>
        </div>

        <div class="card">
          <h3>Completion Rate</h3>
          <p class="description">
            <i class="symbol glyphicon glyphicon-forward"></i>
            {{ completionRate }}%
          </p>
        </div>

        <div class="card">
          <h3>Taps Back</h3>
          <p class="description">
            <i class="symbol glyphicon glyphicon-camera"></i>
            {{ tapsBack }}
          </p>
        </div>

        <div class="card">
          <h3>Replies</h3>
          <p class="description">
            <i class="symbol glyphicon glyphicon-share-alt"></i>
            {{ replies }}
          </p>
        </div>

        <div class="card">
          <h3>Followers</h3>
          <p class="description">
            <i class="symbol glyphicon glyphicon-user"></i>
            {{ followers }}
          </p>
        </div>
      </div>
      <div id="rightcol" class="col-sm" v-cloak>
        <ul>
          <li v-for="story in stories" :key="story.date">
            <div class="selected" v-if="story.selected === true" v-on:click="select(story, $event)">
              <img v-bind:src="story" height="144" width="81"> <!-- Instagram stories are 9:16 -->
              <div class="checkmark"></div>
            </div>
            <div class="nonselected" v-else v-on:click="select(story, $event)">
              <img v-bind:src="story" height="144" width="81">
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import appService from '../app-service.js'

export default {
  name: 'dashboard',
  data () {
    return {
      impressions: 400,
      reach: 300,
      completionRate: 75,
      tapsBack: 150,
      replies: 133,
      followers: 300,
      stories: [
      ]
    }
  },

  methods: {
    getStoryImages(username, token) {
      appService.getArrayOfImages(username, token)
      .then(data => {
        console.log(data)
        this.stories = data.images
      })
    },
    getStoryStats(username, token) {
      appService.getStoryStats(username, token)
      .then(data => {
        console.log(data)
      })
    },
    select: function (story, event) {
      for (var i = this.stories.length - 1; i >= 0; i--) {
        if (this.stories[i].selected === true) {
          this.stories[i].selected = false
        }

        if (this.stories[i] === story) {
          this.stories[i].selected = true
        }
      }
    }
  },
  created() {
    this.token = window.localStorage.getItem('token')
    this.getStoryImages('testy8101', this.token)
    this.getStoryStats('testy8101', this.token)
  }
}
</script>

<style>
  #container {
    width: 90%;
    margin: auto;
    position: relative;
    text-align: center;
    top: 30px;
  }

  #leftcol {
    border-right: solid silver;
  }

  #rightcol {
  /*  overflow-y: scroll;*/
    /*white-space: nowrap; */
  }

  .card {
    /* border: 1px solid #46529E; */
    border-radius: 10px;
    background-color: #FFFFFF;
    box-shadow: 2px 2px 2px 2px silver;
    display: inline-block;
    margin: 20px;
    padding: 30px auto;
    height: 200px;
    width: 200px;
  }

  h3 {
    font-family: 'Lato', sans-serif;
    color: #CE2655;
    text-align: center;
  }

  h1 {
    font-family: 'Lato', sans-serif;
  }

  .symbol {
    color: silver;
    font-size: 20px;
  }

  .description {
    font-family: 'Lato', sans-serif;
    color: #000000;
    font-size: 45px;
    margin-top: 40px;
    font-weight: normal;
  }

  .selected img {
    opacity: 0.5;
  }

  img {
    padding: 10px;
    border-radius: 15px;
  }

  .selected, .nonselected {
    position: relative;
  }

  .checkmark {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 50px;
  }

  .checkmark:before {
    content: "✓";
    font-style: normal;
    font-weight: normal;
    text-decoration: inherit;
    color: #CE2655;
  }

  ul {
    list-style-type: none;
  }
</style>
