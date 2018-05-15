from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import re
import time
import pandas

# to check whether url is a fauna/flora page or not
def isFloraFauna(url) :
    try :
        page = urlopen(url).read()
        soup = BeautifulSoup(page, 'html.parser')

        # every flora and fauna has Kingdom
        found = soup.find("td", text = "Kingdom:")
        
        # every flora and fauna has Species
        found = soup.find("span", {"class" : "species"})

        # found if it success and there is tag with those condition
        if found :
            return (True, page)
        else :
            return (False, page)
    except :
        return (False, None)

# to check whether the page is a national park page or not
def isNationalPark(url) :
    try :
        page = urlopen(url).read()
        soup = BeautifulSoup(page, 'html.parser')

        # every national park page in wikipedia is having a substring "National Park - Wikipedia" in their title
        found = soup.find("title", text = re.compile("^.*National Park - Wikipedia.*$"))

        # found if it success and there is tag with those condition
        if found :
            return (True, page)
        else :
            return (False, page)
    except :
        return (False, None)

# for scrapping flora and fauna
def scrapeFloraFauna(url, page) :
    result = {}

    soup = BeautifulSoup(page, 'html.parser')
    
    # get the name of flora/fauna
    title = soup.find("title").text
    title = title.replace(" - Wikipedia", "")
    result["name"] = title
    
    # get the image of flora/fauna
    image = soup.find("table", {"class" : re.compile("^.*infobox.*$")}).find("a", {"class" : "image"}).find("img")['src']
    result["image"] = image
    
    # get the kingdom of flora/fauna (to distinguish flora/fauna)
    sibling = soup.find("td", text = "Kingdom:")
    kind = sibling.find_next_sibling("td").find("a").text
    result["kingdom"] = kind

    # some flora/fauna has binomial name and other has trinomial name
    try :
        binomial = soup.find("span", {"class" : "binomial"}).find("i").text
        result["binomial-name"] = binomial
    except :
        # do nothing
        pass
    
    try :
        trinomial = soup.find("span", {"class" : "trinomial"}).find("i").text
        result["trinomial-name"] = trinomial
    except :
        # do nothing
        pass

    # some flora/fauna has the status of their existence which is grouped by IUCN Red List
    try :
        status = soup.find("a", {"title" : "IUCN Red List"}).find_parent("small").find_previous_sibling("a").text
        result["status"] = status
    except :
        # do nothing
        pass

    # note the url
    result["url"] = url

    return result

# for scrapping national park
def scrapeNationalPark(url, page) :
    result = {}
    soup = BeautifulSoup(page, 'html.parser')
    
    # get the name of national park
    title = soup.find("title").text
    title = title.replace(" - Wikipedia", "")
    result["name"] = title
    
    # save the infobox html code (infobox is the box which contains the image, location and so on)
    infobox = soup.find("table", {"class" : re.compile("^.*infobox.*$")}).find_all("th")
    
    # get the image of national park
    image = soup.find("table", {"class" : re.compile("^.*infobox.*$")}).find("a", {"class" : "image"}).find("img")['src']
    result["image"] = image
    
    # for every <th> tag in infobox
    for unit in infobox :
        try : 
            sibling = unit.find_next_sibling("td")
            # removing non breaking space and change to the "normal" space
            # make it lower case
            # change space " " to dash "-"
            unitText = unit.text.encode('ascii','replace').decode("UTF-8").replace("?", " ").lower().replace(" ", "-")
            siblingText = sibling.text.encode('ascii', 'replace').decode('UTF-8').replace("?", " ")
            
            # remove info (if there is a foot note)
            siblingText = re.sub(r"\[.*\]", "", siblingText)

            # coordinates has a special case, because it contains longitude and latitude
            if (unitText == "coordinates") :
                result[unitText] = {}
                temp = sibling.find("a", text = "Coordinates").find_next_sibling("span")
                result[unitText]['longitude'] = temp.find("span", {"class" : "longitude"}).text
                result[unitText]['latitude'] = temp.find("span", {"class" : "latitude"}).text
            # the other case
            else : 
                result[unitText] = siblingText
        except :
            #do nothing
            pass
    
    # find all special flora and fauna in national park
    try :
        ffSpan = soup.find("span", {"id" : "Flora_and_fauna"})
        
        # this is to make sure that we find in between two <h2> tag
        ffHeading = ffSpan.find_parent("h2")
        ffSibling = ffHeading.find_next_sibling("h2")
        sibling = ffHeading.find_next_sibling()

        # to gather flora/fauna json
        result['flora'] = []
        result['fauna'] = []
        i = -1
        # while still in between two <h2> tag (with the first tag is <h2> with id = "Flora_and_fauna)
        while (sibling != ffSibling) :
            # get all sibling <a> tag
            listA = sibling.find_all("a")
            for a in listA :
                # add sleep because I don't want to be banned :(
                # time.sleep(1)
                # get the real url
                ffUrl = "https://en.wikipedia.org" + a['href']

                # check if ffUrl is a flora/fauna page
                isKingdom, ffPage = isFloraFauna(ffUrl)
                if isKingdom :
                    print (i)
                    i = i - 1
                    jsonTemp = scrapeFloraFauna(ffUrl, ffPage)
                    # group the flora/fauna based on their kingdom
                    if jsonTemp["kingdom"] == 'Plantae' :
                        result['flora'].append(jsonTemp)
                    else :
                        result['fauna'].append(jsonTemp)
            
            # get the next sibling
            sibling = sibling.find_next_sibling()
    except :
        # do nothing because some of page do not give flora/fauna information
        pass
            
    return result

# big picture scrapper
def bigPicture(url) :
    result = []
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    
    # find all link that has "National Park" in their title
    listPark = soup.find_all("a", {"title" : re.compile("^.*National Park.*$")})
    listUrl = []
    for url in listPark :
        listUrl.append("https://en.wikipedia.org" + url['href'])
    
    listUrl = list(set(listUrl))
    
    # just to iterate because we don't know if it still scrapping or not
    i = 1
    # for every link with that condition
    for url in listUrl :
        # same reason with the other
        # time.sleep(1)
        
        # for my needs
        print(i)
        i = i + 1
        
        # get the real url
        print(url)
        
        # verify whether the page contains national park information
        isPark, page = isNationalPark(url)
        if isPark :
            jsonTemp = scrapeNationalPark(url, page)
            result.append(jsonTemp)
            
        # if (i == 4) :
            # break

    return result