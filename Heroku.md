## Deploy Heroku server
1. Set up the Heroku CLI if you haven't done so.
  * Run `sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"`.
  * Run `curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -`.
  * Run `sudo apt-get update`.
  * Run `sudo apt-get install heroku`.
2. Run `heroku login` and login with given credentials.
3. Run `heroku create juicystory`.
4. Run `git add .`
5. Run `git commit -m <message>`, insert your own message.
6. Run `git push heroku <branch>`, insert the branch you want to push to heroku.
  * If you get the error `fatal: 'heroku' does not appear to be a git repository`, run `heroku git:remote -a juicystory` and try again.
7. Run `heroku config:set PORT=8080`.
8. Run `heroku open` to open your webbrowser with the heroku server.
9. Run `heroku logs --tail` if you want to see the logs.f
