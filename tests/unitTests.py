import sys, os
import unittest
sys.path.insert(1, './source/')
from twitter import Twitter
from g_vision import getImageDescription
from api import app


class APPTESTS(unittest.TestCase):
    def test_twitter(self):
        tweets = Twitter("Reuters").feed
        assert tweets != []
        assert tweets is not None

    def test_image(self):
        imageURL = "https://rgbd-dataset.cs.washington.edu/imgs/rgbd_dataset2.png"
        image = getImageDescription(imageURL)
        assert image.objects is not None
        assert image.objects != []

    def test_get(self):
        client = app.test_client()
        data = client.get('/user?twittername=Reuters')
        assert data._status_code == 200
        
if __name__ == '__main__':
    unittest.main()