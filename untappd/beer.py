import untappd

class Beer(object):

  def __init__(self, api=None, beer_id=None, name=None, label=None, abv=None, style=None,
               description=None, brewery=None):

    self.api = untappd.Api()

    if self.api is None:
      raise Exception('untappd.api is required.')
        
  def SearchBeers(self, beer):
    """Search for a beer."""
    call = '/search/beer/?q=%s?sort=count' % beer
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    return response_dict
  
  def GetBeerInfo(self, beer_id):
    """Pass the beer id."""
    call = '/beer/info/%s' % beer_id
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    
  def BeerFeed(self, beer):
    call = '/beer/checkins/%s' % beer_id
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)