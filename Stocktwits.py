# WARN: THIS FILE CREATED FROM JUYPTER_NOTEBOOK, DO NOT MODIFY
# coding: utf-8

# In[12]:


import requests
from mongoengine import connect
from models import Coin, TextSummary, StockTwitsCursor


# In[13]:


connect(
    db='crypto',
    username='frances',
    password='thuglife',
    host='mongodb://127.0.0.1'
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
        posted_at=msg['created_at'],
    ).save()


# In[14]:


for msg in r.json()['messages']:
    save_msg(msg)
