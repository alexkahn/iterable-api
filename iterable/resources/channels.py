from .base import Resource


class Channels(Resource):

    def list(self):
        resource = "/api/channels"
        return ChannelResponse(self.client.get(resource))


class Channel:

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.channel_type = kwargs.get('channelType')
        self.message_medium = kwargs.get('messageMedium')

    @property
    def email_marketing(self):
        return bool(self.message_medium == 'Email' and self.channel_type == 'Marketing')


class ChannelResponse:

    def __init__(self, http_response):
        self._response = http_response
        if 'channels' in self._response.data:
            self._channels = [Channel(**chan) for chan in self._response.data['channels']]

    def __getitem__(self, index):
        return self._channels[index]

    def __iter__(self):
        for chan in self._channels:
            yield chan
