import xmltodict
from urllib.request import urlopen
from decimal import Decimal
from time import gmtime, strftime

today = strftime("%Y-%m-%d", gmtime())
list =[]
years = ['2018']
for year in years:
    for number in range(1000):
        if len(str(number)) == 1:
            number = '00'+ str(number)
        elif len(str(number)) == 2:
            number = '0'+ str(number)
        else:
            number = str(number)
        print (str(number))
        url = 'https://www.nbp.pl/kursy/xml/en/'+year[2:4]+'a'+str(number)+'en.xml'
        print(url)
        try:
            file = urlopen(url)
            data = xmltodict.parse(file.read())
            data = data['exchange_rates']

            date = data['@date']
            for i in data['mid-rate']:
                if i['@code'] == 'EUR':
                    rate = i['#text']

            print('today: '+str(today))
            print('date: '+str(date))
            print('rate: '+str(rate))
            list.append([date, rate])
            if date == today:
                break
        except:
            continue

print('PLN rates')
for i in list:
    print(i)
