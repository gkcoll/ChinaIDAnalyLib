'''
@File    :   demo.py
@Time    :   2023/05/02 14:41:48
@Author  :   @灰尘疾客
@Version :   1.0
@Site    :   https://www.gkcoll.xyz
@Desc    :   A demo of the project
'''


import ChinaIDAnalyLib as CINA
from json import dumps

# Generate a random ID.
ID = CINA.id_gen(1)[0]

# Create a CNID instance.
obj = CINA.CNID(ID)
print('This is an CNID instance:', obj)

# Show a report message.
CINA.report(obj)
# Also
print(obj.msg())

# Show as a table
CINA.table(obj)

# Get a dict for other works.
d = obj.info()
print(dumps(d, indent=4, ensure_ascii=False))