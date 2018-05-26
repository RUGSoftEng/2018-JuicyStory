/* eslint-disable *//* eslint-disable */
<template>

  <div class="login">
    <div class="limiter">
    <div class="container-login100">
      <div class="wrap-login100">
        <div class="login100-pic">
          <img src="../assets/logo1.png" alt="Juicy Story Logo">
        </div>

        <form class="login100-form validate-form" action="#" method="post">
          <span class="login100-form-title">
            Login
          </span>

          <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
            <input class="input100" type="email" v-model="username" name="email" placeholder="Email">
            <span class="focus-input100"></span>
            <span class="symbol-input100">
              <i class="fa fa-envelope" aria-hidden="false"></i>
            </span>
          </div>

          <div class="wrap-input100 validate-input" data-validate = "Password is required">
            <input class="input100" type="password" v-model="password" name="pass" placeholder="Password">
            <span class="focus-input100"></span>
            <span class="symbol-input100">
              <i class="fa fa-lock" aria-hidden="false"></i>
            </span>
          </div>

          <div class="container-login100-form-btn">
            <!-- <button type="submit" class="login100-form-btn">Login</button> -->
            <a v-on:click="onClick" class="btn btn-default login100-form-btn">Login</a>
          </div>

          <div class="text-center p-t-12">
            <span class="txt1">
              Forgot
            </span>
            <a class="txt2" href="./passRecov.html" target="_blank">
              Password?
            </a>
          </div>

          <div class="text-center">
            <a class="txt2" href="./signup.html" target="_blank">
              Create your Account
            </a>
          </div>
        </form>
      </div>
    </div>
  </div>

  </div>
</template>

<script>
/* eslint-disable */ 

import appService from '../app-service.js'

export default {
  data () {
    return {
      username: 'george',
      password: 'a1234567',
    }
  },
  methods: {
    logInUser (username, password) {
      appService.logInUser(username, password)
      .then(data => {
        window.localStorage.setItem('token', data.token)
        console.log('Succeeded')
      })
    },
    onClick () {
      this.logInUser(this.username, this.password)
    }
  }

}


</script>

<style>
/* eslint-disable */

  .limiter {
    width: 100%;
    margin: 0 auto;
  }

  .container-login100 {
    width: 100%;
    min-height: 80%;
    padding-top: 30px;
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;


    background-attachment: fixed;
  }

  .wrap-login100 {
    width: 900px;
    height: 600px;
    background: white;
    border-radius: 25px;
    overflow: hidden;

    box-shadow:  5px 5px 5px  DarkGrey;

    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    padding: 120px 130px 33px 95px;
  }

  /*------------------------------------------------------------------
  [  ]*/
  .login100-pic {
    width: 316px;
  }

  .login100-pic img {
    max-width: 100%;
  }


  /*------------------------------------------------------------------
  [  ]*/
  .login100-form {
    width: 290px;
  }

  .login100-form-title {
    font-family: 'Heebo' sans-serif;
    font-size: 24px;
    font-weight: bold;
    color: #CE2655;
    line-height: 1.2;
    text-align: center;

    width: 100%;
    display: block;
    padding-bottom: 54px;
  }

  .login100-form-subtitle {
    font-family: 'Lato' sans-serif;
    font-size: 18px;
    color: #333333;
    line-height: 1.2;
    text-align: center;

    width: 100%;
    display: block;
    padding-bottom: 54px;
  }


  /*---------------------------------------------*/
  .wrap-input100 {
    position: relative;
    width: 100%;
    z-index: 1;
    margin-bottom: 10px;
  }

  .input100 {
    font-family: 'Lato';
    font-size: 15px;
    line-height: 1.5;
    color: #CE2655;

    display: block;
    width: 100%;
    background: #e6e6e6;
    height: 50px;
    border-radius: 25px;
    padding: 0 30px 0 68px;
  }


  /*------------------------------------------------------------------
  [ Focus ]*/
  .focus-input100 {
    display: block;
    position: absolute;
    border-radius: 25px;
    bottom: 0;
    left: 0;
    z-index: -1;
    width: 100%;
    height: 100%;
    box-shadow: 0px 0px 0px 0px;
    color: rgba(87,184,70, 0.8);
  }


  .focus-input100-acc {
    display: block;
    position: absolute;
    border-radius: 25px;
    bottom: 0;
    left: 0;
    z-index: -1;
    width: 100%;
    height: 100%;
    box-shadow: 0px 0px 0px 0px;
    color: rgba(87,184,70, 0.8);
  }

  .input100:focus + .focus-input100 {
    -webkit-animation: anim-shadow 0.5s ease-in-out forwards;
    animation: anim-shadow 0.5s ease-in-out forwards;
  }

  .symbol-input100 {
    font-size: 15px;

    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    align-items: center;
    position: absolute;
    border-radius: 25px;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    padding-left: 35px;
    pointer-events: none;
    color: #CE2655;

    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    transition: all 0.4s;
  }

  .symbol-input100-acc{
    font-size: 15px;

    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    align-items: center;
  /*  position: absolute;*/
    border-radius: 25px;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    padding-left: 100px;
    pointer-events: none;
    color: #CE2655;

    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    transition: all 0.4s;
  }

  .input100:focus + .focus-input100 + .symbol-input100 {
    color: #CE2655;
    padding-left: 28px;
  }

  /*------------------------------------------------------------------
  [ Button ]*/
  .container-login100-form-btn {
    width: 100%;
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding-top: 20px;
  }

  .login100-form-btn {
    font-family: 'Heebo';
    font-weight: bold;
    font-size: 15px;
    line-height: 1.5;
    color: white;
    text-transform: uppercase;

    width: 100%;
    height: 50px;
    border-radius: 25px;
    background: #CE2655;
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 25px;

    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    transition: all 0.4s;
  }

  .login100-form-btn:hover {
    background: #46529E;
  }



  /*------------------------------------------------------------------
  [ Responsive ]*/



  @media (max-width: 992px) {
    .wrap-login100 {
      padding: 177px 90px 33px 85px;
    }

    .login100-pic {
      width: 35%;
    }

    .login100-form {
      width: 50%;
    }
  }

  @media (max-width: 768px) {
    .wrap-login100 {
      padding: 100px 80px 33px 80px;
    }

    .login100-pic {
      display: none;
    }

    .login100-form {
      width: 100%;
    }
  }

  @media (max-width: 576px) {
    .wrap-login100 {
      padding: 100px 15px 33px 15px;
    }
  }


  /*------------------------------------------------------------------
  [ Alert validate ]*/

  .validate-input {
    position: relative;
  }

  .alert-validate::before {
    content: attr(data-validate);
    position: absolute;
    max-width: 70%;
    background-color: white;
    border: 1px solid #c80000;
    border-radius: 13px;
    padding: 4px 25px 4px 10px;
    top: 50%;
    -webkit-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    -o-transform: translateY(-50%);
    transform: translateY(-50%);
    right: 8px;
    pointer-events: none;

    font-family: Poppins-Medium;
    color: #c80000;
    font-size: 13px;
    line-height: 1.4;
    text-align: left;

    visibility: hidden;
    opacity: 0;

    -webkit-transition: opacity 0.4s;
    -o-transition: opacity 0.4s;
    -moz-transition: opacity 0.4s;
    transition: opacity 0.4s;
  }

  .alert-validate::after {
    content: "\f06a";
    font-family: FontAwesome;
    display: block;
    position: absolute;
    color: #c80000;
    font-size: 15px;
    top: 50%;
    -webkit-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    -o-transform: translateY(-50%);
    transform: translateY(-50%);
    right: 13px;
  }

  .alert-validate:hover:before {
    visibility: visible;
    opacity: 1;
  }

  @media (max-width: 992px) {
    .alert-validate::before {
      visibility: visible;
      opacity: 1;
    }
  }

</style>
