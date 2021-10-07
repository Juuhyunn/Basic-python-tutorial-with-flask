class Menu(object):

    def print_menu(ls):
        t = ''
        for i, j in enumerate(ls):
            t += str(i) + '. ' + j + '\t'
        return int(input(t))