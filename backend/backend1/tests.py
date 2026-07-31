from django.test import TestCase
from django.urls import reverse

class HelloTest(TestCase):

    def test_hello_url(self):
        response = self.client.get(reverse("hello"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello")