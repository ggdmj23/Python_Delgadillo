import re

string = "'I AM NOT YELLING', she said. Though we knew it to not be true."

print(string)

# new = re.sub(r'[A-Z]', '', string)
# new = re.sub(r'[a-z]', '', string)
# new = re.sub(r'[.,\']', '', string)
new = re.sub(r"[a-z.,'\s]", '', string)

print(new)

string = string + '699 55 91 97'

new = re.sub(r"[^0-9]", '', string)

print(new)
