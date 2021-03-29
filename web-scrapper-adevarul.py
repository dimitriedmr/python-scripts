# adevarul scrapping de articole
import unidecode
import requests
import urllib.request
import re
import pandas
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class Search:
    def __init__(self, terms, pages, startDate, endDate):
        '''
        Search constructor
        '''
        self.url = 'https://adevarul.ro'
        self.searchDictionary = { 
                                'terms'     : '', 
                                'fromDate'  : startDate, 
                                'toDate'    : endDate,
                                'tab'       : 'mrarticle', 
                                'page'      : 1 
                                }
        # compile all url queries
        self.urlQueryList = []
        for keyWord in terms:
            for page in pages:
                urlQuery = self.url + '/cauta/?'
                for searchKey, searchValue in self.searchDictionary.items():
                    urlQuery += f'&{searchKey}='
                    if searchKey == 'terms':
                        urlQuery += keyWord
                    elif searchKey == 'page':
                        urlQuery += str(page)
                    else:
                        urlQuery += searchValue
                self.urlQueryList += [urlQuery]
    
    def fixMonth(self, datainput):
        '''
        date fix
        '''
        date = {
            "Ian" : "01", "ianuarie" : "01",
            "Feb" : "02", "februarie" : "02",
            "Mar" : "03", "martie" : "03",
            "Apr" : "04", "aprilie" : "04",
            'May' : '05', "mai" : "05",
            'Jun' : '06', "iunie" : "06",
            'Jul' : '07', "iulie" : "07",
            'Aug' : '08', "august" : "08",
            'Sep' : '09', "septembrie" : "09",
            'Oct' : '10', "octombrie" : "10",
            'Nov' : '11', "noiembrie" : "11",
            'Dec' : '12', "decembrie" : "12",
        }
        for key, value in date.items():
            datainput = datainput.replace(key, value)
        return datainput

    def parseQueries(self, columns):
        '''
        It saves the necessary information inside a data frame.
        '''
        results = {el : [] for el in columns}
        for query in self.urlQueryList:
            webPage = requests.get(query)
            webPageText = BeautifulSoup(webPage.text, "html.parser")
            articlesList = webPageText.find("ul", class_ = 'article-list')
            for elements in articlesList.find_all('li'):
                # get article link
                articleLinkPart = elements.find('a', href = True)
                if not articleLinkPart:
                    continue
                link = self.url + articleLinkPart['href']
                # get article lead
                articleWebPage = requests.get(link)
                if not articleWebPage:
                    continue
                articleWebPageText = BeautifulSoup(articleWebPage.text, "html.parser")
                articleContent = articleWebPageText.find("div", class_ = 'article-content')
                if not articleContent:
                    break
                # get article title
                title = ' '.join(articleLinkPart.text.split())
                title = unidecode.unidecode(title)
                title = title.replace(',,', '\"')
                # get article date
                data = ' '.join(re.findall(r"\d+:\d+|\w+", elements.find("span", class_ = 'time').text))
                data = self.fixMonth(data)
                if not data:
                    continue
                # get article lead
                lead = f"{articleContent.find('h2', class_ = 'articleOpening').text}"
                lead = ' '.join(lead.split())
                lead = lead.replace(',,', '\"')
                # get article article
                article = f"{articleContent.find('div', class_ = 'article-body').text}"
                article = ' '.join(article.split())
                article = article.replace(',,', '\"')
                
                print(title)
                for column, value in zip(columns, [data, link, title, lead, article]):
                    results[column] += [value]
        return results
        
if __name__ == '__main__':
    searchTerms = ['caracal']
    s = Search(searchTerms, range(1, 37 + 1), '2019-7-25', '2021-3-17')
    # data frame with the final table
    columns = ["data", "link", "titlu", "lead", "articol"]
    results = s.parseQueries(columns)
    dataFrame = pandas.DataFrame(results)
    dataFrame.to_csv(f'{urlparse(s.url).netloc[:-3]}_{"_".join(searchTerms)}.csv')
    for column in columns[:-1]:
        del dataFrame[column]
    dataFrame.to_csv(f'{urlparse(s.url).netloc[:-3]}_{"_".join(searchTerms)}_articol.csv')