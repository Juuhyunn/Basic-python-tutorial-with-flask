from mine.al_test.models import Chuck

if __name__ == '__main__':
    this = Chuck()
    print(this.chuck_to_str(this.make_chuck(this.list_to_chuck(this.bin_to_str(this.int_to_bin(int(input('Input Int'))))))))
