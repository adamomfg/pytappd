#!/usr/bin/python
#TODO: use httplib2 in favor of requests
import requests

UNTAPPD_ENDPOINT = 'http://api.untappd.com/v4'

from beer import Beer
from brewery import Brewery


class APIKeyException(Exception):
  pass


class Untappd(object):

  def __init__(self, client_id=None, client_secret=None):

    self.client_id = client_id
    self.client_secret = client_secret
    self.method = 'get'

    if self.client_id is None:
        raise APIKeyException('Client ID is required.')
    if self.client_secret is None:
        raise APIKeyException('Client secret is required.')

  #TODO: clean up the internal methods for making calls to the API
  def __append_key(self):
    return '?client_id=%s&client_secret=%s' % (
        self.client_id, self.client_secret)

  def __pre_call(self, url):
      return "%s%s%s" % (UNTAPPD_ENDPOINT, url, self.__append_key())

  def __call(self, url):
    return requests.get(self.__pre_call(url)).json()

  def SearchBeers(self, query):
    """/search/beer"""
    feed_url = '/search/beer/?q=%s' % query
    beers = []
    #TODO fix this to work, put in beers.py
    print(self.__call(feed_url)['response']['beers'])

    return beers

  def SearchBreweries(self):
    raise NotImplementedError

  def GetBrewery(self, brewery_id):
    """/brewery/info/"""
    feed_url = '/brewery/info/%s' % brewery_id
    return Brewery(self.__call(feed_url)['response']['brewery'])

  def GetUserFeed(self, username):
    """user/checkins/USERNAME"""
    FEED_URL = '/user/checkins/%s' % username
    return self.__call(FEED_URL)['response']['checkins']['items']

  def GetPubFeed(self, pub):
    feed_url = 'thepub'
    return self.__call(FEED_URL)['response']

  def GetPubFeed(self):
    """/thepub"""
    pass

  def GetVenueVeed(self):
    """/venue/checkins/VENUE_ID"""
    pass

  def GetBeerCheckins(self):
    """/beer/checkins/BID"""
    pass

  def GetBreweryCheckins(self):
    """/brewery/checkins/BREWERY_ID"""
    pass
