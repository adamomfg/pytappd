import untappd

class User(object):

  """An Untappd user object.

  Creates a user object, with no attributes. Call any method to populate the 
  object with attributes, with a username and an api key.
  """
  
  def __init__(self, api=None, bio=None, first_name=None, last_name=None,
               user_avatar=None, uid=None, relationship=None, untappd_url=None,
               url=None, checkins=None, settings=None, media=None, contact=None,
               date_joined=None, location=None, account_type=None,
               is_supporter=None, recent_brews=None, user_name=None, id=None,
               is_private=None, stats=None, badges=None, friends=None):
  
    self.api = untappd.Api()
    
    if self.api is None:
      raise Exception('untappd.api is required.')

  def GetUserInfo(self, username):
    call = '/user/info/%s' % username
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    for k, v in response_dict['response']['user'].iteritems():
      setattr(self, k, v)

  def GetUserBadges(self, username):
    call = '/user/badges/%s' % username
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    self.badges = response_dict['response']['items']

  def GetUserFriends(self, username):
    call = '/user/friends/%s' % username
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    self.friends = response_dict['response']['items']
    
  def GetUserFriends(self, username):
    call = '/user/wishlist/%s' % username
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    self.friends = response_dict['response']['items']
    
  def GetDistinctBeers(self, username):
    call = '/user/beers/%s' % username
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    self.distinct = response_dict['response']['items']

  def GetUserFeed(self, username):
    call = '/user/checkins/%s' % username
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    # print response_dict
    self.feed = response_dict['response']['checkins']['items']
