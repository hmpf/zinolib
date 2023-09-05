from pathlib import Path
import re

from pydantic_settings import BaseSettings, SettingsConfigDict


class ConnectionSettings(BaseSettings):
    server: str
    port: int
    user: str


class Zino1ConnectionSettings(ConnectionSettings):
    model_config = SettingsConfigDict(env_prefix="zino1_")
    secret: str


class Zino1OtherSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="zino1_")
    sort_by: str = None


class Zino1Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="zino1_",
        env_file=".env",
        env_file_encoding="utf-8",
    )
    connection: Zino1ConnectionSettings = Zino1ConnectionSettings()
    other: Zino1OtherSettings = None
