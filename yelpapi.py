from yelpapi import YelpAPI
from yelp.api.v2 import Yelp
import json
import collections
import pandas as pd
import numpy as np
from pprint import pprint

client_id = 'gKE6HPzdUYmxVXKTJ2xIqA'
client_secret = 'ZIXyQ8dhu2CnRJ8b4m5uD5GAg81RjvIIIbe4Z9wfOVtwZW1gxWITj2VI81QRHO98'

consumer_key = 'uOZv9SZSepVUp2s29CyWmA'
consumer_secret = 'akcl2MJFNuJE9lfNlG4fI3Y_Oj8'
token = 'kqFnFl_rs7IFhQEyxBZTzq0XZbOqea65'
token_secret = '-z5NBbAGcO4Do_cYZfrbkR5oik4'

# cons key, cons secret, token, token_secret
yelp_api = YelpAPI(consumer_key, consumer_secret,token,token_secret)

?yelp_api

# https://pypi.python.org/pypi/ezapi-yelp

def convert(x):
    ''' Convert a json string to a flat python dictionary
    which can be passed into Pandas. '''
    ob = json.loads(x)
    for k, v in ob.items():
        if isinstance(v, list):
            ob[k] = ','.join(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                ob['%s_%s' % (k, kk)] = vv
            del ob[k]
    return ob

# THIS WORKS
# https://stackoverflow.com/questions/1254454/fastest-way-to-convert-a-dicts-keys-values-from-unicode-to-str

#AC modified to encode utf-8
def convert(data):
    if isinstance(data, basestring):
        #return str(data)
        return data.encode('utf-8')
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

yelp = Yelp(
    consumer_key,
    consumer_secret,
    token,
    token_secret,
)

# ============ start here
east_village = yelp_search(location='10003', limit=40, term='food')
east_village = yelp_search(location='10003', term='food')
midtown = yelp_search(location='10017', term='dinner')

def yelp_search(**kwargs):
    #kwargs is a dict
    request = yelp.search(**kwargs)

    data = convert(request['businesses'])
    data_dict = {item['name']: item for item in data}
    # lets try to convert this list of dicts into dict of dicts
    df = pd.DataFrame(data_dict).T.sort_values('review_count', ascending=False)
    return df

cols = ['id','rating','review_count','categories']
request = yelp.search(location='new york', limit=40, categories='Food')
request = yelp.search(location='10003', limit=40, term='food')

data = convert(request['businesses'])
data_dict = {item['name']:item for item in data}
# lets try to convert this list of dicts into dict of dicts
df = pd.DataFrame(data_dict).T.sort_values('review_count',ascending=False)

df.columns
df[cols]




# getting a parsing error

?yelp.search
# ==========================
name = request['businesses'][0].keys()[0]
name.encode('ascii')

encoded_keys = [x.encode('ascii') for x in request['businesses'][0].keys()]




for i,v in request.businesses:
    print(i)
convert(request)

json.loads(request)

# Simple Examples
print yelp.search(location='new york', limit=10)
print yelp.business('yelp-san-francisco')
print yelp.phone_search(phone='+14037275451')
print yelp.search(term='food',bounds='37.900000,-122.500000|37.788022,-122.399797')
print yelp.search(term='food',ll='37.900000,-122.500000')
print yelp.search(term='food',location='Hayes',cll='37.77493,-122.419415')