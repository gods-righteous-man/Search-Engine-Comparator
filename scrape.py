from bs4 import BeautifulSoup
from time import sleep
import requests
from random import randint
from html.parser import HTMLParser
import time
import json
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
class SearchEngine:
 @staticmethod
 def search(query, sleep=True):
    if sleep: # Prevents loading too many pages too soon
        time.sleep(randint(10, 20))
        temp_url = '+'.join(query.split()) #for adding + between words for the query
        print(temp_url)
        url = 'https://www.duckduckgo.com/html/?q=' + temp_url + '&n=1'
        print(url)
        soup = BeautifulSoup(requests.get(url, headers=USER_AGENT).text,
        "html.parser")
        # print(soup)
        new_results = SearchEngine.scrape_search_result(soup)
    return new_results
 @staticmethod
 def scrape_search_result(soup):
    raw_results = soup.find_all("a", attrs = {"class" : "result__a"})
    results = []
    #implement a check to get only 10 results and also check that URLs must not be duplicated
    for result in raw_results:
        link = result.get('href')
        results.append(link)
        # print(results)
        if len(results) == 10:
            break
    return results
8
#############Driver code############

data = {}
with open ('queries.txt') as file:
    for item in file:
        print(item)
        r = SearchEngine.search(item)
        data[item] = r
        


# r = list(r)
# data = {
#     "andrew tate" : r
# }


# with open('sample.json', 'r') as json_file:
#     json_decoded = json.load(json_file)

# json_string = json.dumps(data)

with open('sample.json', 'w') as json_file:
    json.dump(data, json_file)



# print(r)
print(len(r))
####################################