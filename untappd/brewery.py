import untappd_object


class Brewery(object):

  def __init__(self, brewery_id=None, brewery_active=None, brewery_name=None, 
               contact=None, url=None, twitter=None, facebook=None,
               brewery_label=None, location=None, brewery_city=None,
               brewery_state=None, lng=None, lat=None, country_name=None):

    self.brewery_active = brewery_active
    self.brewery_city = brewery_city
    self.brewery_id = brewery_id
    self.brewery_label = brewery_label
    self.brewery_name = brewery_name
    self.brewery_state = brewery_state
    self.country_name = country_name    
    self.contact = contact
    self.facebook = facebook
    self.lat = lat    
    self.lng = lng
    self.location = location
    self.twitter = twitter
    self.url = url
    
    self.api = untappd.UntappdApi()

    if self.api is None:
      raise Exception('untappd.api is required.')