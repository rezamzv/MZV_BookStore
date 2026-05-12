from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_reverse_url(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_url(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, 'Home Page')

    def test_home_page_template(self):
        response = self.client.get(reverse('home_page'))
        self.assertTemplateUsed(response, 'home.html')