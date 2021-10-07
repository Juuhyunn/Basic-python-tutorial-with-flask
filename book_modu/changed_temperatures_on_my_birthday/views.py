from book_modu.changed_temperatures_on_my_birthday.models import ChangedTemperaturesOnMyBirthday

if __name__ == '__main__':
    this = ChangedTemperaturesOnMyBirthday()
    this.read_data()
    this.save_highest_temperature()
    # this.visualize_data()
    # # print(this.find_month_using_split())
    this.read_data()
    this.highest_temperatures_my_birthday()