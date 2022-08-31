import re
from string import ascii_lowercase, ascii_uppercase, digits


STRING: str = "".join((ascii_uppercase, ascii_lowercase, digits))

PATTERN = r"^[A-Za-z0-9]{1,16}$"
MATCH = re.compile(PATTERN)

LOG_FORMAT = "\t%(asctime)s – [%(levelname)s]: " \
             "%(message)s. Исполняемый файл – '%(filename)s': " \
             "функция – '%(funcName)s'(%(lineno)d)"
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
