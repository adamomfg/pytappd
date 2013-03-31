__author__ = 'derek'
import untappd_object


class Brewery(untappd_object.UntappdObject):

  def __init__(self, brewery_id=None, brewery_active=None, brewery_name=None, 
               contact=None, url=None, twitter=None, facebook=None):
               #TODO what do we do with nested stuff like this? Make them all 
               # attributes of the brewer, or of a contact subclass?
                u'elysianbrewing', u'facebook': u'http://www.facebook.com/pages/Elysian-Brewing-Company/92348396799'}, u'brewery_label': u'https://untappd.s3.amazonaws.com/site/brewery_logos/brewery-ElysianBrewingCompany_7294.jpeg', u'location': {u'brewery_city': u'Seattle', u'brewery_state': u'WA', u'lng': -122.316, u'lat': 47.614}, u'country_name': u'United States'}