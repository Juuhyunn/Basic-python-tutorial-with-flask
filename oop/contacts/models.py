from icecream import ic


class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        return ic(f'!name : {self.name}\tphone : {self.phone}\temail : {self.email}\taddress : {self.address}')

    @staticmethod
    def set_contact() -> object:
        return Contacts(input('name : '), input('phone :'), input('email : '), input('address : '))

    @staticmethod
    def get_contact(ls):
        for i in ls:
            Contacts(input('name : '), input('phone :'), input('email : '), input('address : ')). to_string()
            i.to_string()

    @staticmethod
    def del_contact(contacts, n):
        for i, j in enumerate(contacts):
            if n == j.name:
                del contacts[i]
                ic('!!Delete Complete!!')
        '''
        for i in contacts:
        if name == i.name:
            contacts.remove(i)
            ic('!!Delete Complete!!')
        '''

    @staticmethod
    def menu(ls) -> int:
        for i, j in enumerate(ls):
            ic(f'{i}.  {j}')
        return int(input())
        '''
        lis = []
        for i in ls:
            ic(f'{ls.index(i)}. {i}\t')
        '''

    @staticmethod
    def main():
        ls = []
        # c = Contacts()
        while 1:
            m = Contacts.menu(['Exit', 'Add', 'Print', 'Delete'])
            if m == 0:
                return
            elif m == 1:
                t = Contacts.set_contact()
                ls.append(t)
            elif m == 2:
                Contacts.get_contact(ls)
            elif m == 3:
                Contacts.del_contact(ls, input('Del Name : '))
            else:
                ic('Wrong Input')
                break
