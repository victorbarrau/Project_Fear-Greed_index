#!/usr/bin/env python
# coding: utf-8

# Get crypto history data from november 2012 to november 2022 and save it in a json file
import finnhub
import json

finnhub_client = finnhub.Client(api_key="xxxx")
dict_crypto=finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1351796400, 1667329200)
print(dict_crypto)

# create a json object from a dictionary
json_object = json.dumps(dict_crypto, indent = 4) 
print(json_object)

# save the json object in a json file
with open("finnhub_api_return.json", "w") as outfile:
    outfile.write(json_object)

# c = close prices, o = open prices, v = volume, t= timestamp

# importing datetime module
import datetime
import time
 
# assigned regular string date
date_time = datetime.datetime(2012, 11, 1, 20, 0)
 
# print regular python date&time
print("date_time =>",date_time)
 
# displaying unix timestamp after conversion
print("unix_timestamp => ",
      (time.mktime(date_time.timetuple())))

# assigned regular string date
date_time = datetime.datetime(2022, 11, 1, 20, 0)
 
# print regular python date&time
print("date_time =>",date_time)
 
# displaying unix timestamp after conversion
print("unix_timestamp => ",
      (time.mktime(date_time.timetuple())))




