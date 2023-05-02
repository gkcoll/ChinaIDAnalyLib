import requests
import re
import json
import string


# Crawling data (2020 data, latest as of April 15, 2023).
url = "https://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html"
content = requests.get(url).text

# Create regex for matching.
regex = r'<td class=xl\d{7}>(?P<code>\d{6})</td>.*?<td class=xl\d{7}>(<span style=\'mso-spacerun:yes\'>.*?</span>){0,1}(?P<loc>.*?)</td>'
obj = re.compile(regex, re.S)

# Extract data.
data = obj.finditer(content)

# Due to data formatting errors on some web pages of mca.gov.cn (Ministry of Civil Affairs), 
# it is necessary to block some illegal characters that are matched.
# We should block English letters, numbers, punctuation.
invalid_char = f"{string.ascii_letters}{string.digits}{string.punctuation}"
result = {i.group('code'): re.sub(f"[{invalid_char}]", "", i.group('loc')) for i in data}

# Output.
with open('data_2020.json', 'a', encoding='utf-8') as d:
    d.write(json.dumps(result, ensure_ascii=False, indent=4))
