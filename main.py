from polygon import RESTClient
from util import convert_datetime_to_timestamp, convert_timestamp_to_datetime
from polygon_client import get_aggs_stock, get_daily_open_close
from service import get_low_after_entry_agg, get_open_price, get_close_price

params = {
    "ticker" : "AAPL",
    "multiplier" : 1,
    "timespan" : "minute",
    "from_time" : "2022-05-05",
    "to_time" : "2022-05-06"
}
aggs = get_aggs_stock(**params)
print (get_low_after_entry_agg(aggs, ))
params_daily = {
    "ticker" : "AAPL",
    "date" : "2022-05-05"
}
daily_agg = get_daily_open_close(**params_daily)
print (get_open_price(daily_agg))
print (get_close_price(daily_agg))
