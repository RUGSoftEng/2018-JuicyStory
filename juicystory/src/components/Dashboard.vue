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
      <div id="rightcol" class="col-sm">
        <ul>
          <li v-for="story in stories" :key="story.date">
            <div class="selected" v-if="story.selected === true" v-on:click="select(story, $event)">
              <img v-bind:src="story.url" height="144" width="81"> <!-- Instagram stories are 9:16 -->
              <div class="checkmark"></div>
            </div>
            <div class="nonselected" v-else v-on:click="select(story, $event)">
              <img v-bind:src="story.url" height="144" width="81">
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
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
        {date: '01-01-2017', time: '15:00', url: 'https://i.pinimg.com/736x/1f/aa/c1/1faac19109da7ea33db3051ce037d7c7--vintage-flowers-wallpaper-flower-iphone-wallpaper.jpg', selected: false},
        {date: '01-01-2017', time: '15:00', url: 'http://www.hdwallpaperspulse.com/wp-content/uploads/2017/06/24/awesome-hd-iphone-image.jpg', selected: false},
        {date: '01-01-2017', time: '15:00', url: 'https://amazingpict.com/wp-content/uploads/2017/09/rough-sea-%E2%98%85-preppy-original-28-free-hd-iphone-7-7-plus-wallpapers.jpg', selected: false},
        {date: '01-01-2017', time: '15:00', url: 'http://backgroundcheckall.com/wp-content/uploads/2017/12/iphone-background-hd-1.jpg', selected: false},
        {date: '01-01-2017', time: '15:00', url: 'http://backgroundcheckall.com/wp-content/uploads/2017/12/iphone-background-images-12.jpg', selected: false},
        {date: '01-01-2017', time: '15:00', url: 'https://amazingpict.com/wp-content/uploads/2018/01/green-land-sky-blue-summer-nature-iphone-6-plus-wallpaper.jpg', selected: false},
        {date: '01-01-2017', time: '15:00', url: 'https://all-images.net/wp-content/uploads/2017/04/iphone-glitter-background-285.jpg', selected: false},
        {date: '01-01-2017', time: '15:00', url: 'https://i.pinimg.com/236x/30/e1/d2/30e1d275c2bd60b80ed576ea3c4b46e6.jpg', selected: false},
        {date: '01-01-2017', time: '15:00', url: 'http://www.iclarified.com/images/news/33642/138964/138964-640.png', selected: false}
      ]
    }
  },

  methods: {
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
