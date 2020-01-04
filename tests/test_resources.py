"""
Testing the API resources
"""
from unittest.mock import Mock, MagicMock

import pytest

from lib.iterable.client import Response
from lib.iterable.resources import Channels, Campaigns


@pytest.fixture
def mock_client():
    return Mock()


def test_channel_list(mock_client):
    mock_client.get.return_value = MagicMock(Response)
    channels = Channels(mock_client)
    channels.list()
    mock_client.get.assert_called_once_with('/api/channels')


def test_campaign_list(mock_client):
    campaigns = Campaigns(mock_client)
    campaigns.list()
    mock_client.get.assert_called_once_with('/api/campaigns')


def test_campaign_create(mock_client):
    campaigns = Campaigns(mock_client)
    campaigns.create(
        name='test_name', list_ids=[1, 2, 3], template_id='some_template')
    payload_data = {
        'name': 'test_name',
        'listIds': [1, 2, 3],
        'templateId': 'some_template',
        'sendAt': None,
        'sendMode': None,
        'startTimeZone': None,
        'defaultTimeZone': None
    }
    mock_client.post.assert_called_once_with('/api/campaigns/create', data=payload_data)
