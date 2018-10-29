import unittest



class TestGit(unittest.TestCase):

    def setup(self):
        #setup git account infomration
        #git commands will always catch HttpException
        self.username = ""
        self.password = ""

    def test_git_download(self):
        
