import requests 
from bs4 import BeautifulSoup

#----------------------------------------------------------------------------------------------------
link = None
while link == None:  # <----- This code here is going to get the link properly, without input errors
    try:
        page = int(input("\nWhich page do you want to see? 1-50\n").strip())
    except ValueError:
        print("Please, you should put the input as an integer")
        continue
    if page == 1:
        link = "http://books.toscrape.com/"
    elif page <= 50:
        link = f"http://books.toscrape.com/catalogue/page-{page}.html"
    else:
        print("List out of range, please, choose a page between 1 and 50")
#----------------------------------------------------------------------------------------------------
response = requests.get(link)
html = response.text
soup = BeautifulSoup(html, "html.parser")

titles = [a.get("title") for a in soup.find_all("a") if a.get("title") != None]
prices = [p.get_text().replace("Â", "") for p in soup.find_all("p", class_="price_color")]
#----------------------------------------------------------------------------------------------------
print("\n\n"+"-"*150) 
for title, price in zip(titles, prices):
    print(f"Book: {title}{" "*(120-len(title))}| Price: {price}")
print("-"*150+"\n\n")
#----------------------------------------------------------------------------------------------------
