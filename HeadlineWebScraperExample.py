import bs4, requests
def getSkyHeadline(HeadlineURL):
    res = requests.get(HeadlineURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems =  soup.select('body > div:nth-child(6) > div > div > div:nth-child(1) > div > div > h3 > a')
    return elems[0].text.strip()

def getBBCHeadline(BBCurl):
    res = requests.get(BBCurl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#nw-c-topstories-scotland > div > div > div.gel-layout__item.gel-4\/5\@xxl.nw-o-keyline\+\@m.nw-o-no-keyline\@xxl > div > div.gel-layout__item.nw-c-top-stories__primary-item.gel-3\/4\@l.gel-3\/4\@xxl.nw-o-keyline.nw-o-no-keyline\@m > div > div > div.gs-c-promo-body.gs-u-display-none.gs-u-display-inline-block\@m.gs-u-mt\@xs.gs-u-mt0\@m.gel-1\/3\@m > div > a')
    return elems[0].text.strip()

def getC4Headline(C4url):
    res = requests.get(C4url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('''
#latest-tabpanel > div > div > ul.stream.top-stories > li.pinned.count-1 > div > div > a > h3
                        ''')
    return elems[0].text.strip()

HLSky = getSkyHeadline('https://news.sky.com/uk')
HLBBC = getBBCHeadline('https://www.bbc.co.uk/news')
HLC4 = getC4Headline('https://www.channel4.com/news/')
print('SKY News: ' + HLSky, '\n' + 'BBC News: ' + HLBBC, '\n' + 'Channel 4 News: ' + HLC4)

