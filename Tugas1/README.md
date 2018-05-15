<h1 align="center">
  <br>
  Data Scraping
  <br>
  <br>
</h2>

This program scrapes from wikipedia [List of National Parks of Indonesia](https://en.wikipedia.org/wiki/List_of_national_parks_of_Indonesia). These National Parks is from all of Indonesia and it also save about the special flora and fauna.

## Specification
The program will fetch each national park's and it's flora and fauna and preprocess it into JSON object. And the program will do the normalization job to the existing JSON file and build a normalized dataframe.

## Requirements
1. Python 3.6
2. BeautifulSoup4, to fetch the source code of the webpage. You can install it if you have pip
    ```
    $ pip install beautifulsoup4
    ```
3. Pandas, to normalize JSON object into dataframe
    ```
    $ pip install pandas
    ```
4. Internet connection to access the page

## How to Use
1. Go to `Tugas1` directory
2. Execute Makefile with command bellow. This command will execute program with default settings: scrape 1 page for each city.
    ```
    $ make
    ```
3. Your scrapping result will be saved to folder `data` which contains JSON object and its normalized form.

## Screenshots
Execute Program:

![alt text](https://github.com/AlifArifin/Seleksi-2018/blob/master/Tugas1/screenshots/kode1.png "Scraping on 1st stage")

Scraping Process:

![alt text](https://github.com/AlifArifin/Seleksi-2018/blob/master/Tugas1/screenshots/progress.png "Scraping on process")

## JSON Structure
```
{
    "area": "250 km2 (97 sq mi)",
    "coordinates": {
        "latitude": "7\u00b050\u2032S",
        "longitude": "114\u00b022\u2032E"
    },
    "established": "1980",
    "fauna": [
        {
            "binomial-name": "Bos javanicus",
            "image": "//upload.wikimedia.org/wikipedia/commons/thumb/0/02/Bos_javanicus_javanicus.jpg/220px-Bos_javanicus_javanicus.jpg",
            "kingdom": "Animalia",
            "name": "Banteng",
            "status": "Endangered",
            "url": "https://en.wikipedia.org/wiki/Banteng"
        },
        .
        .
        {
            "image": "//upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Panthera_tigris_sondaica_01.jpg/220px-Panthera_tigris_sondaica_01.jpg",
            "kingdom": "Animalia",
            "name": "Javan tiger",
            "status": "Extinct",
            "trinomial-name": "Panthera tigris sondaica",
            "url": "https://en.wikipedia.org/wiki/Javan_tiger"
        }
    ],
    "flora": [
        {
            "binomial-name": "Ziziphus mauritiana",
            "image": "//upload.wikimedia.org/wikipedia/commons/thumb/3/32/Ziziphus_mauritiana_fruit_2.jpg/220px-Ziziphus_mauritiana_fruit_2.jpg",
            "kingdom": "Plantae",
            "name": "Ziziphus mauritiana",
            "url": "https://en.wikipedia.org/wiki/Ziziphus_mauritiana"
        },
        .
        .
        {
            "binomial-name": "Tamarindus indica",
            "image": "//upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Tamarindus_indica_pods.JPG/220px-Tamarindus_indica_pods.JPG",
            "kingdom": "Plantae",
            "name": "Tamarind",
            "url": "https://en.wikipedia.org/wiki/Tamarindus_indica"
        }
    ],
    "governing-body": "Ministry of Environment and Forestry",
    "image": "//upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Golden_hour_at_bekol_savannah.jpg/284px-Golden_hour_at_bekol_savannah.jpg",
    "location": "Situbondo Regency, East Java, Indonesia",
    "name": "Baluran National Park",
    "nearest-city": "Situbondo",
    "visitors": "10,192 (in 2007)",
    "website": "balurannationalpark.web.id"
}
```

## References
1. [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [Urllib](https://docs.python.org/3/library/urllib.html)
3. [Pandas](https://github.com/pandas-dev/pandas)

## Author
<h4 align="center">
  <br>
    Muhammad Alif Arifin - 13516078
  <br>
</h4>