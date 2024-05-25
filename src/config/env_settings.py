from enum import StrEnum, auto

from pydantic_settings import BaseSettings


class Environment(StrEnum):
    """The different environments."""

    DEVELOPMENT = auto()
    PRODUCTION = auto()
    TEST = auto()


ENV_FILENAMES = {
    Environment.DEVELOPMENT.value: (".env",),
    Environment.PRODUCTION.value: (".env",),
    Environment.TEST.value: (".env.test",),
}


class Settings(BaseSettings):
    """A class to manage the application settings."""

    ENVIRONMENT: Environment = Environment.DEVELOPMENT
    """The type of the environment."""

    DOCS_URL: str = ""
    """The URL for the API documentation."""

    REDOC_URL: str = ""
    """The URL for the API documentation."""

    DB_HOST: str
    """The database host."""

    DB_PORT: int
    """The database port."""

    DB_NAME: str
    """The database name."""

    DB_USER: str
    """The database user."""

    DB_PASSWORD: str
    """The database password."""

    DB_DRIVER: str
    """The database driver."""


class EnvFileSettings(BaseSettings):
    """Configuration class for loading application environment file settings."""

    ENVIRONMENT: Environment = Environment.DEVELOPMENT

    def load_settings(self) -> Settings:
        """Creates an instance of Settings based on the environment.

        Returns:
            Settings: The instance of Settings for the specified environment.
        """
        env_filename = ENV_FILENAMES[self.ENVIRONMENT.value]
        return Settings(_env_file=env_filename)


settings: Settings = EnvFileSettings().load_settings()

__all__ = ["settings"]
