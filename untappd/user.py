import untappd

class User(object):
  
  def __init__(self, api=None):
  
    self.api = untappd.Api()
    
    if self.api is None:
      raise Exception('untappd.api is required.')

  def GetUserInfo(self, api, username):
    feed_url = '/user/info/%s' % username
    return untappd.Api(feed_url)['response']['user']
