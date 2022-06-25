from polygon import RESTClient
from config import API_KEY

def get_aggs_stock(ticker, multiplier, timespan, from_time, to_time):
    params = {
        "ticker" : ticker,
        "multiplier" : multiplier,
        "timespan" : timespan,
        "from_" : from_time,
        "to" : to_time
    }    
    client = RESTClient(API_KEY)
    aggs = client.get_aggs(**params)    
    return aggs

def get_daily_open_close(ticker, date, adjusted=False):
    params = {
        "ticker" : ticker,
        "date" : date,
        "adjusted" : adjusted
    }    
    client = RESTClient(API_KEY)
    agg = client.get_daily_open_close_agg(**params)    
    return agg

def get_previous_close_agg(ticker, adjusted=False):
    params = {
        "ticker" : ticker
    }    
    client = RESTClient(API_KEY)
    agg = client.get_previous_close_agg(**params)    
    return agg

# def get_