from pydantic import BaseModel, Field

class Prompt(BaseModel):
    text: str
    general_tags: list[str] = Field(default_factory=list)
    specific_tags: list[str] = Field(default_factory=list)