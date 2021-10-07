from scraping.music.models import Music, View

if __name__ == '__main__':
    view = View()
    view.modeling('melon.csv', 'bugs.csv')
    Music.main()