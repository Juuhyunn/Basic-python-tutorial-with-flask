from icecream import ic

# example 1


class OneToTenSum(object):

    def one_to_ten_sum_1(self):
        sum = 0
        for i in range(1, 11):
            sum += i
        ic(sum)

    #example 2
    def one_to_ten_sum_2(self):
        ic(sum(i for i in range(1, 11)))

    #example 3
    def one_to_ten_sum_3(self):
        ic(sum(range(1, 11)))