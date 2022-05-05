
# Heroku URL

https://udacity-capston.herokuapp.com/

# Authentication

Tokens for 2 roles are provided in test_apis.py

ADMIN_TOKEN represents admin user.
USER_TOKEN represents user who has limited permissions.


# Tweeter Light APP documentation

## Tweeter Light

Tweeter Light is a simple application that allows posting tweets.

The app has 2 roles: user and admin.
User can only view tweets and users, wherease adming can create, update and delete tweets and create users.


# Dependencies
## Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs

## PIP Dependencies
Install dependencies by running requirements.txt:

pip install -r requirements.txt


## API Documentation



### Endpoints

`GET '/api/v1.0/tweet/:tweet_id'`

- Fetches a dictionary that represents a tweet
- Parameters  
    No parameters.
- Returns: An object that represents a tweet

```json
{
    "posted user": 1,
    "tweet": "This is a tweet",
    "tweet id": 1,
    "tweet timestamp": "Wed, 27 Apr 2022 10:29:31 GMT"
}
```

`GET '/api/v1.0/user/:user_id'`

- Fetches a dictionary that represents a user
- Parameters  
    No parameters.
- Returns: An object that represents a user

```json
{
    "joined": "Wed, 27 Apr 2022 10:26:26 GMT",
    "user id": 1,
    "username": "User 1"
}
```

`POST '/api/v1.0/tweet'`

- Creates new tweet.
- Parameters  
    `user_id`  
        Specifies which user created a tweet.
    `tweet_text`
        Text of a tweet
- Returns: Representation of posted tweet. Otherwise raises.

```json
{
    "posted user": 1,
    "tweet": "This is a tweet",
    "tweet id": 1,
    "tweet timestamp": "Wed, 27 Apr 2022 10:29:31 GMT"
}
```

`POST '/api/v1.0/user'`

- Creates new user.
- Parameters  
    `username`  
        Specifies username.
- Returns: Representation of created user. Otherwise raises.

```json
{
    "username": "DUMMYUSER",
    "user id": 1,
    "joined": "Wed, 27 Apr 2022 10:29:31 GMT"
}
```

`PATCH '/api/v1.0/tweet'`

- Creates new tweet.
- Parameters  
    `user_id`  
        Specifies which user created a tweet.
    `tweet_text`
        Text of a tweet
- Returns: Representation of posted tweet. Otherwise raises.

```json
{
    "posted user": 1,
    "tweet": "This is an updated tweet",
    "tweet id": 1,
    "tweet timestamp": "Wed, 27 Apr 2022 10:29:31 GMT"
}
```

`DELETE '/api/v1.0/tweet/:tweet_id'`

- Deletes a tweet by ID.
- Parameters  
    No parameters.
- Returns: Successful response if delete was successful, otherwise raises.




### Error Handling

Errors are returned as JSON objects in the following format:
```json
{
    "success": false, 
    "error": 404,
    "message": "Resource not found"
}
```
The API will return three error types when requests fail:

401: Unauthorized
403: Forbidden
404: Resource not found  
422: Malformed Data Request  
500: Internal Server Error  
