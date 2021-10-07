from book_modu.basic_hist.models import BasicHist

if __name__ == '__main__':
    this = BasicHist()
    # this.hist_show(dice(int(input('How much?'))))
    # ls = []
    # while 1:
    #     menu = int(input('1. add else. show'))
    #     [ls.append(this.highest_temperature(input('Month?'))) if menu == 1 else this.hist_show_many(ls)]
    this.show_hist_about(this.highest_temperature('01'), '01')