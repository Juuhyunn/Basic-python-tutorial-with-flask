from book_modu.pop_structure_visual_with_pandas.models import Population

if __name__ == '__main__':
    pop = Population()
    # pop.show_plot(pop.pop_per_dong('방이1동'))
    # pop.pop_per_dong('필동')
    name = input('지역?')
    pop.read_data()
    pop.find_home(name)
    pop.home = pop.list_to_array(pop.home)
    pop.find_similar_area(name)
    pop.show_plot_similar_two_cities(name, pop.home, pop.away)