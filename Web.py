import win32com.client as wincl
import requests
from bs4 import BeautifulSoup


try:
    from googlesearch import search
except ImportError:
    print("no module found named google")


#this file is more about the functionality, rather than the
#interaction between the user and henry

class Web:



    def search_google(self, query):
        #make a google query
        self.query = query
        self.search = search(self.query, start=0, stop=10, num=10, safe='on')
        return self.search


    def find_pdf(self):
        return


    def find_documentation(self, subject):
        return
