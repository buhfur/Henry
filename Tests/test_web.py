import unittest
try:
    #import the Web.py module
    from Web import Web

except ImportError:
    print("couldent import web")




class TestWeb(unittest.TestCase):


    def test_google_search(self):
        search_results = self.web_obj.search_google("research paper pdf")
        self.assertTrue(search_results)

    def test_find_pdf(self):
        #downloads a list of pdfs
        #create a test directory for the test files to be put in
        test_query = Web.search_google("research paper pdf")
        #use test_query
        test_find = Web.find_pdf(test_query)



if __name__ == '__main__':
    unittest.main()
