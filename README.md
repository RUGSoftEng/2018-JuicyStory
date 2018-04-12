# 2018-JuicyStory

## Dependencies
* Python3
* Django
* django_cron app
* widget_tweaks app
* rest_framework
* rest_framework.authtoken
* django_filters

## Installation Instructions

* Make sure you have all the dependencies
* (Linux/MacOS) Set up a cron job
  * Type `crontab -e` to the console
  * Add the following line to the file with the correct paths. <ANY PATH> can be anywhere in your computer.
    > \* * * * * python3 <PROJECT PATH>/2018-JuicyStory/authdemo/manage.py runcrons >> <ANY PATH>/.cronlog
* (Windows) [Schedule a task](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc748993(v=ws.11)) that basically runs `manage.py runcrons` every single minute

## Adding an API-Endpoint
* First, create the desired model in the app
* We need to serialize it, so that i can be viewed as JSON
	* create file `serializer.py` and import `from rest_framework import serializers`
	* also import the desired model from `.models`
	* create a class ie `<name>Serializer` and pass in the arguments `serializers.ModelSerializer` . Indent another class called `Meta` along with the model and fields ie 	`model = <name>` & `fields = '__all__`
	* create file `viewset.py` and import the model long with the serializer class `<name>Serializer`. Create class `<name>ViewSet(viewsets.ModelViewSet):` with the parameter passed from `from rest_framework import viewsets`. Set two variables ie `queryset = <name>.objects.all()` & `serializer_class = <name>Serializer`.
	* inside the default app `authdemo` create file `routers.py` and import the ViewSet from the app that you set it in.
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
  * Go to [http://localhost:8000/admin/](http://localhost:8000/admin/)
  * Add an Instagram User with username `testy8101`, owner `<SUPERUSER>` and the access token `7199328359.a81a42f.61b3bb86b8f647cf9c7bf75a42566fee`

