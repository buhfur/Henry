import win32com.client as wincl
import requests
import webbrowser
from bs4 import BeautifulSoup
#ryan mcvicker

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
        self.search = search(self.query, start=0, stop=10, num=10)
        return self.search

    #creates a directory, then downloads the pdfs
    def find_pdf(self,query,num_of_results=10,file_path=None):



        if not file_path:
            #put pdfs in folder in current working directory
            self.dir = os.mkdir(join(os.cwdir(),"HenryPDF"))

        else:
            try:
                #default dir for pdfs is C:\HenryPDF
                self.dir = os.mkdir("HenryPDf")

            #throws exception for unittests
            except IOError:
                return "FAILED TO CREATE HenryPDF"


        num_of_results = num_of_results or 10

        #download the files from the url

        search_results = search(query, start=0,
        stop=num_of_results)
        #now save all the files in the folder

        results = [result for x in search_results]
        #SOME OF THIS CODE WAS TAKEN FROM https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un


        for url in results:
            #download the pdf and add them to the directory
            r = requests.get(url, allow_redirects=True)
            #split the url to get the name of the file
            split_url = [s_url for sp_url in url.split("/")]
            #now open a file with the name of the last index
            with open(split_url[-1], "wb") as pdf_file:
                pdf_file.write(r.content)
                #henry should be asked to open a specific one






    def open_pdf(self,url):
        #use the web browser module to open the urls
        file_path = file_path or None
        #how to open downloaded pdf???
        if not file_path:
            return "you must have a file path to open a pdf"

        #how to open pdf with a web browser


        webbrowser.open(r"file://C:\Henry\HenryPDF\{}".format(url))





    def find_documentation(self, subject):
        pass
