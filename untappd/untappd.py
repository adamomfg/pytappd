#!/usr/bin/python

#TODO: use httplib2 in favor of requests
import requests

UNTAPPD_ENDPOINT = 'http://api.untappd.com/v4'


class APIKeyException(Exception):
  pass


class Api(object):

  def __init__(self, client_id=None,
               client_secret=None):

    self.client_id = client_id
    self.client_secret = client_secret
    self.method = '/get'

    if self.client_id is None:
      raise APIKeyException('Client ID is required.')
    if self.client_secret is None:
      raise APIKeyException('Client secret is required.')

    self.key = '?client_id=%s&client_secret=%s' % (
              self.client_id, self.client_secret)

  def Call(self, call, key):
    return requests.get(UNTAPPD_ENDPOINT + call + self.key).json()

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
