import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app

class ViewTest(TestBase):
def test_homepage_view(self):
    response =self.client.get(url_for('home'))
    self.assertEqual(response.status_code, 200)

def test_generator_view(self):
    response =self.client.get(url_for('generator'))
    self.assertEqual(response.status_code, 200)

def test_generator_view(self):
    response =self.client.get(url_for('generator'))
    self.assertEqual(response.status_code, 500)

