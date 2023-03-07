def to_message(message):
    """
    Converts the given message to a JSON message object.

    :param message: The message(string) to be converted to JSON.
    :return: A dictionary representing the JSON message object.
    """
    return {"message": message}

# Define some message constants for common scenarios
APPLICATION_ERROR_MESSAGE = "Something went horrificaly wrong!"
NOT_FOUND_ERROR_MESSAGE = "No such entry ... better luck next time"
SUCCESS_DELETE_MESSAGE = "Deleted successfully!"
