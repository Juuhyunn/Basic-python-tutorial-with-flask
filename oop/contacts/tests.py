import unittest
from oop.contacts.models import Contacts


class TestContacts(unittest.TestCase):
    def test_contacts(self):
        ls = []
        c = Contacts()
        ls.append(c.set_contact('name1', 'phone1', 'email1', 'address1'))
        ls.append(c.set_contact('name2', 'phone2', 'email2', 'address2'))
        c.get_contact(ls)
        c.del_contact(ls, 'name2')
        self.assertEqual(ls[0].name, 'name1')