
new Vue({
  el: '#incoming',
  data: {
    /*list of the incomig images*/
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

      selectedImg: ['http://www.iclarified.com/images/news/33642/138964/138964-640.png']
  },
  methods: {
    select: function(image, event) {
      image.selected = !image.selected;
    }
  }
})
