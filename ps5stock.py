import random, requests, sys, time
from bs4 import BeautifulSoup
from datetime import datetime

class stockStatus:

    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]

    STORES = {
    'BESTBUY1': ['https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149',
                '.add-to-cart-button', 
                'Add to Cart',
                'Sony - PlayStation 5 Console'],

    'BESTBUY2': ['https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161',
                '.add-to-cart-button',
                'Add to Cart',
                'Sony - PlayStation 5 Digital Edition Console'],

    'BESTBUY3': ['https://www.bestbuy.com/site/combo/ps5-consoles/96be4c49-d98e-47c6-9a68-291c646d0e47',
                '.add-to-cart-button', 
                'Add to Cart',
                "Package - Sony - PlayStation 5 Console and Marvel's Spider-Man: Miles Morales Standard Launch Edition"],

    'BESTBUY4': ['https://www.bestbuy.com/site/combo/ps5-consoles/8f146095-0a5f-4993-b123-711a1d34745b',
                '.add-to-cart-button', 
                'Add to Cart',
                'Package - Sony - PlayStation 5 Console and PlayStation 5 - DualSense Wireless Controller'],

    'BESTBUY5': ['https://www.bestbuy.com/site/sony-ex14ap-wired-earbud-headphones-blue/5739307.p?skuId=5739307',
                '.add-to-cart-button', 
                'Add to Cart',
                'Cyberpunk 2077 Standard Edition - PlayStation 4, PlayStation 5'],
    }

    def getCarrier(self, url, selection):
        user_agent = random.choice(self.user_agent_list)
        headers = {
          'authority': 'www.bestbuy.com',
          'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
          'sec-ch-ua-mobile': '?0',
          'user-agent': f'{user_agent}',
          'content-type': 'text/plain;charset=UTF-8',
          'accept': '*/*',
          'origin': 'https://www.bestbuy.com',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'cors',
          'sec-fetch-dest': 'empty',
          'referer': 'https://www.bestbuy.com',
          'accept-language': 'en-US,en;q=0.9',
        }
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup.select(selection)

    def runCheck(self, interval):     
        for key in self.STORES:
            myResult = self.getCarrier(self.STORES[key][0],self.STORES[key][1])
            if self.STORES[key][2] in str(myResult):
                sys.stdout.write("\033[0;32m")
                print(f'[{datetime.now()}] :: {key}: {self.STORES[key][3]}')
            else:
                sys.stdout.write("\033[1;31m")
                print(f'[{datetime.now()}] :: {key}: {self.STORES[key][3]}')
            time.sleep(interval)
        self.runCheck(interval)

stockStatus().runCheck(5)
