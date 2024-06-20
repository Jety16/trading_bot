from datetime import datetime, timezone
import os

class Stock():

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.last_update = datetime.now(timezone.utc)
        self.user = os.environ.get("TRADE_BOT_USER")
        self.password = os.environ.get("TRADE_BOT_PASS")
        self.to_buy = False
        self.to_sell = False

    def _get_data():
        pass

    def update():
        pass

