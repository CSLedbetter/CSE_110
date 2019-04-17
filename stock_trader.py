
def trade_action(current_stock, purchase_price, current_price, investment):
    
    if purchase_price > current_price and investment > 10:
       bought_stock = buy_stocks (current_price, investment)
       if (bought_stock * current_price) == 10 :
           return "Hold Shares"
       elif (bought_stock * purchase_price) <= 11 :
           return "Hold Shares"
       else:
           bought_stock = str(bought_stock)
           return ("Buy " + bought_stock + " shares")
    
    elif purchase_price < current_price and investment >= 10 :
        sold_stock = sell_stock(current_price, investment)
        if (sold_stock * current_price) < 10 :
            return "Hold Shares"
        else:
            sold_stock = str(sold_stock)
            return ("Sell " + sold_stock + " shares")
    
    elif purchase_price < current_price and investment == 0 :
        potential_profit = sell_no_invest(current_stock, current_price)
        if (potential_profit * current_price - 10) < 11 :
            return "Hold Shares"
        elif (potential_profit * purchase_price) <= 11 :
            return "Hold Shares"
        elif (current_stock * purchase_price) == potential_profit - 10 :
            return "Hold Shares"
        else:
            sold_stock = str(current_stock)
            return ("Sell " + sold_stock + " shares")

    else:
        return "Hold Shares"
    
def buy_stocks (current_price, investment) :
    bought_stocks = round((investment - 10) / current_price) 
    return bought_stocks

def sell_stock (current_price, investment) :
    sold_stock = round((investment - 10) * current_price)
    return sold_stock

def sell_no_invest (current_stock, current_price) :
    potential_profit = round(current_stock * current_price)
    return potential_profit
``