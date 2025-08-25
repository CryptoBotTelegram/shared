# shared.py
from pydantic import BaseModel, Field
from enum import Enum
from typing import Union


class LLMModel(str, Enum):
    GPT = "gpt"


class User(BaseModel):
    telegram_id: int
    first_name: str
    username: str
    is_premium: bool = Field(default=False)
    is_admin: bool = Field(default=False)


class UserSettingsDTO(BaseModel):
    LLM_model: LLMModel = Field(default=LLMModel.GPT)
    alert_config_general: list[str] = Field(default_factory=list)
    alert_config_specific: list[str] = Field(default_factory=list)
    language: str = Field(default="ru")


class UserFull(BaseModel):
    user: User
    settings: UserSettingsDTO

    # Для обратной совместимости со старым кодом
    @property
    def telegram_id(self):
        return self.user.telegram_id

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def username(self):
        return self.user.username

    @property
    def is_premium(self):
        return self.user.is_premium

    @property
    def is_admin(self):
        return self.user.is_admin

    @property
    def LLM_model(self):
        return self.settings.LLM_model

    @property
    def alert_config_general(self):
        return self.settings.alert_config_general

    @property
    def alert_config_specific(self):
        return self.settings.alert_config_specific

    @property
    def language(self):
        return self.settings.language