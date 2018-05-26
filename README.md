# 2018-JuicyStory
[![Build Status](https://travis-ci.org/RUGSoftEng/2018-JuicyStory.svg?branch=v0.5)](https://travis-ci.org/RUGSoftEng/2018-JuicyStory)

## Django tutorial
Note that you might need to use `python3` instead of `python` depending on our installation
* Make a django app `python manage.py startapp <name>`
* Make a djnago superuser `python manage.py createsuperuser`
* Run the django server `python manage.py runserver` go to `http://localhost:8000/`
* If changes were made to the database perform `python manage.py makemigrations` followed by `python manage.py migrate`
* The admin section can be found on `/admin/` currently there are two superusers
  * Username "george" password "a1234567"
  * Username "tolga" password "a1234567"
* The instagram database contains one test account 
  * Instagram Username "testy8101" password "%3zf(^u7YX" token "r"

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
* Verify a JWT token `http://localhost:8000/api/verify-token/` POST ANY
* Filter Instagram users `http://localhost:8000/api/filter-iusers/` GET JWT
  * Example `http://localhost:8000/api/filter-iusers/?id=&username=&password=&owner=` GET JWT
* Create a new instagram user `http://localhost:8000/api/create-iusers/` POST
* Get an instagram user using their username `http://localhost:8000/api/rud-iusers/<username>/` GET PUT DELETE JWT
  * Example  `http://localhost:8000/api/rud-iusers/testy8101/`
* Register a JuicyStory user `http://localhost:8000/entry/register-user/` POST JWT
* Login a JuicyStory's user credentials `http://localhost:8000/entry/login-user/` POST ANY
* Get statistics regarding followers and view count `http://localhost:8000/statistics/<username>/<from>/<until>/`
  * Example `http://localhost:8000/statistics/testy8101/1526109291/1526413193/` GET  JWT
  * NOTE that the fbtoke expires every three hours.
* Get the DM's from a specific InstagramUser `http://localhost:8000/api/Incoming/?instagram_username=&get_DM=` GET JWT
  * Example `http://localhost:8000/api/Incoming/?instagram_username=testy8101&get_DM=True`

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

