#!/bin/bash
export SQLALCHEMY_DATABASE_URI="postgresql://hetznfjkmvarqt:fdc44632cd98161ac6b08b887b1a86efc82cf3bfc275c2ff1579f5d8c1f5ea06@ec2-54-172-175-251.compute-1.amazonaws.com:5432/d3djidrgqg7qot"
export SQLALCHEMY_TEST_DATABASE_URI="postgresql://hetznfjkmvarqt:fdc44632cd98161ac6b08b887b1a86efc82cf3bfc275c2ff1579f5d8c1f5ea06@ec2-54-172-175-251.compute-1.amazonaws.com:5432/d3djidrgqg7qot"
export SQLALCHEMY_TRACK_MODIFICATIONS="false"
export AUTH0_DOMAIN='dev-lyhnb9r1.us.auth0.com'
export ALGORITHM='RS256'
export API_AUDIENCE='drinks'
echo "setup.sh script executed successfully!"