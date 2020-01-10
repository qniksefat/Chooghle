#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import time


# In[2]:


def get_paper_info(link, refrences):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                                 '63.0.3239.132 Safari/537.36 OPR/50.0.2762.67',}
    req = requests.get(link, headers)
    bs = BeautifulSoup(req.text, 'html.parser')
    title = bs.find_all('h1', {"data-selenium-selector": "paper-detail-title"})[0].contents[0]

    abstract_element = bs.find("meta", {"name":"twitter:description"})
    abstract = abstract_element.attrs["content"]

    tmp = bs.find("span" ,{'data-selenium-selector':"paper-year"})
    try:
        publish_year = tmp.find('span').contents[0].contents[0]
    except:
        publish_year = bs.find('li', {'class': 'citation__meta__publication__item'}).contents[0]
    author_names = [author.attrs['content'] for author in bs.find_all('meta', {'name': 'citation_author'})]
    refrences = bs.find("div", {"class": "citation-list__citations"})
    top_ref_titles = []
    top_ref_links = []
    for item in refrences.contents:
        try:
            ref_title = item.find("h2").attrs["data-heap-paper-id"]
            if ref_title != '':
                top_ref_titles.append(ref_title)
                top_ref_links.append('https://www.semanticscholar.org' + item.find('a').attrs['href'])
        except Exception as e:
            print(e)
    return {
        'id': link.split('/')[-1],
        'title': title,
        'abstract': abstract,
        'publish_year': publish_year,
        'author_names': author_names,
        'refrences': top_ref_titles, 
        'top_ref_links': top_ref_links
    }


# In[3]:


q = ['https://www.semanticscholar.org/paper/Tackling-Climate-Change-with-Machine-Learning-Rolnick-Donti/998039a4876edc440e0cabb0bc42239b0eb29644',
'https://www.semanticscholar.org/paper/Sublinear-Algorithms-for-(%CE%94%2B-1)-Vertex-Coloring-Assadi-Chen/eb4e84b8a65a21efa904b6c30ed9555278077dd3',
'https://www.semanticscholar.org/paper/Processing-Data-Where-It-Makes-Sense%3A-Enabling-Mutlu-Ghose/4f17bd15a6f86730ac2207167ccf36ec9e6c2391']


# In[ ]:


papers = []
result = []
n = input("enter number of papers you want to crawl! ")
while q:
    url = q.pop(0)
    try:
        info_dict = get_paper_info(url, papers)
        papers.append(info_dict["refrences"])
    except:
        continue
    q.extend([item for item in info_dict.pop("top_ref_links") if item not in papers])
    result.append(info_dict)
    time.sleep(0.01)
    if len(result) % 5 == 0:
        print(len(result))
    if len(result) == n:
        break
    

