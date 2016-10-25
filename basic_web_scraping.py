################3
import requests
import json
# h = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
# p = {"t" : "day"}

# req = requests.get("https://oauth.reddit.com/r/python/top", headers = h, params = p)
# python_top = req.json()

# print req.status_code

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content
from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With beautifulsoup, we can access branches by simply using tag types as 
body = parser.body

# Get the p tag from the body.
p = body.p
title_text = parser.head.title.text
# Print the text of the p tag.
# Text is a property that gets the inside text of a tag.
print content
print(p.text)
print (title_text)