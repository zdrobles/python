import requests
from bs4 import BeautifulSoup


# creates a recipe obj for each recipe and requests the ingredients from the link
def recipeLink(name, link):
    recipe = Recipe(name, link)

    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    s = soup.find("div", {"class": "fela-_g6xips"})

    recipe.set_ingredients(s.text)
    mylist.append(recipe)


class Recipe:
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def get_ingredients(self):
        return self.ingredients


mylist = []

res = requests.get("https://www.hellofresh.com/recipes/hall-of-fame?page=100")
soup = BeautifulSoup(res.content, 'html.parser')

s = soup.find_all(class_="web-wpfcry")
for i in range(len(s)-5):
    recipeLink(s[i].text, s[i]["href"])

for item in mylist:
    print(item.name)
    if len(item.get_ingredients()) == 0:
        print("NO INGREDIENTS FOUND")
    else:
        print(item.get_ingredients())

# link = "https://www.hellofresh.com/recipes/winner-winner-chicken-orzo-dinner-5aaabf7530006c52b54bd0c2"
# page = requests.get(link)
# soup = BeautifulSoup(page.content, 'html.parser')

# s = soup.find("div", {"class": "fela-_g6xips"})
# print(s.text)
