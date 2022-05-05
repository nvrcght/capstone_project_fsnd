#!/bin/bash
export DATABASE_URL="postgresql://zgnixvdsixthhn:418a90d2c780e2595f502b62860566d6db3177ecfd9eb9397062196cdb60a3af@ec2-18-210-64-223.compute-1.amazonaws.com:5432/d70aam0q9vam5q"
export SQLALCHEMY_TEST_DATABASE_URI="postgresql://zgnixvdsixthhn:418a90d2c780e2595f502b62860566d6db3177ecfd9eb9397062196cdb60a3af@ec2-18-210-64-223.compute-1.amazonaws.com:5432/d70aam0q9vam5q"
export SQLALCHEMY_TRACK_MODIFICATIONS="false"
export AUTH0_DOMAIN='dev-lyhnb9r1.us.auth0.com'
export ALGORITHM='RS256'
export API_AUDIENCE='drinks'
echo "setup.sh script executed successfully!"