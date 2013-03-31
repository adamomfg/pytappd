import untappd_object


class User(untappd_object.UntappdObject):
  
  def __init__(self, user_name=None, first_name=None, last_name=None,
               user_avatar=None, is_private=None, location=None, url=None,
               bio=None, relationship=None, account_type=None):
    
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
    self.foursquare = foursquare
    