import untappd

class User(object):
  
  def __init__(self, api=None, bio=None, first_name=None, last_name=None,
               user_avatar=None, uid=None, relationship=None, untappd_url=None,
               url=None, checkins=None, settings=None, media=None, contact=None,
               date_joined=None, location=None, account_type=None,
               is_supporter=None, recent_brews=None, user_name=None, id=None,
               is_private=None, stats=None):
  
    self.api = untappd.Api()
    
    if self.api is None:
      raise Exception('untappd.api is required.')

  def GetUserInfo(self, username):
    call = '/user/info/%s' % username
    response_dict = untappd.Api.Call(self.api, call, self.api.key)
    for k, v in response_dict['response']['user'].iteritems():
      setattr(self, k, v)
