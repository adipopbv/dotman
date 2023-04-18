import functools
import os

from app.domain.errors import NotFoundError
from app.utils.config import AppConfig


def valid_dotfiles_home(func):
    """
    Decorator that checks if the dotfiles home exists and has a valid structure
    :param func: the function that needs to be decorated
    :return: the decorated function
    """

    @functools.wraps(func)
    def wrapper_valid_dotfiles_home(*args, **kwargs):
        exists_at_path(AppConfig().config['DOTFILES']['HomePath'])
        return func(*args, **kwargs)

    def exists_at_path(dotfiles_path) -> None:
        if not os.path.exists(os.path.expanduser(dotfiles_path)):
            raise NotFoundError('No dotfiles home directory structure found.')

    return wrapper_valid_dotfiles_home
