import untappd

class User(object):
  
  def __init__(self, data):
  
    self.__dict__.update(data)
    api = untappd.Untappd(client_id='C6D476FF7E034C2F10EB9A9F6975B93B1B82044B',
                          client_secret='E23D250D26BD3237A75C05FF57D5DE93727D8A38')
    self.badges = api.GetUserBadges(self.user_name)
    self.distinct_beers = api.GetUserDistinctBeers(self.user_name)