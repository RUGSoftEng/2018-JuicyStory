## Deploy Heroku server
* Set up the Heroku CLI if you haven't done so.
  * Run `sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"`
  * Run `curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -`
  * Run `sudo apt-get update`
  * Run `sudo apt-get install heroku`
* Run `heroku login` and login with given credentials.
* Run `heroku create juicystory`.
* Run `git add .`
* Run `git commit -m <message>`, insert your own message.
* Run `git push heroku <branch>`, insert the branch you want to push to heroku.
  * If you get the error `fatal: 'heroku' does not appear to be a git repository`, run `heroku git:remote -a juicystory` and try again.
* Run `heroku config:set PORT=8080`
* Run `heroku ps:scale web=1`
* Run `heroku open`
* Run `heroku logs --tail` (to check out the logs)
