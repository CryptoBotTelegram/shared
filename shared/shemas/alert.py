from pydantic import BaseModel

class Alert(BaseModel):
    text: str   # BTC Обновил рекорд по стоимости
    general_tags: list[str]
    specific_tags: list[str]