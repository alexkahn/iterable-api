# Iterable API

This is a mostly complete wrapper of the Iterable API built with Python.

The interface is still in a state of flux, some methods will be renamed but the signatures should stay the same.

## User Docs

This is a pure python development kit for interacting with the Iterable API. If you find anything to be out of date or are looking for support, you can file an issue on Github.

### Installation

You can download and install the package from the Python Package Index with:

```
pip install iterable-api
```

### Quickstart

```py
from iterable import Iterable

api = Iterable('YOUR_API_KEY')

api.events.track(event_name='hello_iterable', user_id=42, created_at=datetime.now().to_timestamp())
```

If you're familiar with environment variables, you can set `ITERABLE_API_KEY`. In that case you can set up the api client like so:

```py
from os import getenv
from iterable import Iterable

api = Iterable(getenv('ITERABLE_API_KEY'))
```

### Data exports

If you're interested in getting data out of your Iterable account, you can use the `export_data_api` method on the API client.

### Dropping down

The API client is a requests.Session under the hood with HTTP method names as top level functions in the wrapper.

If you want to drop down to the client, you only need to provide the resource path, e.g.:

```py
api.get('/events/track')
```

This might be useful for exploring the API or debugging an issue.

## Development Docs

If you're interested in extending this library, please follow these guidelines:

1. Please file an issue first describing what you want to add or change.
2. Fork the repository and submit a pull request.

### Installation for development

This project uses poetry for now, so follow your preferred procedure for that.

```
poetry install
```

### Testing

The library uses pytest - you can run the tests by invoking the following:

```py
poetry run pytest
```
