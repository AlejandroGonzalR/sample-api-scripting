import logging


class UserNotFoundException(Exception):
    logging.error('User not found.')
    pass
