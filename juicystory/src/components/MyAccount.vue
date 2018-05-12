<template>
  <div id="accountList" v-cloak>
    <div class="row" v-bind:class="accountListStyle">
      <div id="left" class="col-sm-6">
        <div><label>{{headerName}}</label><br></div>
        <ul>
          <li v-for="item in items">
            <img id="over" src="../assets/logo.png" v-bind:class="imgStyle"> <br> <b>{{item.name}}</b>
          </li>
        </ul>
      </div>
      <div id="right" class="col-sm-6 ">
        <label>Manage account list</label><br>

          <div class="input">
            <input v-model.trim.lazy="input" type="text" class="form-control" placeholder="Instagram Account" style="text-align: center"></input>
          </div>
          <div class="buttons">
            <button class="btn btn-primary" v-on:click="addElem(input)">Add</button>
            <button class="btn btn-primary" v-on:click="removeElem(input)">Remove</button>

      </div>
       </div>
    </div>
</div>

</template>

<script>
  export default {

  name:'accountList',
  data() {
    return {
      headerName: 'My Accounts List',
      /*list of accounts*/
      items: [
          {name: '@tolga', pic:'../../src/assets/logo.png'},
          {name: '@SE2018', pic:'https://www.google.nl/imgres?imgurl=https%3A%2F%2Fwww.cats.org.uk%2Fuploads%2Fimages%2Ffeaturebox_sidebar_kids%2Fgrief-and-loss.jpg&imgrefurl=https%3A%2F%2Fwww.cats.org.uk%2F&docid=-uCj01WW3BLRtM&tbnid=B3B6q7ZifCm2kM%3A&vet=10ahUKEwj0l8aHrPHaAhUHa8AKHSeDAlUQMwjcASgCMAI..i&w=582&h=328&bih=759&biw=1536&q=cats&ved=0ahUKEwj0l8aHrPHaAhUHa8AKHSeDAlUQMwjcASgCMAI&iact=mrc&uact=8'}
        ],
      accountListStyle:'accountList',
      view: 'split',
      left: ['left', 'col-md-4'],
      right: ['right', 'col-md-8'],
      imgStyle: 'img-circle',
      cnt: 'container-input',
      input: ''
    }
  },

  methods: {
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
      }

        if(ok == 1) {
          /* placeholder for pushing the Instagram name + profile photo*/
          this.items.push({name: 'alina123'});
        }
    }

  }

  }
</script>

<style>
.input {
  padding-left: 29%;
}
.form-control {
  width: 60%;
  text-align: center;
}
.accountList {
  font-family: 'Lato', sans-serif;
  font-size: 18px;
  color: #CE2655;
  padding-top: 5%;
  padding-bottom: 5%;
}

.accountList ul {
  list-style-type: none;
}

.accountList li {
   margin:0 0 30px 0;
   color: #808080;
   display: block;
}

#right, #left {
  text-align: center;
}


.buttons {
  padding-top: 2%;
}

.img-circle {
  height: 90px;;
  weight: 90px;
  border-radius: 50%;
  border: solid;
  border-color: #CE2655;
}

</style>
