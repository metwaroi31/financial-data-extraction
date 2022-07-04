from util import get_day_of_week, convert_timestamp_to_datetime, convert_time_zone, \
                    strptime_timestamp

# get low agg after 
def get_low_after_entry_agg(aggs, entry_datetime):
    smallest_price = 9999999999
    return_datetime  = 0
    processing_format = "%Y-%m-%d %H:%M:%S%z"
    
    for agg in aggs:
        low_price_of_agg = agg.low
        date_to_process = str(convert_time_zone(convert_timestamp_to_datetime(agg.timestamp / 1000), 'US/Eastern'))
        date_to_process = strptime_timestamp(str(date_to_process), processing_format)
    
        # from open to close time respect to EST
        if low_price_of_agg < smallest_price and entry_datetime.hour < date_to_process.hour and entry_datetime.minute < date_to_process.minute:
            smallest_price = low_price_of_agg
            return_datetime = date_to_process
    return smallest_price, return_datetime

# if miss values at any time then setting default values
def set_missing_values_after_premarket(after_premarket_volumes):
    processing_format = "%Y-%m-%d %H:%M:%S%z"
    return_volumes_after_premarket = []
    flag_at_931 = False
    flag_at_933 = False
    flag_at_935 = False
    flag_at_940 = False
    flag_at_10 = False
    flag_at_1030 = False
    flag_at_12 = False
    flag_at_14 = False
    for premarket_agg in after_premarket_volumes:
        date_to_process = str(convert_time_zone(convert_timestamp_to_datetime(premarket_agg[1] / 1000), 'US/Eastern'))
        date_to_process = strptime_timestamp(str(date_to_process), processing_format)
        print (date_to_process.hour, date_to_process.minute)


    return

def get_volumes_after_premarket(aggs):
    # preMarket_time = daily_agg.from
    processing_format = "%Y-%m-%d %H:%M:%S%z"
    return_volumes_after_premarket = []
    # return_volumes_after_premarket[0] is after_1_mins
    # return_volumes_after_premarket[1] is after_3_mins
    # return_volumes_after_premarket[2] is after_5_mins
    # return_volumes_after_premarket[3] is after_10_mins
    # return_volumes_after_premarket[4] is after_30_mins
    # return_volumes_after_premarket[5] is after_60_mins
    # return_volumes_after_premarket[6] is after_150_mins
    # return_volumes_after_premarket[7] is after_270_mins

    for agg in aggs:
        # get_time
        # compare hours and minutes
        date_to_process = str(convert_time_zone(convert_timestamp_to_datetime(agg.timestamp / 1000), 'US/Eastern'))
        date_to_process = strptime_timestamp(str(date_to_process), processing_format)
        print (date_to_process.hour, date_to_process.minute)
        if date_to_process.hour == 9 and date_to_process.minute == 31:
            return_volumes_after_premarket.append([agg.volume, agg.timestamp])
        if date_to_process.hour == 9 and date_to_process.minute == 33:
            return_volumes_after_premarket.append([agg.volume, agg.timestamp])
        if date_to_process.hour == 9 and date_to_process.minute == 35:
            return_volumes_after_premarket.append([agg.volume, agg.timestamp])
        if date_to_process.hour == 9 and date_to_process.minute == 40:
            return_volumes_after_premarket.append([agg.volume, agg.timestamp])
        if date_to_process.hour == 10 and date_to_process.minute == 0:
            return_volumes_after_premarket.append([agg.volume, agg.timestamp])
        if date_to_process.hour == 10 and date_to_process.minute == 30:
            return_volumes_after_premarket.append([agg.volume, agg.timestamp])
        if date_to_process.hour == 12 and date_to_process.minute == 0:
            return_volumes_after_premarket.append([agg.volume, agg.timestamp])
        if date_to_process.hour == 14 and date_to_process.minute == 0:
            return_volumes_after_premarket.append([agg.volume, agg.timestamp])
        
    # after_3_mins = [aggs[3].volume, aggs[3].timestamp]
    # after_5_mins = [aggs[5].volume, aggs[5].timestamp]
    # after_10_mins = [aggs[10].volume, aggs[10].timestamp]
    # after_30_mins = [aggs[30].volume, aggs[30].timestamp]
    # after_60_mins = [aggs[60].volume, aggs[60].timestamp]
    # after_150_mins = [aggs[150].volume, aggs[150].timestamp]
    # after_270_mins = [aggs[270].volume, aggs[270].timestamp]
    
    # return_volumes_after_premarket = [after_1_mins, after_3_mins, after_5_mins, after_10_mins, \
    #                                     after_30_mins, after_60_mins, after_150_mins, after_270_mins]
    print (return_volumes_after_premarket)
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

def get_premarket_volume(aggs):
    processing_format = "%Y-%m-%d %H:%M:%S%z"
    for agg in aggs:
        date_to_process = str(convert_time_zone(convert_timestamp_to_datetime(agg.timestamp / 1000), 'US/Eastern'))
        date_to_process = strptime_timestamp(str(date_to_process), processing_format)
        if date_to_process.hour > 5 and date_to_process.hour < 9:
            return agg.volume
    return -1

def get_premarket_value(daily_agg):
    # preMarket = 
    # premarket volume at get volume > 5
    return daily_agg.pre_market

def get_volume_of_day(daily_agg):
    return daily_agg.volume

def get_previous_close_high(previous_close_agg):
    return previous_close_agg.high

def get_previous_close_low(previous_close_agg):
    return previous_close_agg.low

def get_previous_close_volume(previous_close_agg):
    return previous_close_agg.volume

def get_weekday_string(weekday):
    switcher = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return switcher.get(weekday, "null")

def get_low_after_premarket(aggs):
    smallest_price = 9999999999
    processing_format = "%Y-%m-%d %H:%M:%S%z"
    
    for agg in aggs:
        low_price_of_agg = agg.low
        date_to_process = str(convert_time_zone(convert_timestamp_to_datetime(agg.timestamp / 1000), 'US/Eastern'))
        date_to_process = strptime_timestamp(str(date_to_process), processing_format)
    
        if low_price_of_agg < smallest_price and date_to_process.hour < 9 and date_to_process.minute < 30:
            smallest_price = low_price_of_agg
    return smallest_price
