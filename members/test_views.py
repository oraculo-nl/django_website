from unittest import TestCase

from django.test import TestCase
from django.urls import reverse


class HelloViewTests(TestCase):
    def test_return200(self):
        response = self.client.get(reverse('hello-view'))
        self.assertEqual(response.status_code, 200)

    def test_return200_2(self):
        response = self.client.get('/members/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tennis Club')



