#!/usr/bin/python
#TODO: use httplib2 in favor of requests
import requests

UNTAPPD_ENDPOINT = 'http://api.untappd.com/v4'

from exceptions import APIKeyException
from beer import Beer
from brewery import Brewery


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

  def GetBeers(self):
    beers = []
    for beer in self.get_feed(''):
      beers.append(self.get_beer(beer['beer']['bid']))
    return beers

  def SearchBeers(self, query):
    """/search/beer"""
    feed_url = '/search/beer/?q=%s' % query
    beers = []
    print(self.__call(feed_url)['response']['beers']['items'])
    for beer in self.__call(feed_url)['response']['beers']['items']:
      beers.append(self.get_beer(beer['bid']))

    return beers

  def SearchBreweries(self):
    raise NotImplementedError

    #TODO(fix this to work)
    def get_beer(self, beer_id):
      """/beer/info/"""
      feed_url = '/beer/info/%s' % beer_id
      return Beer(self.__call(feed_url)['response']['beer'])

  def GetBrewery(self, brewery_id):
    """/brewery/info/"""
    feed_url = '/brewery/info/%s' % brewery_id
    return Brewery(self.__call(feed_url)['response']['brewery'])


  def GetFeed(self, username):
    """user/checkins/USERNAME"""
    FEED_URL = '/user/checkins/%s' % username
    return self.__call(FEED_URL)['response']['checkins']['items']

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
