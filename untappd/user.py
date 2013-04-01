import untappd

class User(object):
  
  def __init__(self, data):
  
    self.__dict__.update(data)