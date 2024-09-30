# This scrapes data from https://searx.be
# No docs yet, but I'll maybe make a library for this

from requests import get
from bs4 import BeautifulSoup as bs

_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}

def _query_to_url(query):
    query = query.replace(" ", "+")
    return "https://searx.be/search?q=" + query

def _get_instant_results(bs_obj) -> str | None:
    result = bs_obj.find("p", {"class": "infobox_part"})
    if result is None:
        return None

    return result.text

def _get_first_url_data(bs_obj) -> str:
    first_div = bs_obj.find("div", {"class": "result"})
    
    p = first_div.find("p")
    a = first_div.find("a")
    
    if a:
        desc = a
    else:
        desc = p

    return desc.text


def search(query: str):
    url = _query_to_url(query)
    response = get(url, headers=_headers)

    if response.status_code != 200:
        return None
    
    
    soup = bs(response.text, "html.parser")
    result_element = soup.find("div", {"class": "container"})
    
    instant_results = _get_instant_results(result_element)
    if not instant_results is None:
        return instant_results
    
    first_url_data = _get_first_url_data(result_element)
    return first_url_data