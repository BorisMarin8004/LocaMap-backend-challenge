# LocaMap-backend-challenge

Welcome to our Engineering Challenge repository 🖖

If you found this repository it probably means that you are participating in our recruitment process. Thank you for your time and energy.

Please fork this repo before you start working on the challenge, read it careful and take your time and think about the solution. Also, please fork this repository because we will evaluate the code on the fork.

This is an opportunity for us both to work together and get to know each other in a more technical way. If you have any doubts please open and issue and we'll reach out to help.

## Challenge Objective

At Abord, Travel is the very core of our product. We have deep integrations of maps and locations almost on every screen within the app. Your objective for this challenge is to build an API that takes a latitude and longitude coordinate pair and return with the name of the country.

There are plenty of ways this can be implemented - We only need you to give us one.
Feel free to use any third party resources or APIs as long as you document about it in the ReadME.

> HAVE FUN!!

### Start writing here...

### How to start server with API
Run "docker-compose up --build" in "LocaMap-backend-challenge" directory. This will start a docker container.

### API requests
The API uses opencagedata API to convert coordinates to country. 
In order to get the country by coordinates, the user needs to specify "lat" and "lng" variables(latitude and longitude respectively).
Example query "http://127.0.0.1:5000/api/geocoding?key=key&lat=47&lng=7" would return:
{
    "country": "Switzerland"
}
The API also handles the case when coordinates are in the ocean for example:
For query "http://127.0.0.1:5000/api/geocoding?key=key&lat=87&lng=7" would return:
{
    "country": null
}

### Security
The key for API requests is currently set to "key", which can be changed in the api.py file. We can also set different keys for any other APIs we might use. I also recommend changing "--host=0.0.0.0" option in the flask to docker container IP, once we want to go into production for extra security.

### Scalability 
In the current state, the backend can be easily scaled. For example, if we would like to add another API, we can just add it to the web_api folder as a separate python file, which we would like to app.py using Blueprint. We can also add any number of local databases and link them to app.py using Blueprint as well.





