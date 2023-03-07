import unittest
from event_wave_app import app


class TestCaseBase(unittest.TestCase):
    """
    Base class for test cases in the Event Wave application.

    This class sets up the Flask application context for testing and provides a
    convenient method for cleaning up the context after each test method.

    Subclasses of this class should implement their own test methods.
    """
    def setUp(self):
        """
        Set up the Flask application context for testing.

        This method sets the Flask application's TESTING configuration variable to
        True and creates a new application context. The application context is then
        pushed onto the context stack, making it available for use in the current
        thread.
        """
        app.config["TESTING"] = True
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        """
        Clean up the Flask application context after each test method.

        This method pops the application context from the context stack, making it
        unavailable for use in the current thread. It then calls the tearDown
        method of the superclass to perform any additional cleanup.
        """
        self.app_context.pop()
        return super().tearDown()
