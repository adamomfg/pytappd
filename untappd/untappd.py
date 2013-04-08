#!/usr/bin/python

#TODO: use httplib2 in favor of requests
import requests

UNTAPPD_ENDPOINT = 'http://api.untappd.com/v4'


class APIKeyException(Exception):
  pass


class Api(object):

  def __init__(self, payload=None):
  
    key = {}
    
    self.payload = key

  def _AddParams(self, params=None):
    if params:
      for k, v in params.iteritems():
        self.payload[k] = v

  def Call(self, call, payload, params=None):
    self._AddParams(params)        
    r = requests.get(UNTAPPD_ENDPOINT + call, params=self.payload)
    print r.url
    return r.json()

  def SearchBeers(self, query):
    """/search/beer"""
    feed_url = '/search/beer/?q=%s' % query
    return self.__call(feed_url)['response']

  def SearchBreweries(self):
    raise NotImplementedError

  def GetBrewery(self, brewery_id):
    feed_url = '/brewery/info/%s' % brewery_id
    return Brewery(self.__call(feed_url)['response']['brewery'])
    
  def GetPubFeed(self, pub):
    feed_url = 'pub'
    return self.__call(FEED_URL)['response']

  def GetVenueVeed(self):
    """/venue/checkins/VENUE_ID"""
    pass

  def GetBeerCheckins(self):
    """/beer/checkins/BID"""
    pass

  def GetBreweryCheckins(self):
    """/brewery/checkins/BREWERY_ID"""
    pass
