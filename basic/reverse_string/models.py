from icecream import ic


class ReversString(object):

    def str_to_list(self, payload) -> []:
        return [i.lower() for i in payload if i.isalnum()]

    def reverse_string(self, ls: []) -> []:
        #ic(type(ls))
        #ic(type(ls[::-1]))
        return ls[::-1]

    def list_to_str(self, ls) -> str:
        return "".join([i for i in ls])

    def total(self, payload) -> str:
        return "".join([i for i in [i.lower() for i in payload if i.isalnum()][::-1]])
