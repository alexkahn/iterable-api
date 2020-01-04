class InvalidParameters(Exception):
    """
    When the request payload is incorrect for some reason, raise this exception
    """

    pass


class AuthorizationError(Exception):
    """
    When the API key doesn't work for that thing.
    """

    pass
