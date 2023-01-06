from periodictable import elements
import re
el = {}
sum = 0
compound = input("Compound: ")

for element in elements:
  el[f'{element.symbol}'] = element.mass

x = re.findall("([A-Z][^A-Z\d]*\d*)", compound)
for item in x:
  elem = re.search("([A-Z][^A-Z\d]*)", item).group(0)
  if len(elem) is not len(item):
    length = len(elem)
    sum += el[elem] * int(item[length:])
  else:
    sum += el[elem]
print(round(sum,3))  
