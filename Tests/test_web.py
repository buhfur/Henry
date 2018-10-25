import unittest
import Web from Web


class TestWeb(unittest.TestCase):
    def setup(self):
        self.web_obj = Web()

    def test_google_search(self):
        search_results = self.web_obj.search_google("python")
        self.assertTrue(search_results)
