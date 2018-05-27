from django.test import TestCase


class EstoqueApiTeste(TestCase):
    def setUp(self):
        self.resp = self.client.get('/api/v1/estoques')

    def test_get_status(self):
        self.assertEqual(200, self.resp.status_code)