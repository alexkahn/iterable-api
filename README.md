# Iterable API

This is a mostly complete wrapper of the Iterable API built with Python.

The interface is still in a state of flux, some methods will be renamed but the signatures should stay the same.

## Quickstart

```py
import os
from iterable import Iterable

api = Iterable(os.environ.get('ITERABLE_API_KEY'))

api.events.track(event_name='hello_iterable', user_id=42, created_at=datetime.now().to_timestamp())
```

## Dropping down

The API client is a requests.Session under the hood with HTTP method names as top level functions in the wrapper.

If you want to drop down to the client, you only need to provide the resource path, e.g.:

```py
api.get('/events/track')
```

## Testing

The library uses pytest - you can run the tests by invoking the following:

```py
pytest 
```
