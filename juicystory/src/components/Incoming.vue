<template>
  <div id="incoming" v-cloak>
      <ul>
        <li v-for="img in images" :key="img.user">
          <div class="selected" v-if="img.selected === true" v-on:click="select(img, $event)">
            <img v-bind:src="img.url" height="288" width="162"> <!-- Instagram stories are 9:16 -->
            <div class="checkmark"></div>
          </div>
          <div class="nonselected" v-else v-on:click="select(img, $event)">
            <img v-bind:src="img.url" height="288" width="162">
          </div>
          <p class="imginfo">
            {{ img.user }}<br>
            {{ img.date }} | {{ img.time }}
          </p>
        </li>
      </ul>

        <router-link :to="{ name: 'StoryCreator'}">
      <button class="btn btn-primary">Create Story</button>
      </router-link>
    </div>
</template>

<script>
import appService from '../app-service.js'

export default {
  name: 'incoming',
  data () {
    return {
    /* list of the incoming images */
      images: [
        {user: '@user', date: '01-01-2017', time: '15:00', url: 'https://i.pinimg.com/736x/1f/aa/c1/1faac19109da7ea33db3051ce037d7c7--vintage-flowers-wallpaper-flower-iphone-wallpaper.jpg', selected: false},
        {user: '@user', date: '01-01-2017', time: '15:00', url: 'http://www.hdwallpaperspulse.com/wp-content/uploads/2017/06/24/awesome-hd-iphone-image.jpg', selected: false},
        {user: '@user', date: '01-01-2017', time: '15:00', url: 'https://amazingpict.com/wp-content/uploads/2017/09/rough-sea-%E2%98%85-preppy-original-28-free-hd-iphone-7-7-plus-wallpapers.jpg', selected: false},
        {user: '@user', date: '01-01-2017', time: '15:00', url: 'http://backgroundcheckall.com/wp-content/uploads/2017/12/iphone-background-hd-1.jpg', selected: false},
        {user: '@user', date: '01-01-2017', time: '15:00', url: 'http://backgroundcheckall.com/wp-content/uploads/2017/12/iphone-background-images-12.jpg', selected: false},
        {user: '@user', date: '01-01-2017', time: '15:00', url: 'https://amazingpict.com/wp-content/uploads/2018/01/green-land-sky-blue-summer-nature-iphone-6-plus-wallpaper.jpg', selected: false},
        {user: '@user', date: '01-01-2017', time: '15:00', url: 'https://all-images.net/wp-content/uploads/2017/04/iphone-glitter-background-285.jpg', selected: false},
        {user: '@user', date: '01-01-2017', time: '15:00', url: 'https://i.pinimg.com/236x/30/e1/d2/30e1d275c2bd60b80ed576ea3c4b46e6.jpg', selected: false},
        {user: '@user', date: '01-01-2017', time: '15:00', url: 'http://www.iclarified.com/images/news/33642/138964/138964-640.png', selected: false}
      ],
      selectedImg: []
    }
  },

  methods: {
    getIncomingImages(username, token) {
      appService.getIncoming(username, token)
      .then(data => {
        console.log(data)
        for(var i = 0; i <= data.images.length; i++) {
          var obj = {}
          obj.user = 'testy8101.' + i
          var a = new Date(data.timestamps[i] / 1000)
          var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
          var year = a.getFullYear()
          var month = months[a.getMonth()]
          var date = a.getDate()
          var hour = a.getHours()
          var min = a.getMinutes()
          obj.date = date + '-' + month + '-' + year
          obj.time = hour + ':' + min
          obj.url = data.images[i]
          obj.selected = false
          this.images.push(obj)
        }
      })
    },
    select: function (image, event) {
      image.selected = !image.selected
      this.selectedImg.push(image)
    }
  },
  created() {
    this.token = window.localStorage.getItem('token')
    this.getIncomingImages('testy8101', this.token)
  }
}
</script>

<style>
  #incoming {
    width: 90%;
    margin: auto;
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
    font-size: 80px;
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

  .imginfo {
    padding: 0 10px;
    font-family: 'Lato', sans-serif;
  }
</style>
