from book_algorithm_interview.string_tutorial.models import StringConversion

if __name__ == '__main__':
    stringConversion = StringConversion()
    ls = stringConversion.str_to_list(input("Input"))
    resversed_ls = stringConversion.reverse_list(ls)
    print(stringConversion.list_to_str(resversed_ls))