# Consumer App

This is a flask application that can be deployed to App Engine.

The application has two endpoints:

* GET /

    It displays the application home page that will display a list of the top 10 twitter hashtags. A websocket is established between the client and the server when the page is loaded.

* POST /notify

    It parses the push message received from a Pub/Sub topic and broadcasts the object to all the connected clients.

To deploy the application in App Engine follow the following steps

1. Authenticate to Google Cloud

        gcloud auth login

2. Deploy the application to an existing project

        gcloud app deploy --project <PROJECT_ID>

3. Open the application in the browser

        gcloud app browse --project <PROJECT_ID>
