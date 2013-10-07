#!/usr/bin/python

#TODO: use httplib2 in favor of requests
import requests

UNTAPPD_ENDPOINT = 'http://api.untappd.com/v4'


class APIKeyException(Exception):
  pass


class Api(object):

  def __init__(self, payload=None):
  
    key = {} # Add your Untappd API client_id and client_secret here.

    self.payload = key

  def _AddParams(self, params=None):
    if params:
      for k, v in params.iteritems():
        self.payload[k] = v

  def Call(self, call, payload, params=None):
    self._AddParams(params)        
    r = requests.get(UNTAPPD_ENDPOINT + call, params=self.payload)
    print r.url
    return r.json()