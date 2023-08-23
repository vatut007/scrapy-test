import re
string = ' +7 (921) 960-68-62'
PATTERN_NUMBER = r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}'
number = re.search(PATTERN_NUMBER, string)

print(number)