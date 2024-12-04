
import re
from collections import defaultdict

data = """
Day         Electricity     Coffee  Cleaning
Monday      330             10      50
Tuesday     220             12      40
Wednesday   130             14      80
"""
category = defaultdict(float)
days = defaultdict(float)
lines = re.split("\n", data)
header = None
for line in lines:
    #print(f"'{line}'")
    # ^\s*$  --- skip white spaces. start of white spaces ^ and end $. \s is a white space
    if re.search(r"^\s*$", line):
        continue
    fields = re.split(r"\s+", line) #split the data into fields
    if header is None:
        header = fields
        continue
        #print(fields)
    day = fields.pop(0)
    for i, field in enumerate(fields):
        heading = header[i + 1]
        days[day] += float(field)
        category[heading] += float(field)
print(header)
print(days)
print(category)

"""
Output

['Day', 'Electricity', 'Coffee', 'Cleaning']
defaultdict(<class 'float'>, {'Monday': 390.0, 'Tuesday': 272.0, 'Wednesday': 224.0})
defaultdict(<class 'float'>, {'Electricity': 680.0, 'Coffee': 36.0, 'Cleaning': 170.0})
"""
