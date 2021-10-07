from book_modu.pop_structure_visual.models import Population

if __name__ == '__main__':
    pop = Population()
    # pop.pop_per_dong('방이1동')
    pop.show_plot(pop.pop_per_dong('방이1동'))
