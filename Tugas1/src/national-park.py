from scrapper import *

if __name__ == '__main__':
    # test case url
    url = 'https://en.wikipedia.org/wiki/Baluran_National_Park'

    # test case
    isPark, page = isNationalPark(url)

    if isPark :
        data = scrapeNationalPark(url, page)
        print (json.dumps(data, indent=4, sort_keys=True))

        with open('data/datant.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

        # normalized structure
        df = pandas.io.json.json_normalize(data)
        out = df.to_json(orient='records')
        print (out)

        with open('data/datant.txt', 'w') as outfile:
            outfile.write(df.to_string().encode('ascii','replace').decode("UTF-8"))