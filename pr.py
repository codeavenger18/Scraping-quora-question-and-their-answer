from bs4 import BeautifulSoup
#import requests
import re
import urllib
import json
import timeit
from multiprocessing import Pool
import multiprocessing

start = timeit.default_timer()

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

def parse(url):
    start = timeit.default_timer()
    print(url)
    try:
        soup = get_soup(url,header)
        html=urllib.request.urlopen(urllib.request.Request(url,headers=header)).read()
    except:
        return
    urls=[]
    try:
        cnt=soup.find('div',{'class':'answer_count'})
        cnt_a=cnt.text
        print(cnt_a)
    except:
        return
    for foo in soup.findAll("div", {"class": "ui_qtext_expanded"}):
        #print(foo.span.text+'\n\n\n')
        query=foo.span.text
        urls.append(query)
    try:
        file=open("final1.txt","a+")
        for s in urls:
            file.write(str(s)+'\n\n')
            file.write('\n\n\n\n\n\n')
        file.close()
    except:
        return
    stop = timeit.default_timer()
    print(len(urls))
    print('\n'+'Time :')
    print(stop-start)
    print('\n\n')

with open("link.txt","r") as f:
    data_links=f.readlines()

#for i in range (0,len(data_links)):
#parse(data_links[0])

if __name__ == '__main__':
    processes = []
    for i in data_links:
        p = multiprocessing.Process(target=parse, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
stop = timeit.default_timer()
print('Time: ', stop - start)
