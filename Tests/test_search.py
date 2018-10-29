import unittest
from googlesearch import search


class TestSearch(unittest.TestCase):



    def test_search(self):
        self.assertTrue(search(query="pdf research paper"))
        query_search = search(query="research paper pdf",
        start=0, stop=10)
        for new in query_search:
            print(new)









if __name__ == '__main__':
    unittest.main()
