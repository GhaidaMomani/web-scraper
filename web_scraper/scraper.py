import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
  citations = 0
 
  page = requests.get(url)

  soup = BeautifulSoup(page.content, 'html.parser')

  titles = soup.find_all('a')
 
  for title in titles:
    if title.text == 'citation needed':
      citations+=1
      
  return citations

def get_citations_needed_report(url):
  passages = ''
 
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  titles = soup.find_all('p')

  for title in titles:
    if 'citation needed' in title.text:
      passages += title.text
  passages = passages.replace("'\n '", ' ')
  print(passages)
  return passages




if __name__=="__main__":
    url="https://en.wikipedia.org/wiki/History_of_Mexico"
    get_citations_needed_count(url)
    get_citations_needed_report(url)