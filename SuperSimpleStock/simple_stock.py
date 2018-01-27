import operator
import time

stocks_details = {
    "TEA": {
        "type": "common",
        "last_divident": 0,
        "fixed_divident": 0,
        "par_value": 100
    },
    "POP": {
        "type": "common",
        "last_divident": 8,
        "fixed_divident": 0,
        "par_value": 100
    },
    "ALE": {
        "type": "common",
        "last_divident": 23,
        "fixed_divident": 0,
        "par_value": 60
    },
    "GIN": {
        "type": "preferred",
        "last_divident": 8,
        "fixed_divident": 0.02,
        "par_value": 100
    },
    "JOE": {
        "type": "common",
        "last_divident": 13,
        "fixed_divident": 0,
        "par_value": 250
    }
}

"""
This variable holds our Last transactions in Memory.
Format is: 
{	
    12345678: {
        "timestamp": 12345678,
        "quantity": 0,
        "transaction_type": buy,
        "price": 12200
    }
}
"""
last_trades = {}


class SimpleStock:

    def __init__(self, stock_type, quantity, market_price, transaction_type):
        """
        Constructor
        :param stock_type:  str
        :param quantity: int
        :param market_price: float
        :param transaction_type: str
        """

        self.stock_type = stock_type
        self.stock_details = stocks_details[stock_type]
        self.quantity = quantity
        self.market_price = market_price
        self.transaction_type = transaction_type

        curr_timestamp = time.time()
        last_trades[int(curr_timestamp)] = {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(curr_timestamp)),
            "quantity": self.quantity,
            "transaction_type": self.transaction_type,
            "price": self.market_price
        }

    def calculate_divident_yield(self):
        """
        This calculates the divident yield with formula based on stock type (common/preferred)
        :param self:
        :return: float
        """

        if self.stock_details["type"] == "preferred":
            divident = operator.mul(self.stock_details["par_value"], self.stock_details["fixed_divident"])
        else:
            divident = self.stock_details["last_divident"]

        try:
            return operator.div(divident, self.market_price)
        except ZeroDivisionError:
            return 0

    def calculate_pe_ratio(self):
        """
        Calculates PE ratio for the stock provided in input
        :return: float
        """
        try:
            return operator.div(self.market_price, self.stock_details["last_divident"])
        except ZeroDivisionError:
            return 0

    @staticmethod
    def check_previous_stocks():
        """
        This functions loops through our trades stored in memory and returns volumn weighted stock price and
        all share index
        :return: dict
        """
        timestamp_15 = time.time() - 900
        sum_trade_quantity = 0
        sum_quantity = 0
        price_sum = 1

        for i in last_trades:
            price_sum *= last_trades[i]["price"]
            if i >= timestamp_15:
                sum_trade_quantity += operator.mul(last_trades[i]["quantity"], last_trades[i]["price"])
                sum_quantity += last_trades[i]["quantity"]

        try:
            return {
                "weighted_stock_price": round(operator.div(sum_trade_quantity, sum_quantity), 2),
                "all_share_index": price_sum**(1/float(len(last_trades)))
            }
        except ZeroDivisionError:
            return {
                "weighted_stock_price": 0,
                "all_share_index": 0
            }


def validate_params(params):
    """

    :param params: list containing 4 indices
    0: stock type (ale/gin/pop etc.)
    1: quantity
    2: market price
    3: trade type (buy/sell)
    :return: Status (bool), Message (str)
    """
    status = True
    msg = []

    if len(params) < 4:
        return False, "Not enough input params to work with!"

    if params[0].upper() not in stocks_details:
        status = False
        msg.append("Stock is not a valid Input!")

    if not params[1].isdigit() or params[1] <= 0:
        status = False
        msg.append("Quantity should be a number greater than 0!")

    if not params[2].isdigit() or params[2] <= 0:
        status = False
        msg.append("Market Price should be a number greater than 0!")

    if params[3] != "buy" and params[3] != "sell":
        status = False
        msg.append("Transaction Type should be either buy or sell!")

    return status, " ---- ".join(msg)
