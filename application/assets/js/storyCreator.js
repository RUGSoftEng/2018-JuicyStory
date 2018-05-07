new Vue({
  el:'#story',
  data: {
    /*list of the previously selected images in incoming*/
      items:
        [
        'http://www.iclarified.com/images/news/33642/138964/138964-640.png',
        'https://i.pinimg.com/236x/30/e1/d2/30e1d275c2bd60b80ed576ea3c4b46e6.jpg',
        'http://backgroundcheckall.com/wp-content/uploads/2017/12/iphone-background-images-12.jpg'
        ],
      storyItems: [],
      accountListStyle:'story',
      message: 'No images to display',
      view: 'split',
      left: 'left',
      right: 'right',
      aspect: 'ratio',
      placeholder: 'placeholder'
  },

  methods: {
    removeElem: function(input, list) {
      for(var i = list.length - 1; i >= 0; i--) {
          if(list[i] == input) {
            Vue.delete(list, i);
        }
      }
    },

    addToStory: function(picture){
      this.storyItems.push(picture);
      this.removeElem(picture, this.items);
    },

    removeFromStory: function(picture){
      this.items.push(picture);
      this.removeElem(picture, this.storyItems)
    }
  }
})
