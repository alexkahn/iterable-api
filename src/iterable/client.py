"""
Iterable API Wrapper

Getting Started:

You can interact with resources like so:
    from iterable import Iterable
    api = Iterable('YOUR_API_KEY')

    res = api.email.send(recipient_email='you@example.com', data_fields={'foo': 42, 'bar': False})
    res.status_code
    res.data
    res.headers
    res.url

Exporting data is also supported, currently to a local file but the method could be easily
refactored to accept any file-like object (like a socket or a buffer)
"""
import os
from json import JSONDecodeError
import time
from collections import namedtuple

from requests import Session

from .exceptions import AuthorizationError, InvalidParameters
from .resources import *


Response = namedtuple("Response", ("data", "status_code", "headers", "url"))


class Iterable:
    """
    Main interface for interacting with the Iterable API.
    """

    base_uri = "https://api.iterable.com"

    def __init__(self, api_key=None):
        """
        This preforms the necessary initialization parameters for the
        Iterable project. It stores the base URI, the API key for the
        project, and headers that are consistent across all requests.
        """
        self._session = Session()
        if api_key:
            self.api_key = api_key
        else:
            try:
                self.api_key = os.environ["ITERABLE_API_KEY"]
            except KeyError:
                raise ValueError(
                    "No value passed for API Key, please do that or set the ITERABLE_API_KEY environment variable"
                )

        self._session.headers.update(
            {"Content-type": "application/json", "Api-Key": self.api_key}
        )
        self.campaigns = Campaigns(self)
        self.channels = Channels(self)
        self.commerce = Commerce(self)
        self.email = EmailMessage(self)
        self.events = Events(self)
        self.experiments = Experiments(self)
        self.export = Export(self)
        self.in_app = InAppMessages(self)
        self.lists = Lists(self)
        self.message_types = MessageTypes(self)
        self.metadata = Metadata(self)
        self.push = PushNotification(self)
        self.sms = SmsMessage(self)
        self.templates = Templates(self)
        self.users = Users(self)
        self.web_push = WebPushNotification(self)
        self.workflows = Workflows(self)

    def get(self, resource, params=None, headers=None):
        url = self.base_uri + resource
        response = self._session.get(url, params=params, headers=headers)
        return self._handle_response(response)

    def post(self, resource, data=None, headers=None):
        url = self.base_uri + resource
        response = self._session.post(url, json=data, headers=headers)
        return self._handle_response(response)

    def put(self, resource, data=None, headers=None):
        url = self.base_uri + resource
        response = self._session.put(url, json=data, headers=headers)
        return self._handle_response(response)

    def delete(self, resource, headers=None):
        url = self.base_uri + resource
        response = self._session.delete(url)
        return self._handle_response(response)

    @staticmethod
    def _handle_response(http_response):
        if http_response.status_code == 400:
            raise InvalidParameters(http_response.json())
        elif http_response.status_code == 401:
            raise AuthorizationError(http_response.json())
        try:
            return Response(
                data=http_response.json(),
                status_code=http_response.status_code,
                headers=http_response.headers,
                url=http_response.url,
            )
        except JSONDecodeError:
            return Response(
                data=http_response.text,
                status_code=http_response.status_code,
                headers=http_response.headers,
                url=http_response.url,
            )

    def export_data_api(
        self,
        call,
        params,
        path,
        format=None,
        chunk_size=None,
        return_response_object=False,
    ):
        r = self._session.request(
            method="GET", url=self.base_uri + call, params=params, stream=True
        )
        if r.status_code == 200 and return_response_object:
            return r
        local_filename = f"iterableDataExport_{str(round(time.time()))}.{format}"
        with open(path + local_filename, "wb") as write_file:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    write_file.write(chunk)
        return True
