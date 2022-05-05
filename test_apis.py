import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import datetime
from app import app
from models import setup_db, Tweet, User

ADMIN_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNYT3BrWVlzUHlfcV9qWVpWU2hKQSJ9.eyJpc3MiOiJodHRwczovL2Rldi1seWhuYjlyMS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDY1NTExNTk0NzE2MTA0NDAwNTgiLCJhdWQiOiJkcmlua3MiLCJpYXQiOjE2NTE3MTk2MTEsImV4cCI6MTY1MTcyNjgwNywiYXpwIjoic3FFRko4MVRQVVJVN3hKMWdaTkc3azFFUm1LTkxCRzAiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTp0d2VldHMiLCJnZXQ6dHdlZXRzIiwiZ2V0OnVzZXIiLCJwYXRjaDp0d2VldHMiLCJwb3N0OnR3ZWV0IiwicG9zdDp1c2VyIl19.JByyaODEK72ZZJIuwO0Y61dD9cLC9CD2eO8w4U1dVYqxxhp4p3Zk91VFbMzdjTOIPiU8Ct0bUHm0HA_wnxzSBhQEl8UTLKsnWYwRtWxplfWslepBIC8KpvokmcpnwjqFRpLz_owKDkmRqaj6x137Kbgw0AJuI42w_kLb0e3jYjnrMxt0jt8SE3d0t_0pPyaVpEcuO_8Fmt1Hu39xCmlnGFGV7lsPGLMntjTJ92J-2vnfbJJfSg5ApSilfxIZjgb8r5VubjHiuP4DcZ1PTWVDw2SsjeUsMV0ANiUeEfcsKzYxb9ExbDfJaF3GqrkJyjq_z3VDvFCK4PwJuqxIuQD3tA'
USER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNYT3BrWVlzUHlfcV9qWVpWU2hKQSJ9.eyJpc3MiOiJodHRwczovL2Rldi1seWhuYjlyMS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI0OGUzYzM0YTc5NTIwMDY5ZDk3ZmQwIiwiYXVkIjoiZHJpbmtzIiwiaWF0IjoxNjUxNzE5Njk1LCJleHAiOjE2NTE3MjY4OTEsImF6cCI6InNxRUZKODFUUFVSVTd4SjFnWk5HN2sxRVJtS05MQkcwIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6dHdlZXRzIl19.Xp8Su8obb65qLeKVkMgKBUIM-506s7Mk7ZdWELarzat4YdVQD8zDwwb7PQ0nXG8jRtWRkbr-MuGpw5qCJDj2t5tQg-zvo_OmWtVfwd80qujuVOL6QbKkPgI0IONh4vvgRJLEKQZylOXg806tAwEan2wtYyvePPbo7njrweeSLUesxckgCd87djmy9uPTTJ2CjhSrAOUIMKYqqp-D1xTHA2RH4mArkE2SO2m2SNGOZ-em7rGmyutCPn0TD6gYXY_gQKF4-8j6ZJJtioQ2vTH9blFdLlVBmZRYX3xTvIMdOkmpBqyu2eYWIy6Zyl3aQNYI4LtBq8EkWYOKxZml7tE4HA'

class TweeterEndpointsTestCase(unittest.TestCase):
    """This class represents unittests for endpoints"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        setup_db(self.app, test=True)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        self.setup_data()
        self.admin_headers = {'Authorization': f'Bearer {ADMIN_TOKEN}'}
        self.user_headers = {'Authorization': f'Bearer {USER_TOKEN}'}

    def setup_data(self):
        """Sets up data in test DB"""
        user = User.query.get(1)
        if not user:
            user = User(username="User 1", joined_ts=datetime.datetime.now())
            user.insert()
        tweet = Tweet.query.get(1)
        if not tweet:
            tweet = Tweet(
                text="This is a tweet",
                user_id=1,
                tweet_ts=datetime.datetime.now()
            )
            tweet.insert()

    def _test_error_404(self, res):
        self.assertEqual(res.status_code, 404)
        self.assertEqual(json.loads(res.data)["message"], "Resource not found")

    def test_get_homepage(self):
        
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        

    def get_tweet(self, headers):
        """Tests successful GET tweet request"""
        res = self.client().get('/tweet/1', headers=headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["tweet"], "This is a tweet")

    def test_get_tweet_admin(self):
        self.get_tweet(self.admin_headers)
    
    def test_get_tweet_user(self):
        """User role is allowed to query tweets"""
        self.get_tweet(self.user_headers)

    def test_get_tweet_not_found(self):
        res = self.client().get('/tweet/100', headers=self.admin_headers)
        self.assertEqual(res.status_code, 404)

    def test_get_user(self):

        res = self.client().get('/user/1', headers=self.admin_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["username"], "User 1")

    def test_get_user_not_found(self):
        res = self.client().get('/user/100', headers=self.admin_headers)
        self.assertEqual(res.status_code, 404)

    def test_add_tweet(self):
        tweet_data = {
            "user_id": 1,
            "tweet_text": "This is a test tweet",

        }
        res = self.client().post('/tweet', data=json.dumps(tweet_data), headers=self.admin_headers) 
        self.assertEqual(res.status_code, 200)

    def test_add_tweet_user(self):
        """User role is not allowed to add tweets"""
        tweet_data = {
            "user_id": 1,
            "tweet_text": "This is a test tweet",

        }
        res = self.client().post('/tweet', data=json.dumps(tweet_data), headers=self.user_headers) 
        self.assertEqual(res.status_code, 403)

    def test_add_tweet_user_id_does_not_exist(self):
        tweet_data = {
            "user_id": 100,
            "tweet_text": "This is a test tweet",

        }
        res = self.client().post('/tweet', data=json.dumps(tweet_data), headers=self.admin_headers) 
        self.assertEqual(res.status_code, 404)

    def test_add_user(self):
        res = self.client().post('/user', data=json.dumps({'username': 'DUMMYUSER'}), headers=self.admin_headers) 
        self.assertEqual(res.status_code, 200)

    def test_add_user_error(self):
        #TODO
        pass

    def test_update_tweet(self):
        tweet_data = {
            "user_id": 100,
            "tweet_text": "This is a test tweet",

        }
        new_tweet = Tweet(user_id=1, text='This is a completely new tweet.', tweet_ts=datetime.datetime.now())
        new_tweet.insert()
        tweet_id = new_tweet.id

        tweet_data = {
            "user_id": 1,
            "tweet_text": "This is an updated tweet",

        }
        res = self.client().patch(f'/tweet/{tweet_id}', data=json.dumps(tweet_data), headers=self.admin_headers)
        self.assertEqual(res.status_code, 200)

        updated_tweet = Tweet.query.get(tweet_id)
        self.assertEqual(updated_tweet.text, "This is an updated tweet")

    def test_update_tweet_error(self):
        tweet_data = {
            "user_id": 1,
            "tweet_text": "This is an updated tweet",

        }
        tweet_id = 10000
        res = self.client().patch(f'/tweet/{tweet_id}', data=json.dumps(tweet_data), headers=self.admin_headers)
        self.assertEqual(res.status_code, 404)

    def test_delete_tweet(self):
        new_tweet = Tweet(user_id=1, text='This is a completely new tweet.', tweet_ts=datetime.datetime.now())
        new_tweet.insert()
        tweet_id = new_tweet.id

        res = self.client().delete(f'/tweet/{tweet_id}', headers=self.admin_headers)
        self.assertEqual(res.status_code, 200)
        query_tweet = Tweet.query.get(tweet_id)
        self.assertIsNone(query_tweet)

    def test_delete_tweet_error(self):
        res = self.client().delete('/tweet/100000', headers=self.admin_headers)
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()