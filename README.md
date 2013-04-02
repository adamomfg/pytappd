### Pytappd

An Untappd API wrapper in Python
--------------------------------

This project is just getting started and is no way ready for any
kind of use.  You must apply for a clientID and secret before using
this library.

Wrapper design heavily inspired by https://github.com/dstegelman/pytappd


Usage
-----

Create an instance of Untappd.

Startup the API
---------------

    from untappd import Untappd

    api = Untappd(client_id='xxx', client_secret='xxx')


Call a User Feed
----------------

    feed = api.get_feed('username')
