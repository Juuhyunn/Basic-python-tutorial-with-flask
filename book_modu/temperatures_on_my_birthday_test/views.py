from book_modu.temperatures_on_my_birthday_test.models import TemperaturesOnMyBirthdayTest

if __name__ == '__main__':
    this = TemperaturesOnMyBirthdayTest()
    this.read_data()
    this.save_data_to_list()
    this.extracting_date()