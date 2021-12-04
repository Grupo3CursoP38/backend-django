@echo OFF

heroku login
heroku container:login
heroku container:push web --app rentalproject-auth-ms
heroku container:release web --app rentalproject-auth-ms

exit