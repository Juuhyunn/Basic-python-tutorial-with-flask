import matplotlib.pyplot as plt
from common.menu import print_menu

"""
list 값은 y축이고, x축은 0부터 자동으로 증가한다.
색깔은 color
linestyle은 ls
그래프 이름은 label
범례는 plt.legend()
"""


class BasicPlot(object):

    def plot_show(self):
        plt.title("Plotting")
        plt.plot([10, 20, 30, 40], color='r', ls='--', label='asc')
        plt.plot([40, 30, 20, 10], color='g', ls=':', label='desc')
        plt.legend()
        plt.show()
    """
    첫 번째 list가 x축, 두 번째 list가 y축이다.
    """

    def plot_two_list_show(self):
        plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
        plt.show()
    """
    mark
    색깔 + 원 r.
    색깔 + 삼각형 g^
    """

    def scatter(self):
        plt.title('Marker')
        plt.plot([10, 20, 30, 40], 'r.', label='Circle')
        plt.plot([40, 30, 20, 10], 'g^', label='Triangle_up')
        plt.legend
        plt.show()
