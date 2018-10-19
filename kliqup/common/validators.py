from django.core.exceptions import ValidationError as CoreValidationError
from django.core.validators import URLValidator


def validate_url(value, raise_exception=False):
    """
    Validate given value is a url.
    If so, return the value, else return None if raise_exception is disabled.
    """
    url_validator = URLValidator()
    try:
        url_validator(value)
        return value
    except CoreValidationError:
        if not raise_exception:
            return None
        else:
            raise
