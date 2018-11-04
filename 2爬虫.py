from requests_html import HTMLSession
import pandas as pd
session = HTMLSession()
url = 'https://blog.snowstar.org/'
r = session.get(url)
sel = '#post-任意数字 > header > div > div > h2 > a'
def get_text_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            mylink = list(result.absolute_links)[0]
            mylist.append((mytext,mylink))
        return mylist
    except:
            return None
df = pd.DataFrame(get_text_link_from_sel(sel))
df.columns = ['title', 'link']
df
