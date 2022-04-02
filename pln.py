import requests
from datetime import datetime

class plnFX:
    def __init__(self):
        self.url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR'

    def get_year(self, year):
        today       = datetime.now()
        start_year  = datetime(int(year), 1, 1)
        end_year    = datetime(int(year), 12, 31)
        end_year    = today if end_year > today else end_year
        url = f'{self.url}/{start_year.date()}/{end_year.date()}/'
        response = requests.get(url)       
        if not response.status_code == 200:
            print('Error could not retrieve from API, response status code: {response.status_code}')
            return []
        else:
            data = response.json()
            data = data.get('rates', [])
            data = [{'date' :x['effectiveDate'], 'rate': x['mid']} for x in data]
            return data
        
    def get_date(self, date):
        date = datetime.strptime(date, "%Y-%m-%d")
        data = self.get_year(date.year)
        for x in data: 
            if x['date'] == str(date.date()): 
                return x; break
        return None
       
if __name__ == '__main__':
    fx = plnFX()
    
    year_rate = fx.get_year('2022')
    print('\n year_rate: ', year_rate)
    
    day_rate = fx.get_date('2022-01-03')
    print('\n day_rate: ', day_rate)
