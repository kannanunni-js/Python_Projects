import requests
import json
response = requests.get('https://corona.lmao.ninja/v2/countries?')
countries = json.loads(response.text)
values=[]


with open("data.txt","w") as book:
    book.write("{},{},{},{},{},{}".format("Name","Updated",'Cases','Deaths','Recovered','Critical'))
    book.write('\n')
    for country in countries:
        book.write("{},{},{},{},{},{}".format(country['country'],country['updated'],
                                        country['cases'],country['deaths'],country['recovered'],country['critical']))
        book.write('\n')


