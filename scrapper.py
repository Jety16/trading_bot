import requests
import os

class Scrapper():
    def __init__(self):
        self.user = os.environ.get("TRADE_BOT_USER")
        self.password = os.environ.get("TRADE_BOT_PASS")

    def _get_finger_print(self):
        # Use bs4
        # <input data-val="true" data-val-required="El campo FingerPrint es obligatorio." id="FingerPrint" name="FingerPrint" type="hidden" value="7dfb58c1a532edb710368b2cdc4ee1dc">

        pass

    def _get_request_verification_token(self):
        # <input name="__RequestVerificationToken" type="hidden" value="CfDJ8P5Kwit1nzZLuv1V7wRPTMVTexPxVhPM-UhSb47N4MwWWubmv7fK89fBlfC7_7Xg1YAa3b7SLTWBh968tkpBNi18WthrlY4miayMuxngide2kVceYDGTd3XsSQFBtNJceSrGsTfg-25rEXWcZOYDEPM">
        pass

    def _login(self, client):
        # First we get the login page
        client.get('https://bullmarketbrokers.com/Security/SignIn')

        # Security n shi. idk if this is necessary tho
        params = {
            'v': 'vE7LRPTNv9YQqGtTwk2Ye5Ljr4nZrydKpFBj30t1MvY',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': '*/*',
            'Accept-Language': 'es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'keep-alive',
            'Referer': 'https://bullmarketbrokers.com/Security/SignIn',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        client.get('https://bullmarketbrokers.com/bundles/js/jquery.min.js',
            headers=headers,
            params=params)

        # This will make the login.
        data = {
            'FingerPrint': self._get_finger_print(),
            'Email': self.user,
            'Password': self.password,
            '__RequestVerificationToken': self._get_request_verification_token(),
        }

        response = client.post('https://bullmarketbrokers.com/Security/SignIn', data=data)


    def run(self):
        client = requests.session()


Scrapper.run()