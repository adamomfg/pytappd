
import requests

UNTAPPD_ENDPOINT = 'http://api.untappd.com/v4'

from .exceptions import APIKeyException


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

    def get_feed(self, username):
        FEED_URL = '/user/checkins/%s' % username
        return self.__call(FEED_URL)['response']['checkins']['items']
