class NotFound(Exception):
    """
    Represendted as 404 error
    """


class IntegrityCompromised(Exception):
    """
    Represendted as 409 error
    """


class AuthenticationError(Exception):
    """
    Represendted as 401 error
    """


class AuthorizationError(Exception):
    """
    Represendted as 403 error
    """
