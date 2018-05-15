from scrapper import *

if __name__ == '__main__':
    # the real main program
    url = "https://en.wikipedia.org/wiki/List_of_national_parks_of_Indonesia"

    data = bigPicture(url)

    with open('data/data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

    # normalized structure
    df = pandas.io.json.json_normalize(data)
    out = df.to_json(orient='records')
    print (out)

    with open('data/data.txt', 'w') as outfile:
        outfile.write(df.to_string().encode('ascii','replace').decode("UTF-8"))