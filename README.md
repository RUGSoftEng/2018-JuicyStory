# 2018-JuicyStory
[![Build Status](https://travis-ci.org/RUGSoftEng/2018-JuicyStory.svg?branch=v0.5)](https://travis-ci.org/RUGSoftEng/2018-JuicyStory)

## Django tutorial
Note that you might need to use `python3` instead of `python` depending on our installation
* Make a django app `python manage.py startapp <name>`
* Make a djnago superuser `python manage.py createsuperuser`
* Run the django server `python manage.py runserver` go to `http://localhost:8000/`
* If changes were made to the database perform `python manage.py makemigrations` followed by `python manage.py migrate`
* The instagram database contains one test account 
  * Instagram Username "testy8101" password "%3zf(^u7YX"

## Port routing
* Find out your local ip address (ipconfig on windows, ifconfig on linux. It's the one that goes 192....)
* Forward the port to your local ip address through your router interface (google port forwarding, it's easy)
* Start django server with python3 manage.py runserver 0.0.0.0:[PORT]. Use the port that you have forwarded. 8000 works alright. 0.0.0.0 part is important!!
* Add your ip adddress (external ip address. google to find) to the allowed hosts in django settings file.
* Add that ip address also to the redirect urls on instagram api
* Go to [IP]:[PORT] on your browser, should be working.
* Voila! Don't forget to stop routing the port after you are done developing.

## Dependencies
All dependencies can be found in the requirements.txt.
In order to verify if the dependencies are valid, proceed with the following:
* Delete the current `requirements.txt` file
  * CD into the directory that used to contain `requirements.txt`
* run `pip freeze > requirements.txt`
* run `pip install -r requirements.txt`
  * Be patient there are a lot of dependencies to be downloaded

## Installation Instructions
* Make sure you have all the dependencies
* (Linux/MacOS) Set up a cron job
  * Type `crontab -e` to the console
  * Add the following line to the file with the correct paths. <ANY PATH> can be anywhere in your computer.
    > \* * * * * python3 <PROJECT PATH>/2018-JuicyStory/application/manage.py runcrons >> <ANY PATH>/.cronlog
* (Windows) [Schedule a task](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc748993(v=ws.11)) that basically runs `manage.py runcrons` every single minute

## Api-Authentication
Two urls have been created that retrieve and validate a JWT token that can be used for authentication.
In order to perform requests the following can be done:
* run `curl -X POST -d "username=<admin username>&password=<admin password>" http://localhost:8000/api/get-token/` 
  * If successful it returns the dictionary `{"token" : "<token>"}`.
* Make a request to a authentication protected uri, ie. `curl -H "Authorization: JWT <token>" http://localhost:8000/api/rud-iusers/<instagram username in the database>/`
  * if successful it returns the relevant jason data `{"id":1,"username":"<instagram username in the database>","password":"","fbtoken":"","fbid":"","access_token":"","login_session":null,"username_id":null,"owner":2}`

## Api-Endpoints
The following list contains information about the api end-points of JuicyStory.
They are written using the following format:
* `<Description>` `<Url>` `<CRUD>` `<?Access Level?>`
* Receive a JWT token `http://localhost:8000/api/get-token/` POST ADMIN
  * post `<usernmae>` & `<password>` ie `username=george&password=a1234567`
  * Data retrived `"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imdlb3JnZSIsImV4cCI6MTUyNzgwMjk3NCwiZW1haWwiOiIifQ.FVFhbbeEAS_CC97lZl7mjlNeKBzl3_XMsBtImuvMw4s"`
* Verify a JWT token `http://localhost:8000/api/verify-token/` POST ANY
  * post `<token>`
  * Data retrieved `"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imdlb3JnZSIsImV4cCI6MTUyNzgwMjk3NCwiZW1haWwiOiIifQ.FVFhbbeEAS_CC97lZl7mjlNeKBzl3_XMsBtImuvMw4s"
}`
* Filter Instagram users `http://localhost:8000/api/filter-iusers/` GET JWT
  * filter by `<id>`, `<username>`, `<password>`, `<owner>` `id=&username=&password=&owner=`
  * Note that the filter has the potential to receive the whole database of instagram users
  * (1) Data retrieved `"id": 7,
        "username": "testy8101",
        "password": "MFxH*854&t",
        "fbtoken": "EAACEdEose0cBAPq7nwF9HUcNqAkty2N8FoyqJo40yBWyiOYB6xq4N3LQsJFjmk92wzN1b5qS3O7FcG0UNfXd18mmFRBohhazvZB5QKuyibd1jDOaxTrJQc1HpCZAASY6Jl2VFeBB8mlhAd068TzGlYFK5QA88OGHHVxCNZAZC6QzqbRACQ9Hs56HaCAZCRAbPvdNjiu5r4fqD6siTVzrGVWZCg6Y8EEZAgZD",
        "fbid": "160447804650500",
        "access_token": "7199328359.a81a42f.61b3bb86b8f647cf9c7bf75a42566fee",
        "login_session": "gAJ9cQAoWAkAAABjc3JmdG9rZW5xAVggAAAAR1BEcGNJcHdQRmVSVTFERzFkT2JyMElvQ2xZNU96M0dxAlgHAAAAZHNfdXNlcnEDWAkAAAB0ZXN0eTgxMDFxBFgKAAAAZHNfdXNlcl9pZHEFWAoAAAA3MTk5MzI4MzU5cQZYBAAAAGlnZmxxB1gJAAAAdGVzdHk4MTAxcQhYEgAAAGlzX3N0YXJyZWRfZW5hYmxlZHEJWAMAAAB5ZXNxClgDAAAAbWNkcQtYAQAAADNxDFgDAAAAbWlkcQ1YHAAAAFd3dlM3Z0FCQUFFMmg1UGdQc2hySFlFZ05BSmJxDlgDAAAAcnVycQ9YAwAAAEZUV3EQWAkAAABzZXNzaW9uaWRxEVjmAQAASUdTQzYzMGVhYzg5MGMwY2Q3YTI4NzE0MzhlMDdkZDIyY2I2MjI3YzQyOTM0MDU1NWNjN2MxOWFiNGMwNDk2ZGEyZWMlM0ExV3Q0SzhwQm0xY0s4QkhMSmgxc09BV0dtcHkzV0pxayUzQSU3QiUyMl9hdXRoX3VzZXJfaWQlMjIlM0E3MTk5MzI4MzU5JTJDJTIyX2F1dGhfdXNlcl9iYWNrZW5kJTIyJTNBJTIyYWNjb3VudHMuYmFja2VuZHMuQ2FzZUluc2Vuc2l0aXZlTW9kZWxCYWNrZW5kJTIyJTJDJTIyX2F1dGhfdXNlcl9oYXNoJTIyJTNBJTIyJTIyJTJDJTIyX3BsYXRmb3JtJTIyJTNBMSUyQyUyMl90b2tlbl92ZXIlMjIlM0EyJTJDJTIyX3Rva2VuJTIyJTNBJTIyNzE5OTMyODM1OSUzQWxVVlVOMzRkSDd5YjhhOGxJbVFhWWZ2cUlnb08waHpyJTNBOGE4YmM2ZjI0NDNlYWY4MGEzM2E1NWM1YTA1OTM2YTBkNTYzZDMyMTk0ZDFhYmNlZWRmMGRhZGFkODcyZTcyZCUyMiUyQyUyMmxhc3RfcmVmcmVzaGVkJTIyJTNBMTUyNzUwMTU1MS4wMDg1NzIxMDE2JTdEcRJYBQAAAHNoYmlkcRNYBQAAADE0NDc1cRRYBQAAAHNoYnRzcRVYEgAAADE1Mjc1MDE1NTQuNTIyMTg5MXEWWAYAAAB1cmxnZW5xF1hQAAAAInt0aW1lOiAxNTI3NTAxNTU0XDA1NCA4MC4xMTQuMTc4LjE3MzogOTE0M306MWZORXZxOnotazFnQ3FnZjgxUTc4eTRwZWo1OXJ1MW0yOCJxGHUu",
        "username_id": 7199328359,
        "owner": 1`
  * Example `http://localhost:8000/api/filter-iusers/?id=&username=&password=&owner=` GET JWT
* Create a new instagram user `http://localhost:8000/api/create-iusers/` POST JWT
  * You can post the same fields as mentioned above in (1).
* Get an instagram user using their username `http://localhost:8000/api/rud-iusers/<username>/` GET PUT DELETE JWT
  * You can post, delete and update for that specific instagram account using the fields mentioned in (1)
  * Example  `http://localhost:8000/api/rud-iusers/testy8101/`
* Register a JuicyStory user `http://localhost:8000/api/register-user/` POST JWT
  * post `<username>`, `<password>` post `username=test12312&password=a12345678`
  * Data retrieved `"username": "test12312"`
* Login a JuicyStory's user credentials `http://localhost:8000/api/login-user/` POST ANY
  * post `<username>`, `<password>` post `username=george&password=a1234567`
  * Data retrieved `"username": "george",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imdlb3JnZSIsImV4cCI6MTUyNzgwNDA3OCwiZW1haWwiOiIifQ.BfopKimtO6yCecgBoNGiK7Tva05Oq0_L6vXJTf_hsbc"`
* Get statistics regarding followers and view count `http://localhost:8000/api/stats/<username>/<from>/<until>/`
  * Example `http://localhost:8000/api/stats/testy8101/1526109291/1526413193/` GET JWT
  * NOTE that the fbtoken expires every three hours.
  * Data retrieve `{
        "name": "follower_count",
        "period": "day",
        "values": [
            {
                "value": 0,
                "end_time": "2018-05-13T07:00:00+0000"
            },
            {
                "value": 0,
                "end_time": "2018-05-14T07:00:00+0000"
            },
            {
                "value": 0,
                "end_time": "2018-05-15T07:00:00+0000"
            }
        ],
        "title": "Follower Count",
        "description": "Total number of unique accounts following this profile",
        "id": "17841406970799916/insights/follower_count/day"
    }`
* Get the array of images of ones instagram story `http://localhost:8000/api/story/<iusername>/` GET JWT
  * Example `http://localhost:8000/api/story/testy8101/`
  * Data retrieved `"images": [
        "https://scontent.xx.fbcdn.net/v/t51.12442-15/33630403_205477556844157_8497524797213769728_n.jpg?_nc_cat=0&oh=0dfd616fc02d400c5bb5f0c88fc49fa0&oe=5B8603A0"
    ]`
* Get statistics regarding the story metrics of ones instagram account `http://localhost:8000/api/metrics/<iusername>/`
  * Example `http://localhost:8000/api/metrics/testy8101/`
  * Data retrieved `{
    "exits": 0,
    "impressions": 0,
    "reach": 0,
    "replies": 0,
    "taps_forward": 0,
    "taps_back": 0
}`
  * Currently not operational since further testing needs to be conducted using a 'bigger' instagram account.
* Get the DM's from a specific InstagramUser `http://localhost:8000/api/get-dms/<iusername>/` GET JWT
  * Example `http://localhost:8000/api/get-dms/testy8101/`
  * Data retrieved `"dms": {
        "1528045852336149": "https://scontent-ams3-1.cdninstagram.com/vp/36ed9d85f32eaaeeafff3d9a0984bb5c/5BB7270F/t51.2885-15/e35/33210231_271941783549154_471935718063603712_n.jpg?ig_cache_key=MjgxODc0NzA3NzA5MzgzMTcxNzMyNDIwODg4OTgxNjY3ODQ%3D.2"
    }`
  * On the above mentioned dictionary each entry has a unix timestamp followed by the url to that image

## Adding an API-Endpoint
* First, create the desired model in the app
* We need to serialize it, so that i can be viewed as JSON
	* create file `serializer.py` and import `from rest_framework import serializers`
	* also import the desired model from `.models`
	* create a class ie `<name>Serializer` and pass in the arguments `serializers.ModelSerializer` . Indent another class called `Meta` along with the model and fields ie 	`model = <name>` & `fields = '__all__`
	* create file `viewset.py` and import the model long with the serializer class `<name>Serializer`. Create class `<name>ViewSet(viewsets.ModelViewSet):` with the parameter passed from `from rest_framework import viewsets`. Set two variables ie `queryset = <name>.objects.all()` & `serializer_class = <name>Serializer`.
	* inside the default app `core` create file `routers.py` and import the ViewSet from the app that you set it in.
	* import `from rest_framework import routers` and set `router = routers.DefaultRouter()`. Now register the router by `router.register(r’<title>’, <name>ViewSet)` where title should be a meaningful name for your Data.
* Now if you go to `http://127.0.0.1:8000/api/` you should see all the available endpoints along with a link to your included Api. ie `http://127.0.0.1:8000/api/<title>/`

## Heroku
* perform `heroku login`
  * pass credentials email: `j.m.de.jong.14@student.rug.nl`, password: `Linnaeusborg 5118`.

## Running the Application (for testing purposes)
* Make sure you migrate everytime you start working on a new branch
  * `python3 manage.py migrate`
* If you haven't done so, create a super user
  * `python3 manage.py createsuperuser`
* Run the server
  * `python3 manage.py runserver 0.0.0.0:8000`
* If it doesn't exist, add an instagram account 
  * Go to [http://localhost:8000/admin/](http://localhost:8000/admin/) and login with the superuser account you have just created
  * Add an Instagram User with 
    * username `testy8101`
    * owner `<SUPERUSER>` 
    * password `MFxH*854&t`
    * access token `7199328359.a81a42f.61b3bb86b8f647cf9c7bf75a42566fee`
    * FBToken `EAACEdEose0cBAImmJpxQg3nWm2AV04RBa2UWQNqU9GWlTZARPVexVhTxUZABoMt8fN2Kvok8Tjbjm2Db0CKFXmcf7jn4a3WK0ZCDjpZBWxjNyihZBwdRejgCxNtunYUuVkZChKZAZCrahWBe5QSghm8BDjkdY5JPyF2g6Po1oZCxEJg4HyTeNjGZAZA0f5iT2xu9fzrNFSddPHe0NFJJ6Mhxknb1jvPzQOAsAsZD`
    * FBid `160447804650500`

