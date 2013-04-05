#!/usr/bin/python
#TODO: use httplib2 in favor of requests
import requests

UNTAPPD_ENDPOINT = 'http://api.untappd.com/v4'


class APIKeyException(Exception):
  pass


class Api(object):

  #TODO(api): make sure that all calls have feed_url specified along with 
  # client_id and client_secret
  def __init__(self, client_id='C6D476FF7E034C2F10EB9A9F6975B93B1B82044B', 
               client_secret='E23D250D26BD3237A75C05FF57D5DE93727D8A38'):

    self.client_id = client_id
    self.client_secret = client_secret
    self.method = 'get'

    if self.client_id is None:
      raise APIKeyException('Client ID is required.')
    if self.client_secret is None:
      raise APIKeyException('Client secret is required.')

    self.key = '?client_id=%s&client_secret=%s' % (
              self.client_id, self.client_secret)
    self.pre_call = '%s%s' % (UNTAPPD_ENDPOINT, self.key)

  def Call(self, call):
    return requests.get(self.pre_call).json()

  def SearchBeers(self, query):
    """/search/beer"""
    feed_url = '/search/beer/?q=%s' % query
    return self.__call(feed_url)['response']

  def SearchBreweries(self):
    raise NotImplementedError

  def GetBrewery(self, brewery_id):
    feed_url = '/brewery/info/%s' % brewery_id
    return Brewery(self.__call(feed_url)['response']['brewery'])

  def GetUserFeed(self, username):
    feed_url = '/user/checkins/%s' % username
    return self.__call(feed_url)['response']['checkins']['items']
  
  def GetUserBadges(self, username):
    feed_url = '/user/badges/%s' % username
    return self.__call(feed_url)['response']

  def GetUserFriends(self, username):
	feed_url = '/user/friends/%s' % username
	return self.__call(feed_url)['response']
	
  def GetUserWishList(self, username):
	feed_url = '/user/wishlist/%s' % username
	return self.__call(feed_url)['response']
    
  def GetUserDistinctBeers(self, username):
    feed_url = '/user/beers/%s' % username
    return self.__call(feed_url)['response']
    
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
