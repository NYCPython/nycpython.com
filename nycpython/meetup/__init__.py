"""Meetup API wrapper."""

from datetime import datetime
import json
import logging

import redis
import requests

__all__ = 'events', 'photos'

_logger = logging.getLogger(__name__)


class APIWrapper:

    """Wrapper around the meetup.com API."""

    def __init__(self, api_key):
        self.api_key = api_key

    def _get(self, method, limit, **params):
        r = redis.StrictRedis()
        key = 'meetup_{}_{}'.format(method, limit)

        result = None and r.get(key)
        if not result:
            url = 'http://api.meetup.com/2/{}.json'.format(method)
            params['key'] = self.api_key
            params['page'] = limit

            resp = requests.get(url, params=params)
            if resp.status_code != 200:
                _logger.error('Meetup API <{}>: {}'.format(
                    resp.status_code, resp.json().get('details')))
                raise Exception('Meetup returned no results for {}'.format(method))

            result = resp.json().get('results', [])

            r.set(key, json.dumps(result))
            r.expire(key, 300)
        else:
            result = json.loads(result)

        return result

    def events(self, group_id, limit=None):
        """Return the upcoming events for the group."""
        limit = limit or 20

        result = self._get(
            'events',
            limit,
            group_id=group_id,
            status='upcoming',
            visibility='public',
        )

        events = []
        for event in result:
            name = event.get('name', 'Unnamed event')
            url = event.get('event_url', '')
            description = event.get('description', '')
            time = int(event.get('time', 0)) + int(event.get('utc_offset', 0))
            time /= 1000
            events.append({
                'name': name.strip(),
                'url': url,
                'description': description,
                'time': datetime.fromtimestamp(time),
            })

        return events

    def photos(self, group_id, limit=None):
        """Return photos for the group."""
        limit = limit or 20

        result = self._get('photos', limit, group_id=group_id)

        photos = []
        for photo in result:
            url = photo.get('photo_link')
            if not url:
                continue

            photos.append({'url': url})

        return photos
