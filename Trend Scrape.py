import requests
import bs4
import json
import time
from datetime import datetime, timedelta



if __name__ == "__main__":

    s = requests.Session()

    # set header
    s.headers.update({'user-agent':'Mozilla/5.0'})

    # connect to the main page to collect any cookies that we might need
    s.get('https://trends.google.com', timeout=1)

    # sleep for about 3 seconds to seem more human like
    time.sleep(3)

    # then go straight to the link for past 24 hr search trends for the search term "stock"

    s.get('https://trends.google.com/trends/explore?date=now%201-d&geo=US&q=stock', timeout=1)

    # sleep for about 3 seconds to seem more human like
    time.sleep(3)

    # we'll have to conect to this url to get a token to make json requests

    siteData = s.get('https://trends.google.com/trends/api/explore?hl=en-US&tz=300&req=%7B%22comparisonItem%22:%5B%7B%22\
          keyword%22:%22stock%22,%22geo%22:%22US%22,%22time%22:%22now+1-d%22%7D%5D,%22category%22:0,%22property%22:%22%22%7D&tz=300', timeout=1)

    soup = bs4.BeautifulSoup(siteData.text, 'html.parser')

    # extract our api key from the returned json file

    # the first few characters do not line up with a typical json file and throw the next line of code off
    # so we slice those characters off and keep going

    newDict = json.loads(soup.text[5:])

    newDict = newDict['examples'][0]

    newDict = newDict['widget']

    apiToken = newDict['token']

    # url time is in Coordinated Universal Time (UTC)

    todayUTC = datetime.utcnow() - timedelta(days=1)
    yesterdayUTC = todayUTC - timedelta(days=1)
    tomorrowUTC = todayUTC + timedelta(days=1)

    todayUTCFormatted = todayUTC.strftime("%Y-%m-%dT03\\\\:%H\\\\:%M")
    yesterdayUTCFormatted = yesterdayUTC.strftime("%Y-%m-%dT03\\\\:%H\\\\:%M")
    tomorrowUTCFormatted = tomorrowUTC.strftime("%Y-%m-%dT03\\\\:%H\\\\:%M")

    

    relatedJsonUrl = 'https://trends.google.com/trends/api/widgetdata/relatedsearches?hl=en-US&tz=300\
&req={"restriction":{"geo":{"country":"US"},"time":"' + todayUTCFormatted + ' ' + tomorrowUTCFormatted + '",\
"originalTimeRangeForExploreUrl":"now 1-d","complexKeywordsRestriction":{"keyword":[{"type":"BROAD",\
"value":"stock"}]}},"keywordType":"QUERY","metric":["TOP","RISING"],"trendinessSettings":{"compareTime":\
"' + yesterdayUTCFormatted + ' ' + todayUTCFormatted + '"},"requestOptions":{"property":"","backend":"CM","category":0},\
"language":"en","userCountryCode":"US"}&token=' + apiToken


    #print(relatedJsonUrl)

    time.sleep(3)

    print(s.cookies)

    jsonData = s.get(relatedJsonUrl, timeout=1)

    soup = bs4.BeautifulSoup(jsonData.text, 'html.parser')

    print(soup)

