import matplotlib.pyplot as plt
import numpy as np
from icecream import ic



class NumpyLib(object):
    def show_numpy(self):
        t = np.arange(0., 5., 0.2)
        plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
        plt.show()

    def numpy_choice(self):
        dice = np.random.choice(6, 1000000, p=[.1, .2, .3, .2, .1, .1])
        plt.hist(dice, bins=6)
        plt.show()

    '''
    np.random.randint(low=10, high=100, size=200)
    low ~ high 추출되는 숫자의 범위
    size 추출되는 데이터의 숫자
    '''

    def numpy_not_need_for_loop(self):
        x = np.random.randint(low=10, high=100, size=200)
        y = np.random.randint(low=10, high=100, size=200)
        size = np.random.randint(100) * 100
        plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
        plt.colorbar()
        plt.show()

    def indexing_slicing(self):
        a = np.array([1, 2, 3, 4])
        ic(f'list -> array (내부 연산의 loop을 돌리지 않기 위하여) : \n {a}')  # [1 2 3 4]가 출력됨. 쉼표가 없다. 루프를 쓸 필요가 없다,
        ic(f'indexing a[1] : {a[1]} \nindexing a[-1] : {a[-1]}')
        ic(f'slicing a[1:] : {a[1:]}')

    def array_have_to_one_type(self):
        a = np.array([1, 2, '3', 4])
        ic(f'int -> str : {a}')

    def np_zeros(self):
        ic(np.zeros(10))

    def np_ones(self):
        ic(np.ones(10))

    def np_eye(self):
        ic(np.eye(3))

    def np_arange(self):
        ic(f' [0 1 2] : {np.arange(3)}')
        ic(f' [3 4 5 6] : {np.arange(start=3, stop=7)}')
        ic(f' [3 5] : {np.arange(start=3, stop=7, step=2)}')
        ic(f' [1.  1.2 1.4 1.6 1.8] : {np.arange(start=1, stop=2, step=.2)}')
        ic(f' [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. ] : {np.linspace(1, 2, 11)}')

    def np_linespace(self):
        ic(f' [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. ] : {np.linspace(1, 2, 11)}')
        a = np.linspace(1, 2, 11)
        ic(f'{np.sqrt(a)}')
        '''
        [1.         1.04880885 1.09544512 1.14017543 1.18321596 1.22474487
         1.26491106 1.30384048 1.34164079 1.37840488 1.41421356]
        '''

    def np_mask(self):
        a = np.arange(-5, 5)
        ic(f'mask [-5 -4 -3 -2 -1] : {a[a < 0]}')
        mask1 = abs(a) > 3
        ic(f'mask [-5 -4  4] : {a[mask1]}')
        mask2 = abs(a) % 2 == 0
        ic(f'mask + (Java에서 || 연산) [-5 -4 -2  0  2  4] : {a[mask1 + mask2]}')
        ic(f'mask * (Java에서 && 연산) [-4  4] : {a[mask1 * mask2]}')

    def np_bubble(self):
        x = np.random.randint(-100, 100, 1000)
        y = np.random.randint(-100, 100, 1000)
        size = np.random.randint(100) * 100
        mask1 = abs(x) > 50
        mask2 = abs(y) > 50
        x = x[mask1 + mask2]
        y = y[mask1 + mask2]
        plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
        plt.colorbar()
        plt.show()