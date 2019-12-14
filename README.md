# Stress Testing an AWS Machine Learning Web Application
Alexander Dougherty, Carlos Olea, Quinton Hoffman

## Branches
- master: master has the local implementation which will run the code locally
- prod: prod has the implementation which will run on the first EC2 instance which does not have docker
- prod2: prod2 has the implementation which will run on the second EC2 instance with docker

## How to Use
You will be able to run the application locally, but the EC2 instances will be shut down to save money.
In general, the static website was hosted at http://vanderbilt-ccfinal-team2.s3.amazonaws.com/index.html.
To run locally, make sure you are on the master branch. Open a terminal and cd to the
cloud_computing_react directory. Run yarn start and the front end should start on localhost:3000.
Then open another terminal and cd to cloud_computing_flask directory. Run python app.py and the Flask
application will start up at localhost:5000. You should then be able to submit requests on the
frontend and see the data being processed on the backend.
