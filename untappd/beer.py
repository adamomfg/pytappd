import untappd

class Beer(object):

  def __init__(self, api, beer_id=None, name=None, label=None, abv=None, style=None,
               description=None, brewery=None):

    self.api = untappd.Api()

      if self.api is None:
        raise Exception('untappd.api is required.')
        
  def GetBeerInfo(self.api, beer):
    """Pass the beer id."""
    pass
    
  def BeerSearch(self.api,  beer):
    pass