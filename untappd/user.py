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
    
    self.account_type = account_type
    self.badges = badges
    self.bio = bio
    self.checkins = checkins
    self.contact = contact
    self.date_joined = date_joined
    self.friends = friends
    self.is_private = is_private
    self.is_supporter = is_supporter
    self.media = media
    self.relationship = relationship
    self.settings = settings
    self.stats = stats
    self.uid = uid
    self.untappd_url = untappd_url
    self.url = url
    self.user_avatar = user_avatar
    self.user_name = user_name
    
    self.api = untappd.UntappdApi()
    
    if self.api is None:
      raise Exception('untappd.UntappdApi is required.')
    
    if self.user_name is not None:
      self.GetUserInfo()

  def GetUserInfo(self):
    if self.user_name is None:
      raise Exception('An Untappd user_name must be defined.')
    call = '/user/info/%s' % self.user_name
    response_dict = untappd.UntappdApi.Call(self.api, call, self.api.payload)
    for key, v in  response_dict['response']['user'].iteritems():
      setattr(self, key, response_dict['response']['user'][key])
    return response_dict

  def GetUserBadges(self, params=None):
    call = '/user/badges/%s' % self.user_name
    response_dict = untappd.UntappdApi.Call(self.api, call, self.api.payload, params)
    self.badges = response_dict['response']['items']
    return self.badges

  def GetUserFriends(self, params=None):
    call = '/user/friends/%s' % self.user_name
    response_dict = untappd.UntappdApi.Call(self.api, call, self.api.payload, params)
    self.friends = response_dict['response']['items']
    return self.friends
    
  def GetDistinctBeers(self, params=None):
    call = '/user/beers/%s' % self.user_name
    response_dict = untappd.UntappdApi.Call(self.api, call, self.api.payload, params)
    self.distinct_beers = response_dict['response']['beers']
    return self.distinct_beers

  def GetUserFeed(self, params=None):
    call = '/user/checkins/%s' % self.user_name
    response_dict = untappd.UntappdApi.Call(self.api, call, self.api.payload, params)
    self.feed = response_dict['response']['beers']
    return self.feed