import pprint
from icecream import ic


class Palindrome(object):
    def str_to_list(self, payload : str) -> []:
        '''strs = []
        for char in payload:
            if char.isalnum():
                strs.append(char.lower())
        return strs
        '''
        return [i for i in payload if i.isalnum()]


    def isPalindrome(self, ls: [])->bool:
        '''
            while len(ls) > 1:
            if ls.pop(0) != ls.pop():
                return False
            else:
                return True
        '''
        while len(ls) > 1:
            return [False if ls.pop(0) != ls.pop() else True]
