from bs4 import BeautifulSoup as bs
import requests 
import pprint

VOTE_NUMBERS = 100

url ="https://news.ycombinator.com/"
res = requests.get(url=url)



soup = bs(res.text, "html.parser")
titleline_raw = soup.select(".titleline")
votes_raw = soup.select(".score")

if len(titleline_raw) == len(votes_raw):
    titleline = [item.select("a")[0].get("href") for item in titleline_raw]
    votes = [item.contents for item in votes_raw]

    concatenate_info = list(zip(titleline, votes))
    filtered_list = list(filter(lambda x: int(x[1][0].strip(" points"))>= VOTE_NUMBERS, concatenate_info))
    print(filtered_list)
else:
    print("One or more title(s) don't have a vote")