from recipe_scrapers import scrape_me
url='https://www.bbc.co.uk/food/recipes/applecrumble_2971'
# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
scraper = scrape_me(url, wild_mode=True) 

scraper.host()
scraper.title()
scraper.total_time()
scraper.image()
scraper.ingredients()
scraper.instructions()
scraper.instructions_list()
scraper.yields()
scraper.to_json()
scraper.links()
scraper.nutrients()  # if available

print(scraper.host())
print(scraper.title())
print(scraper.total_time())
print(scraper.image())
print(scraper.ingredients())
print(scraper.instructions())
print(scraper.instructions_list())
print(scraper.yields())
print(scraper.to_json())
print(scraper.links())
print(scraper.nutrients())  # if available
