from django.test import TestCase


class ProdutoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/api/v1/produtos')

    def test_get_status(self):
        self.assertEqual(200, self.resp.status_code)
