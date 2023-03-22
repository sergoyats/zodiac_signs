from django.test import TestCase


class TestHoroscope(TestCase):
    # каждая функция тестирует одно представление:
    def test_index(self):
        response = self.client.get('/horoscope/')  # .client заменяет собой браузер
        self.assertEqual(response.status_code, 200)

    def test_gemini(self):
        response = self.client.get('/horoscope/gemini')
        self.assertEqual(response.status_code, 200)
        # self.assertIn('какая подстрока ищется', 'в какой строке'):
        self.assertIn('Близнецы - третий знак зодиака, Меркурий (с 22 мая по 21 июня).',
                      response.content.decode())  # .decode() для перевода байтов в стоковые символы

    def test_gemini_redirect(self):
        response = self.client.get('/horoscope/3')
        self.assertEqual(response.status_code, 302)  # 302 ─ код перенаправления на /horoscope/gemini
        self.assertEqual(response.url, '/horoscope/gemini')