from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")[0]
b_tags = tags.find_all("b")

if b_tags:
    for b_tag in b_tags:
        print(b_tag.text)
else:
    print("No <b> tags found in the first <p> tag")

url = "https://www.noon.com/uae-en/iphone-15-pro-max-256gb-natural-titanium-5g-with-facetime-middle-east-version/N53432547A/p/?o=e42a70af119ca6de"

result = requests.get(url)

if result.status_code == 200:
    doc = BeautifulSoup(result.text, "html.parser")

    price_tag = doc.find("div", class_="_30jeq3 _16Jk6d")

    if price_tag:
        print(f"Price: {price_tag.text}")
    else:
        print("Price not found on the webpage")
else:
    print(f"Failed to retrieve the webpage. Status code: {result.status_code}")
