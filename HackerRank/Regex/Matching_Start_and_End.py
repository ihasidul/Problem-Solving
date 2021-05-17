Regex_Pattern = r"^[0-9]\w\w\w\w.$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
