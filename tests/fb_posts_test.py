import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import shelve
import time
from fb_scrapper import save_shelve,  get_tstamp, get_access
from fb_posts import getFacebookPageFeedData
def test_func(page_id,d):
    if page_id in d:
        return 1
    else:
        return 0

class MyTest(unittest.TestCase):
    def test_save_shelve(self):
        save_shelve("13142345","test")
        d = shelve.open('test')
        self.assertEqual(test_func("13142345",d), 1)
    def test_tstamp(self):
        self.assertEqual(get_tstamp("13142345", 0,"test"),-2180131200)
    def test_tstamp2(self):
        timestamp = int(time.time())
        d = shelve.open("test")
        d["13142345"] = timestamp
        self.assertEqual(get_tstamp("13142345", 1,"test"), str(timestamp))
    def test_access_t(self):
        self.assertEquals(get_access("54449",'text.txt'),"54449|awerqwerdummytext")
    def test_getFacebookPageFeedData(self):
        access = "238791666290359|" + os.environ['FB_KEY']
        data = getFacebookPageFeedData("176485839144245", access, 100, 0 )
        if("message" in data["data"][0]):
            good = 1
        else:
            good = 2
        self.assertEquals(good,1)









    #Fix timeout errors



if __name__ == '__main__':
    unittest.main()
