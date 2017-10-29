##Coin: to represent a cryptocurrency in the system
*ticker (type=string, example=BTC, indexed=true)
*name (type=string, example=Bitcoin)
*validationMethod (type=string, example=PoW, indexed=true)
*hashingAlgorithm (type=string, example=sha256, indexed=true)

##Price: an object that records the price of a cryptocurrency in USD.
*coin (type=Coin, indexed=true)
*price (type=double)
*createdAt (type=timestamp, indexed=true)

##TextSummary: an object that records processed information related to a post or text document about cryptocurrency.
*coin (type=Coin, indexed=true)
*rawText (type=string)
*sentiment (type=integer, example=1)
*tags (type=list<string>, example=[BULLISH, HAS_IMAGE], indexed=true)
*userId (type=long, indexed=true)
*reshareCount (type=integer)
*reshareUsers (type=list<long>, example=[123, 456]) 
*postedAt (type=timestamp, indexed=true)
*createdAt (type=timestamp, indexed=true)
*updatedAt (type=timestamp, indexed=true)

##StockTwitsCursor: an object that will allow us to track where we left off in the collection of tweets. We could save one after every collection to track the range of data collected.
*more (type=boolean)
*since (type=long)
*maximum (type=long)
*createdAt (type=timestamp, indexed=true)
