import logging
import sys
import structlog
import requests
from threading import Thread

FORMATTER_STRING = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
FORMATTER = logging.Formatter(FORMATTER_STRING)

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)
    return logger

def replace_user(_, __, event_dict):
    user = event_dict.get("user")
    if user:
        user_token = "some_string_that_we_can_learn_username_from"
        event_dict["user"] = user_token
    return event_dict

def censor_password(_, __, event_dict):
    pw = event_dict.get("password")
    if pw:
        event_dict["password"] = "*CENSORED*"
    return event_dict

class HTTPCriticalHandler(logging.Handler):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def emit(self, record):
        try:
            log_entry = self.format(record)
            if record.levelname == "CRITICAL":
                response = requests.post(self.url, json={"message": log_entry})
                if response.status_code != 200:
                    print("Failed to send critical log")
        except Exception as e:
            print(f"Error in sending log: {e}")

log = structlog.wrap_logger(
    get_logger("my_app_logger"),
    processors=[
        censor_password,
        replace_user,
        structlog.processors.JSONRenderer(indent=1, sort_keys=True),
    ],
)

http_handler = HTTPCriticalHandler(url="http://localhost:8080/log")
http_handler.setFormatter(FORMATTER)
logging.getLogger().addHandler(http_handler)

log.warning("something", password="secret")
log.warning("something", user="Ivan")
log.critical("A critical error occurred!", password="supersecret")
