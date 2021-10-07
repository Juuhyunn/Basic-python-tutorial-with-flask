class Chuck(object):

    def int_to_bin(self, a : int):
        return bin(a)

    def bin_to_str(self, a) -> []:
        ls = []
        [ls.append(str(a)[i]) for i in range(len(str(a)))]
        del ls[0:2]
        print('2진수 표현 : ' + ''.join(ls))
        return ls

    def list_to_chuck(self, ls : []) -> []:
        # print(f'변환 전 : {ls}')
        for i,j in enumerate(ls):
            if j == '1':
                ls[i] = '0'
            elif j == '0':
                ls[i] = '00'
        return ls

    def make_chuck(self, ls : []) -> []:
        result = []
        ls.append('가짜값')
        # print(f'척 값 만들기 전 : {ls}')
        n = 1
        for i, j in enumerate(ls):
            if i == len(ls)-1:
                pass
            elif j != ls[i+1]:
                result.append(str(f'{j} {"0"*n} '))
                n = 1
            elif j == ls[i+1]:
                n += 1
        return result

    def chuck_to_str(self, ls: []) -> str:
        return ''.join(ls)
