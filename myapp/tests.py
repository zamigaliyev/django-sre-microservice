from django.test import TestCase


class MyViewTests(TestCase):
    def test_my_view(self):
        response = self.client.get('/api/v1/resource/?param1=test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())
