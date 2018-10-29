import unittest
try:



class TestWeb(unittest.TestCase):


    def test_google_search(self):
        search_results = self.web_obj.search_google("python")
        self.assertTrue(search_results)

    def test_find_pdf(self):
        #downloads a list of pdfs
