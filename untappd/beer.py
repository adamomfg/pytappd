import untappd

class Beer(object):

  def __init__(self, abv=None, api=None, beer_id=None, brewery=None, description=None, label=None, 
               name=None, style=None):
    
    self.abv = abv
    self.beer_id = beer_id
    self.brewery = brewery
    self.description = description
    self.label = label
    self.name = name
    self.style = style

    self.api = untappd.UntappdApi()

    if self.api is None:
      raise Exception('untappd.api is required.')
        
  def SearchBeers(self, beer):
    """Search for a beer."""
    call = '/search/beer/?q=%s?sort=count' % beer
    response_dict = untappd.UntappdApi.Call(self.api, call, self.api.payload)
    return response_dict
  
  def GetBeerInfo(self, beer_id):
    """Pass the beer id."""
    call = '/beer/info/%s' % beer_id
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    return response_dict
    
  def BeerFeed(self, beer):
    call = '/beer/checkins/%s' % beer_id
    response_dict = untappd.Api.Call(self.api, call, self.api.payload)
    return response_dict