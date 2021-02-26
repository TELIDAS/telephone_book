from django.test import TestCase
from phonebook.models import PhoneNumber


class TestModel(TestCase):
    """
    Testing PhoneNumber models successful creation and failure creation.
    """

    def test_create_model_success(self):
        payload = {
            'number': '+996775071204',
            'name': 'Ruslan Sapataev',
        }
        phone = PhoneNumber.objects.create(**payload)
        self.assertEqual(phone.number, payload['number'])
        self.assertEqual(phone.name, payload['name'])

    def test_create_model_fail(self):
        payload = {
            'number': '+996776434334',
            'namee': 'Adilet Saparbek'
        }
        with self.assertRaises(TypeError):
            phone = PhoneNumber.objects.create(**payload)
    """
    Testing model updating function.
    """
    def test_update_model(self):
        new_name = 'Adilet'
        payload = {
            'number': '+996774123456',
            'name': 'Adiletoo'
        }
        phone = PhoneNumber.objects.create(**payload)
        phone.name = new_name
        phone.save()
        phone.refresh_from_db()
        self.assertEqual(phone.name, new_name)

    """
    Testing model deleting function.
    """
    def test_delete_model(self):
        payload = {
            'number': '+996703777111',
            'name': 'Adilet Saparbek',
        }
        phone = PhoneNumber.objects.create(**payload)
        pk = phone.pk
        phone.delete()
        with self.assertRaises(PhoneNumber.DoesNotExist):
            PhoneNumber.objects.get(pk=pk)
