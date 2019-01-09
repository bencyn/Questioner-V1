#Library imports
import json
# from passlib.hash import pbkdf2_sha256 as sha256
import datetime
from .base_tests import BaseTest
from app.v1.models.meetup_model import Meetup

import unittest
import json
import instance
from app.v1.views import meetup_view
from app.v1.models import meetup_model
from app import create_app

app = create_app("testing")

class TestUser(BaseTest):
    def setUp(self):
        """ defining test data"""
        app.config.from_object(instance.config.TestingConfig)
        self.client = app.test_client

        self.meetup = {
            "topic": "Ethical Hacking Hackathon",
            "location": "Nairobi",
            "images": ["image3.png", "image4.png"],
            "happeningOn": "Monday 12 2018",
            "tags": ["Pentests", "Bruteforce"]
        }
        self.meetup1 = {}
    def test_meeetup_create_record(self):
            url = '/api/v1/meetup/create'
            response= self.client.post(url, data=json.dumps(self.meetup), content_type="application/json")
            result = json.loads(response.data.decode('UTF-8'))

            self.assertEqual(response.status_code, 201)
            self.assertEqual(result["status"], 201)
            self.assertEqual(result["data"], [
                {
                    "topic": "Python",
                    "location": "Nairobi",
                    "happeningOn": "Thursday",
                    "tags": ["RESTful API", "JSON Data"],
                }
            ])
if __name__ == "__main__":
    unittest.main()
   

    