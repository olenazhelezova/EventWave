import re

def validate_date(date):
    """
    Validates if the given date is in the format YYYY-MM-DD using regex.

    :param date: A string representing the date to be validated.
    :raises ServiceException: If the date is not in the correct format.
    """
    if (
        re.fullmatch(
            r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", str(date)
        )
        is None
    ):
        raise ServiceException("Invalid date format.")

class ServiceException(BaseException):
    """
    Custom exception for service-level errors.
    """
