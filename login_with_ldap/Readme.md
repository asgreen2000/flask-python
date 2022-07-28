# document
https://www.mongodb.com/compatibility/mongoengine-pymongo
https://www.mongodb.com/basics/bson
https://docs.mongoengine.org/guide/querying.html#filtering-queries
https://docs.mongoengine.org/guide/querying.html#sorting-queries
https://docs.mongoengine.org/guide/querying.html#pagination-queries
https://docs.mongoengine.org/guide/querying.html#advanced-queries
https://docs.mongoengine.org/guide/querying.html#querying-embedded-documents
https://docs.mongoengine.org/guide/querying.html#querying-embedded-documents-with-dot-notation
https://docs.mongoengine.org/guide/querying.html#querying-embedded-documents-with-dot-notation-and-list-indexes
https://docs.mongoengine.org/guide/querying.html#querying-embedded-documents-with-dot-notation-and-list-indexes-and-dictionary-indexes
# document about flask
https://flask.palletsprojects.com/en/1.1.x/tutorial/database/
# document about jwt
https://jwt.io/
# document about system architecture
https://www.mongodb.com/blog/post/mongodb-3-6-new-system-architecture-for-mongodb-4-0
# document about design pattern for flask
https://flask.palletsprojects.com/en/1.1.x/patterns/
# document about design pattern for mongoengine
https://docs.mongoengine.org/guide/patterns/
# document about restful api
https://flask-restful.readthedocs.io/en/latest/
# document about logger
https://docs.python.org/3/library/logging.html
# document about profiler
https://docs.python.org/3/library/profile.html

# guide user to run this project
# 1. run this project
python3 run.py 
# 2. run this project with development mode
python3 run.py development
# 3. run this project with production mode
python3 run.py production

# guide user to run docker
# 1. run docker
docker build . -t mongoengine-flask-restful-api
docker run -p 5000:5000 -d mongoengine-flask-restful-api
