#1作业
import requests
b=requests.get('http://www.17k.com/book/2811930.html')
from lxml import etree
tree=etree.HTML(b.text)
book=tree.xpath('//body/div[@class="Nav"]/div/a[@href]/@href')
print(book)

#2作业
import re
content='Hello 1234567 hahah 123 lalal 456'
res=re.match('^Hello\s\d{3}(\d)\d{3}.*\s\d(\d)\d\s.*?(\d+)',content)
print(res.group(1))
print(res.group(2))
print(res.group(3))