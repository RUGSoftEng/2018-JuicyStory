<template>
  <div id="story" v-bind:class="accountListStyle" v-cloak>
    <div class="row">
      <div class="col-sm-6">
        <label>Select Pictures</label><br>
        <i class="fa fa-camera-retro icon"></i><small> Click images to add to story</small>
        <br><br>

        <ul v-if="items.length === 0">
          <li><div v-bind:class="[placeholder, aspect]">{{message}}</div></li>
        </ul>

        <ul v-else>
          <li v-for="item in items">
            <img v-bind:src="item.url" v-on:click="addToStory(item)" height="288" width="162">
          </li>
        </ul>

      <br>
      </div>
      <div class="col-sm-6">
        <div>
          <label>Story</label><br>
          <i class="fa fa-camera-retro icon"></i><small> Click images to remove from story</small>
        <br><br>

          <ul v-if="storyItems.length === 0">
            <li><div v-bind:class="[placeholder, aspect]">{{message}}</div></li>
          </ul>

          <ul v-else>
            <li v-for="pic in storyItems">
              <img v-bind:src="pic.url" v-on:click="removeFromStory(pic)" v-bind:class="aspect">
            </li>
          </ul>
        </div>

        <div>
          <button v-on:click="postStory" class="btn btn-primary">Schedule Story</button>
        </div>
        <br>
      </div>
    </div>
  </div>

</template>

<script>
import appService from '../app-service.js'

export default {
  name: 'story',
  data () {
    return {
    // list of the previously selected images in incoming
      items: [
        {url: 'http://www.iclarified.com/images/news/33642/138964/138964-640.png'},
        {url: 'https://i.pinimg.com/236x/30/e1/d2/30e1d275c2bd60b80ed576ea3c4b46e6.jpg'},
        {url: 'http://backgroundcheckall.com/wp-content/uploads/2017/12/iphone-background-images-12.jpg'}
      ],
      storyItems: [],
      accountListStyle: 'story',
      message: 'No images to display',
      view: 'split',
      left: 'left',
      right: 'right',
      aspect: 'ratio',
      placeholder: 'placeholder'
    }
  },

  created() {
    this.token = window.localStorage.getItem('token')
    //this.postStory('testy8101', this.token)
  },

  methods: {
    removeElem: function (input, list) {
      for (var i = list.length - 1; i >= 0; i--) {
        if (list[i] === input) {
          list.splice(i, 1)
        }
      }
    },

    addToStory: function (picture) {
      this.storyItems.push(picture)
      this.removeElem(picture, this.items)
    },

    removeFromStory: function (picture) {
      this.items.push(picture)
      this.removeElem(picture, this.storyItems)
    },

    postStory: function (){
      appService.postStory('testy8101', this.token)
      //this.postStory('testy8101', this.token)

    }
  }
}
</script>

<style>

.story {
  font-family: 'Lato', sans-serif;
  font-size: 18px;
  font-weight: normal;
  color: #CE2655;
  padding-top: 3%;
}

.col-sm-6 {
  text-align: center;
  font-weight: lighter;
  color: #CE2655;
}

.story ul {
  list-style-type: none;
}

.story li {
   margin: 0 0 30px 0;
   display: inline-block;
   padding: 5px 5px;
}

.ratio {
  height: 288px;
  width: 162px;
}

.icon {
  box-shadow: 0 8px 6px -2px DarkGrey;
}

.placeholder {
  box-shadow:  5px 5px 5px  DarkGrey;
  border-radius: 20px;
  border-style: dashed;
  border-color: DarkGrey;
  padding-top: 70%;
  padding-left: 10%;
  padding-right: 10%;
  display: fixed;
  color: Grey;
}

img {
  border-radius: 20px;
  align-self: center;
}
</style>



