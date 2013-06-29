# -*- coding: utf-8 -*-


"""
    nycpython.services.meetup.events
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains services interfacing with the meetup.com API and grabbing events

"""


from datetime import datetime

from src import GROUP_ID, GROUP_URL
from src.services.meetup import MeetupAPIRequest


EVENT_FIELDS = ('name', 'event_url', 'time')
RECURRING_TAG = '#recurring'


def get_group_events():
    """Gets the events from the Meetup API for the NYCPython group and returns
    a dictionary of events that contains name, event_url, datetime object and
    a boolean recurring depending on whether or not the name of the event
    contains ``RECURRING_TAG``

    """

    req = MeetupAPIRequest(
        'events',
        status='upcoming',
        visibility='public',
        group_id=GROUP_ID)

    req_json = req()

    events = []

    for event in req_json.get('results', {}):
        events.append({
            'name': event.get('name', 'Unnamed event'),
            'event_url': event.get('event_url', GROUP_URL),
            'recurring': True if RECURRING_TAG in event.get('name') else False,
            'time': datetime.fromtimestamp(
                int(event.get('time', 0)) / 1000 +
                int(event.get('utc_offset', 0)) / 1000)
        })

    return events
