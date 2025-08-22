from enum import Enum

class TelegramBotMode(str, Enum):
    TEST = 'test'
    POLLING = 'polling'
    WEBHOOK = 'webhook'
    WEBHOOK_LOCAL = 'webhook_local'