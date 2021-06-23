import re

p = re.compile("ca.e")

m = p.match("caffe")
print(m.group())