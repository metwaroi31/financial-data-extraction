from polygon import RESTClient
import datetime
from util import get_day_of_week

def get_low_after_entry_agg(aggs, entry_timestamp):
    smallest_price = 9999999999
    return_timestamp  = 0
    for agg in aggs:
        timestamp_of_agg = agg.timestamp
        low_price_of_agg = agg.low
        # from open to close time respect to EST
        if low_price_of_agg < smallest_price and entry_timestamp < agg.timestamp:
            smallest_price = low_price_of_agg
            return_timestamp = timestamp_of_agg
    return smallest_price, return_timestamp

def get_volumes_after_premarket(aggs, daily_agg):
    # preMarket_time = daily_agg.from
    after_1_mins = [aggs[1].volume, aggs[1].timestamp]
    after_3_mins = [aggs[3].volume, aggs[3].timestamp]
    after_5_mins = [aggs[5].volume, aggs[5].timestamp]
    after_10_mins = [aggs[10].volume, aggs[10].timestamp]
    after_30_mins = [aggs[30].volume, aggs[30].timestamp]
    after_60_mins = [aggs[60].volume, aggs[60].timestamp]
    after_150_mins = [aggs[150].volume, aggs[150].timestamp]
    after_270_mins = [aggs[270].volume, aggs[270].timestamp]
    
    return_volumes_after_premarket = [after_1_mins, after_3_mins, after_5_mins, after_10_mins, \
                                        after_30_mins, after_60_mins, after_150_mins, after_270_mins]
    return return_volumes_after_premarket

def get_open_price(daily_agg):
    return daily_agg.open

def get_close_price(daily_agg):
    return daily_agg.close

def get_high_of_day(daily_agg):
    return daily_agg.high

def get_low_of_day(daily_agg):
    return daily_agg.low

def get_high_time(aggs, daily_agg):
    high_of_day_string = str(get_high_of_day(daily_agg))
    return_timestamp = -1
    for agg in aggs:
        high_of_agg_string = str(agg.high)
        if high_of_day_string == high_of_agg_string:
            return_timestamp = agg.timestamp 
            return return_timestamp
    return return_timestamp

def get_low_time(aggs, daily_agg):
    high_of_day_string = str(get_low_of_day(daily_agg))
    return_timestamp = -1
    for agg in aggs:
        high_of_agg_string = str(agg.low)
        if high_of_day_string == high_of_agg_string:
            return_timestamp = agg.timestamp 
            return return_timestamp
    return return_timestamp

def get_premarket_volume(daily_agg):
    # preMarket = 
    return daily_agg.pre_market

def get_volume_of_day(daily_agg):
    return daily_agg.volume

def get_previous_close_high(previous_close_agg):
    return previous_close_agg.high

def get_previous_close_low(previous_close_agg):
    return previous_close_agg.low

def get_previous_close_volume(previous_close_agg):
    return previous_close_agg.volume

# def get_low_time_after_entry():
#     return

# def 