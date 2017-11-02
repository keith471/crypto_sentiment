# To Set Up This Bad-Boy
## Get code and download dependencies
```
git clone https://github.com/keith471/crypto_sentiment.git
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Run setup script
###### Currently supported environments are "test" and "local"
```
python setup.py [env]
```


# Mongodb 
## Run db locally in docker container (using example username/password)
###### Note: you shoudn't have to do this if you are running in the test environment
```
docker run -d -p 27017:27017 -p 28017:28017 -e MONGODB_USER="frances" -e MONGODB_DATABASE="crypto" -e MONGODB_PASS="thuglife" tutum/mongodb
```
## Starting existing db
```
docker start [container-id]
```
## Run mongodb shell locally
```
mongo [db_name] -u [username] -p [password]
```
## Run mongobd shell with remote 
mongo [host]:[port]/[db_name] -u [username] -p [password]


# Tweet collector
```
python Stocktwits.py [env]
```

# Sentiment analyzer
```
python run.py [env]
```

# Web visualizer
## To start the webapp
###### You must first have the bower package manager installed
```
cd static && bower install
cd ..
python server.py [env]
```


## Other Resources
*Python Mongo ORM docs: https://mongoengine-odm.readthedocs.io/guide/defining-documents.html#fields
