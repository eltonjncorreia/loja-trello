from django.test import TestCase
from django.shortcuts import resolve_url as r


class StoreHomeTest(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.resp = self.client.login(username='ejnc', password='ejnc')
        self.resp = self.client.get(r('store:home'))

    def test_get_status(self):
        self.assertEqual(200, self.resp.status_code)

    def test_tem_template(self):
        self.assertTemplateUsed(self.resp, 'store/home.html')
