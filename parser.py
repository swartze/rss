import requests
import xml.etree.ElementTree as ET


url = "https://lifehacker.com/rss"
r = requests.get(url, allow_redirects=True)

tree = ET.parse(r.content)
root = tree.getroot()
for child in root:
    print(child.tag)
