from django.test import TestCase


class PeditoApiTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/api/v1/pedidos')

    def test_get_status(self):
        self.assertEqual(200, self.resp.status_code)