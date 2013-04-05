import untappd

class User(object):
  
  def __init__(self, api=None):
  
    self.api = untappd.Api()
    
    if self.api is None:
      raise Exception('untappd.api is required.')

  def GetUserInfo(self, username):
    feed_url = '/user/info/%s' % username
    return untappd.Api.Call(self.api, self.key, feed_url)
