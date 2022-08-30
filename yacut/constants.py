import re
from string import ascii_lowercase, ascii_uppercase, digits


STRING: str = "".join((ascii_uppercase, ascii_lowercase, digits))

pattern = r"^[A-Za-z0-9]{1,16}$"
match = re.compile(pattern)