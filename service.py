from polygon import RESTClient
import datetime

def get_low_after_entry_agg(aggs, entry_timestamp):
    smallest_price = 9999999999
    return_timestamp  = 0
    for agg in aggs:
        timestamp_of_agg = agg.timestamp
        low_price_of_agg = agg.low
        # from open to close time respect to EST
        if low_price_of_agg < smallest_price and entry_timestamp > agg.timestamp:
            smallest_price = low_price_of_agg
            return_timestamp = timestamp_of_agg
    return smallest_price, return_timestamp

def get_open_price(daily_agg):
    return daily_agg.open

def get_close_price(daily_agg):
    return daily_agg.close


# def get_low_time_after_entry():
#     return

# def 