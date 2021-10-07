import pandas as pd
from icecream import ic


class Olympic(object):

    def read_wiki(self) -> object:
        df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
        ic(df)
        return df