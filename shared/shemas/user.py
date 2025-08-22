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
    LLM_model: str = Field(default=LLMModel.GPT)
    alert_config_general: list[str] = Field(default_factory=list)
    alert_config_specific: list[str] = Field(default_factory=list)

UserFull = Union[User, UserSettingsDTO]