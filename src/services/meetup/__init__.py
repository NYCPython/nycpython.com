# -*- coding: utf-8 -*-


"""
    nycpython.services.meetup
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains services interfacing with the meetup.com API

"""


from urllib.parse import urlencode

import requests

from src import MEETUP_API_KEY


class MeetupAPIError(Exception):
    pass


class MeetupAPIRequest(object):
    """Creates and formats the API URL, makes the HTTP requests and parses
    accordingly"""

    url = None

    def __init__(self, method, **params):
        """Creates an object with the URL, ready to execute

        :param method: Meetup API method to call
        :param **params: Additional Meetup API params to be encoded
        """

        params.update({'key': MEETUP_API_KEY})
        params = urlencode(params)

        self.url = 'http://api.meetup.com/2/{0}.json/?{1}'.format(
            method, params)

    def __call__(self):
        """Executes the HTTP call and returns the JSON parsed as a dict, or
        throws MeetupAPIError or ValueError"""

        req = requests.get(self.url)
        if req.status_code != 200:
            raise MeetupAPIError("Couldn't connect to Meetup: HTTP {}".format(
                req.status_code))

        try:
            req_json = req.json()
        except ValueError:
            raise MeetupAPIError("Meetup didn't return valid JSON")

        return req_json
