new Vue({
  delimiters: ['[[', ']]'],
  el:'#accountList',
  data: {
    headerName: 'My Account List',
    /*list of accounts*/
    items: [
        {name: '@tolga', pic:'images/profile.png'},
        {name: '@SE2018', pic:'images/profile.png'}
      ],
    accountListStyle:'accountList',
    view: 'split',
    left: ['left', 'col-md-4'],
    right: ['right', 'col-md-8'],
    imgStyle: 'img-circle',
    cnt: 'container-input',
    input: ''
  },

  methods: {
    getInstagramUsers: function(){
      this.loading = true;
      //specify the http request type ie. get & the url
      this.$http.get('/api/InstagramUser/').then((response) => {
        //code if the request actually worked
        this.items = response.data.results;
        this.loading = false;
      }).catch((err) => {
        //request didn't work
       this.loading = false;
       console.log(err);
      })
    },

    removeElem: function(input) {
      for(var i = this.items.length - 1; i >= 0; i--) {
          if(this.items[i].name == input) {
          this.items.splice(i, 1);
        }
      }
    },

    addElem: function(input) {
      var ok=1;
      if(input != "") {
        for(var i = this.items.length - 1; i >= 0 && ok==1; i--) {
            if(this.items[i].name == input) {
              ok = 0;
          }
        }

        if(ok == 1) {
          /* placeholder for pushing the Instagram name + profile photo*/
          this.items.push({name: 'alina123'});
        }
      }

    }
  }
})
