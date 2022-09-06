from unittest.mock import Mock, patch

import pytest

from iterable import Iterable


def test_client_initializes():
    api = Iterable('test_key')
    assert api.base_uri == 'https://api.iterable.com'
    assert 'Content-Type' in api._session.headers
    assert api._session.headers['Content-Type'] == 'application/json'
    assert 'Api-Key' in api._session.headers
    assert api._session.headers['Api-Key'] == api.api_key


def test_client_resources():
    resources = (
        'campaigns',
        'channels',
        'commerce',
        'email',
        'events',
        'experiments',
        'export',
        'in_app',
        'lists',
        'message_types',
        'metadata',
        'push',
        'sms',
        'templates',
        'users',
        'web_push',
        'workflows',
    )
    api = Iterable('test_key')
    assert all(hasattr(api, resource) for resource in resources)


def test_safe_api_calls():
    with patch('iterable.client.Session') as mock_session:
        session = mock_session()
        api = Iterable('test_key')
        api.get('/route', headers={'foo': 42})
        session.get.assert_called_once_with(
            api.base_uri + '/route',
            params=None,
            headers={'foo': 42})

def test_unsafe_api_calls():
    pass
