from bs4 import BeautifulSoup
import requests

# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")[0]

print(tags.find_all("b"))

# HTML From Website
url = "https://www.flipkart.com/caddle-toes-famous-car-remote-control-3d-led-lights-chargeable/p/itm700e6f8007130?pid=RCTGZHYYCGGYSG3P&lid=LSTRCTGZHYYCGGYSG3POQ9BAC&marketplace=FLIPKART&store=tng%2F56a%2Ffq8&srno=b_1_1&otracker=browse&fm=organic&iid=en_NAPirp6oM6HtijDcFcgTKpUrLhGrTLbxD7h6Kn7CYRwQTgvAjplb4T1ZZmE_RSh5AuJu5tpZasAMwkbAVxsodA%3D%3D&ppt=None&ppn=None&ssid=i4n5epk2hc0000001726931840307"

result = requests.get(url)
print(result.text)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
