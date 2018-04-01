# 2018-JuicyStory

## Dependencies
* Python3
* Django
* django_cron app
* widget_tweaks app

## Installation Instructions

* Make sure you have all the dependencies
* (Linux/MacOS) Set up a cron job
  * Type `crontab -e` to the console
  * Add the following line to the file with the correct paths. <ANY PATH> can be anywhere in your computer.
    > \* * * * * python3 <PROJECT PATH>/2018-JuicyStory/authdemo/manage.py runcrons >> <ANY PATH>/.cronlog
* (Windows) [Schedule a task](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc748993(v=ws.11)) that basically runs `manage.py runcrons` every single minute

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

