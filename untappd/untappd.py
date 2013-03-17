
import requests

UNTAPPD_ENDPOINT = 'http://api.untappd.com/v4'

from .exceptions import APIKeyException
from .beer import Beer
from .brewery import Brewery


class Untappd(object):

    def __init__(self, client_id=None, client_secret=None):

        self.client_id = client_id
        self.client_secret = client_secret

        if self.client_id is None:
            raise APIKeyException('Client ID is required.')
        if self.client_secret is None:
            raise APIKeyException('Client secret is required.')

    def __append_key(self):
        return '?client_id=%s&client_secret=%s' % (self.client_id, self.client_secret)

    def __pre_call(self, url):
        return "%s%s%s" % (UNTAPPD_ENDPOINT, url, self.__append_key())

    def __call(self, url):
        return requests.get(self.__pre_call(url)).json()

    def get_beers(self):

        beers = []
        for beer in self.get_feed('dstegelman'):
            beers.append(self.get_beer(beer['beer']['bid']))
        return beers

    def search_beers(self, query):
        """
        /search/beer
        """
        feed_url = '/search/beer/?q=%s' % query
        beers = []
        print(self.__call(feed_url)['response']['beers']['items'])
        for beer in self.__call(feed_url)['response']['beers']['items']:
            beers.append(self.get_beer(beer['bid']))

        return beers

    def search_breweries(self):
        raise NotImplementedError

    def get_beer(self, beer_id):
        """
        /beer/info/
        """
        feed_url = '/beer/info/%s' % beer_id
        return Beer(self.__call(feed_url)['response']['beer'])

    def get_brewery(self, brewery_id):
        """
        /brewery/info/
        """
        feed_url = '/brewery/info/%s' % brewery_id
        return Brewery(self.__call(feed_url)['response']['brewery'])


    def get_feed(self, username):
        """
        user/checkins/USERNAME
        """
        FEED_URL = '/user/checkins/%s' % username
        return self.__call(FEED_URL)['response']['checkins']['items']

    def get_pub_feed(self):
        """
        /thepub
        """
        pass

    def get_venue_feed(self):
        """
        /venue/checkins/VENUE_ID
        """
        pass

    def get_beer_checkins(self):
        """
        /beer/checkins/BID
        """
        pass

    def get_brewery_checkins(self):
        """
        /brewery/checkins/BREWERY_ID
        """
        pass



