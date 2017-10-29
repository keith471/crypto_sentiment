# To Set Up This Bad-Boy

```
git clone https://github.com/keith471/crypto_sentiment.git
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

# Run db locally in docker container (using example username/password)
```
docker run -d -p 27017:27017 -p 28017:28017 -e MONGODB_USER="frances" -e MONGODB_DATABASE="crypto" -e MONGODB_PASS="thuglife" tutum/mongodb
```
** Run mongodb shell locally
```
mongo crypto -u frances -p thuglife
```

# To start the web api
```
export FLASK_APP=server.py
flask run
```

##Other Resources
*Python Mongo ORM docs: https://mongoengine-odm.readthedocs.io/guide/defining-documents.html#fields


