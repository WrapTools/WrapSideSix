# io/__init__.py

import logging

# Create a logger for your library
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# __all__ = ['Class']

def some_function():
    logger.debug("This is a debug message from io/module.")

# from .library import class or function
