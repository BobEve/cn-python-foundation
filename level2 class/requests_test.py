import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
soup = BeautifulSoup(response.text,
                     'html.parser')
content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.find("a", recursive=False):
        first_relative_link = element.find("a", recursive=False).get('href')
        print(first_relative_link)
        break


# TODO: Implement the continue_crawl function described above
def continue_crawl(list_search_history, target_url):
    if len(list_search_history) >= 25:
        print('查找数量超过25条了')
        return False
    if list_search_history[-1] == target_url:
        print('找到"哲学"条目了')
        return False
    if list_search_history[-1] in list_search_history[:-1]:
        # list_search_history[:-1] 左闭右开，如果不包括最后一条数据的列表，如果只有1条数据则得到一个空列表
        print('There is a loop in the page list')
        return False

    return True


target_url = 'https://en.wikipedia.org/wiki/Philosophy'
list_search_history = ['https://en.wikipedia.org/wiki/Philosophy',
                       'https://en.wikipedia.org/wiki/Philosophy1',
                       'https://en.wikipedia.org/wiki/Floating_point']
print(continue_crawl(list_search_history, target_url))
