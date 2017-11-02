# WARN: THIS FILE CREATED FROM JUYPTER_NOTEBOOK, DO NOT MODIFY
# coding: utf-8

# In[12]:

import requests
from mongoengine import connect
from db.models import Coin, TextSummary, StockTwitsCursor
from datetime import *
from environment import Environment
from argparse import ArgumentParser

# In[13]:

#===============================================================================
# Arugment parsing
#===============================================================================

parser = ArgumentParser()
parser.add_argument('env', type=str, action='store', help='the environment')
parser.add_argument('--h', action='store_true', help='if set, usage will be printed out')
args = parser.parse_args()

## TODO error checking on the args

if args.h:
    parser.print_help()

print()

#===============================================================================
# Connecting to MongoDB
#===============================================================================

env = Environment(args.env)
connect(
    db=env.DB_NAME,
    username=env.DB_USERNAME,
    password=env.DB_PASSWORD,
    host='mongodb://' + env.DB_HOST
)

# In[3]:


# make sure setup.py was run first
btc_coin = Coin.objects(ticker='BTC').first()
assert(btc_coin is not None)


# In[4]:


# lets ignore this for now
# st_cursor = StockTwitsCursor.objects().first()
# assert(st_cursor is not None)

# and just get a dump of the latest 30 messages
r = requests.get('https://api.stocktwits.com/api/2/streams/symbol/BTC.json')
assert(r.status_code == 200)


# In[7]:


def save_msg(msg):
    TextSummary(
        coin=btc_coin,
        raw_text=msg['body'],
        posted_at=datetime.strptime(msg['created_at'], "%Y-%m-%dT%H:%M:%SZ" ),
    ).save()

# In[14]:


for msg in r.json()['messages']:
    save_msg(msg)
