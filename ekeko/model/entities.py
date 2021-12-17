from sqlalchemy import Column, Integer, Sequence, ForeignKey, Text, REAL

from ..database import connector

class Trader(connector.Manager.Base):
    __tablename__ = 'trader'

    id       = Column(Integer, Sequence('trader_id'), primary_key = True)
    username = Column(Text)
    password = Column(Text)

class Market(connector.Manager.Base):
    __tablename__ = 'market'

    stock    = Column(Text, primary_key = True)
    currency = Column(Text, primary_key = True)

class BuySellOrder(connector.Manager.Base):
    __tablename__ = 'buy_sell_order'

    id          = Column(Integer, Sequence('order_id'), primary_key = True)
    trader_id   = Column(Integer, ForeignKey('trader.id'))
    buy_or_sell = Column(Integer)
    stock       = Column(Text, ForeignKey('market.stock'))
    currency    = Column(Text, ForeignKey('market.currency'))
    price       = Column(REAL)
    amount      = Column(REAL)

    def to_json_dict(self):
        return {
            "id"          : self.id ,
            "trader_id"   : self.trader_id ,
            "buy_or_sell" : self.buy_or_sell ,
            "stock"       : self.stock ,
            "currency"    : self.currency ,
            "price"       : self.price ,
            "amount"      : self.amount ,
        }
