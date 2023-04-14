import os
from configparser import ConfigParser

from app.domain.errors import NotFoundError


class AppConfig:
    """The configurations of the app at runtime"""
    __instance = None
    config = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(AppConfig, cls).__new__(cls)
            cls.config = cls._load_config()
        return cls.__instance

    @staticmethod
    def _load_config() -> ConfigParser:
        """
        Loads the .config file from the root of the project.

        :return: the config
        """
        env = os.getenv("ENV", "config.ini")
        if env == "config.ini":
            config = ConfigParser()
            config.read(["config.ini", "test.config.ini"])
            return config
        raise NotFoundError("configuration file not found")