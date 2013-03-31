__author__ = 'derek'
import untappd_object


class Brewery(untappd_object.UntappdObject):

  def __init__(self, brewery_id=None, brewery_active=None, brewery_name=None, 
               contact=None, url=None, twitter=None, facebook=None,
               brewery_label=None, location=None, brewery_city=None,
               brewery_state=None, lng=None, lat=None, country_name=None):
               
    self.brewery_id = brewery_id
    self.brewery_active = brewery_active
    self.brewery_name = brewery_name
    self.contact = contact
    self.url = url
    self.twitter = twitter
    self.facebook = facebook
    self.brewery_label = brewery_label
    self.location = location
    self.brewery_city = brewery_city
    self.brewery_state = brewery_state
    self.lng = lng
    self.lat = lat
    self.country_name = country_name