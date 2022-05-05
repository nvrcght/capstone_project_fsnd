#!/usr/bin/env python
"""
A simple app to create a JWT token.
"""
import os
import logging
import datetime
import functools
import jwt
from flask_cors import CORS
from flask import Flask, jsonify, request, abort
from models import setup_db, User, Tweet
from auth import requires_auth, AuthError
import json

def init_app(app_, test=False):
    # create and configure the app
    setup_db(app_, test=test)
    CORS(app_)
    return app_

app = Flask(__name__)
init_app(app)

@app.route('/', methods=["GET"])
def home():
    """Test endpoint"""
    res = "hello this is working now"
    return jsonify(res)

@app.route('/tweet/<tweet_id>', methods=["GET"])
@requires_auth('get:tweets')
def get_tweet(payload, tweet_id):
    tweet = Tweet.query.get(tweet_id)
    if tweet:
        return jsonify(tweet.describe())
    else:
        abort(404)

@app.route('/user/<user_id>', methods=["GET"])
@requires_auth('get:user')
def get_user(payload, user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.describe())        
    else:
        abort(404)
   
@app.route('/tweet', methods=["POST"])
@requires_auth('post:tweet')
def add_tweet(payload):
    
    data = json.loads(request.data)
    user_id = data["user_id"]
    if not User.query.get(user_id):
        abort(404)

    tweet = Tweet(
        text=data["tweet_text"],
        user_id=user_id,
        tweet_ts=datetime.datetime.now()
    )
    try:
        tweet.insert()
        res = {"success": True, "data": data}
    except:
        tweet.rollback()
        res = {"success": False}
    return jsonify(res)

@app.route('/user', methods=["POST"])
@requires_auth('post:user')
def add_user(payload):
    data = json.loads(request.data)

    if "username" not in data:
        abort(422)
    user = User(username=data["username"], joined_ts=datetime.datetime.now())
    try:
        user.insert()
        res = {"data": user.describe()}
    except:
        user.rollback()
        res = {"success": False}
    return jsonify(res)


@app.route('/tweet/<tweet_id>', methods=["PATCH"])
@requires_auth('get:tweets')
def update_tweet(payload, tweet_id):
    data = json.loads(request.data)

    tweet = Tweet.query.get(tweet_id)
    if "tweet_text" not in data:
        abort(422)
    if tweet:
        tweet.text = data["tweet_text"]
        tweet.tweet_ts = datetime.datetime.now()
        try:
            tweet.update()
            res = {"success": True, "data": tweet.describe()}
        except:
            tweet.rollback()
            abort(500)
    else:
        abort(404)
    return jsonify(res)

@app.route('/tweet/<tweet_id>', methods=["DELETE"])
@requires_auth('delete:tweets')
def delete_tweet(payload, tweet_id):

    tweet = Tweet.query.get(tweet_id)
    if tweet:
        try:
            tweet.delete()
            res = {"success": True}
        except:
            tweet.rollback()
            abort(500)
    else:
        abort(404)
    return jsonify(res)    


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404
        
@app.errorhandler(422)
def malformed(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Malformed request"
    }), 422

@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error["description"]
    }), error.status_code


@app.errorhandler(500)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 500

if __name__ == '__main__':
    app.run()


