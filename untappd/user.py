class User(object):
  
  def __init__(self, data):
  
    self.__dict__.update(data)          
    """
    self.user_name = user_name
    self.first_name = first_name
    self.last_name = last_name
    self.user_avatar = user_avatar
    self.is_private = is_private
    self.location = location
    self.url = url           
    self.bio = bio
    self.relationship = relationship
    self.account_type = account_type
    self.contact = contact
    self.is_supporter = is_supporter
    self.facebook = facebook
    self.twitter = twitter
    self.foursquare = foursquare
    self.uid = uid
    """