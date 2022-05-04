#!/bin/bash
export SQLALCHEMY_DATABASE_URI="postgresql://yjauabkooioqcy:8dc5cbc28cea39f32c6e8199642b468e677927cc72c9c34a6e73234ea489882c@ec2-3-211-6-217.compute-1.amazonaws.com:5432/daeq9fqt6mfgpd"
export SQLALCHEMY_TEST_DATABASE_URI="postgresql://yjauabkooioqcy:8dc5cbc28cea39f32c6e8199642b468e677927cc72c9c34a6e73234ea489882c@ec2-3-211-6-217.compute-1.amazonaws.com:5432/daeq9fqt6mfgpd"
export SQLALCHEMY_TRACK_MODIFICATIONS="false"
export AUTH0_DOMAIN='dev-lyhnb9r1.us.auth0.com'
export ALGORITHM='RS256'
export API_AUDIENCE='drinks'
echo "setup.sh script executed successfully!"