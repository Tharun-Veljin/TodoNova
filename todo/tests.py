from django.test import TestCase
from django.urls import reverse

class TodoViewsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('todo:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse('todo:about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse('todo:contact'))
        self.assertEqual(response.status_code, 200)

    def test_course_page(self):
        response = self.client.get(reverse('todo:course'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_page(self):
        response = self.client.get(reverse('todo:gallery'))
        self.assertEqual(response.status_code, 200)

