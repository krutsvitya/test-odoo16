from odoo.tests.common import TransactionCase, tagged


class TestDeveloper(TransactionCase):

    def test_create_developer(self):
        developer = self.env['developer'].create({
            'name': 'John',
            'type': 'front-end',
            'phone': '+1234567890',
            'email': 'john@example.com',
        })

        self.assertTrue(developer.name.istitle())  # checking if all words start with a capital letter

        self.assertIn('+', developer.phone)  # checking if there is a + in the phone number

        self.assertIn('@', developer.email)  # checking if @ is in email
