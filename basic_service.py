from util import get_day_of_week, convert_timestamp_to_datetime, convert_time_zone, \
                    strptime_timestamp

# get low agg after 
def get_low_after_entry_agg(aggs, entry_datetime):
    smallest_price = 9999999999
    return_time  = 0
    processing_format = "%Y-%m-%d %H:%M:%S%z"
    output_time_format = "%H:%M:%S%"
    for agg in aggs:
        low_price_of_agg = agg.low
        date_to_process = str(convert_time_zone(convert_timestamp_to_datetime(agg.timestamp / 1000), 'US/Eastern'))
        date_to_process = strptime_timestamp(str(date_to_process), processing_format)
    
        # from open to close time respect to EST
        if low_price_of_agg < smallest_price and entry_datetime.hour < date_to_process.hour and entry_datetime.minute < date_to_process.minute:
            smallest_price = low_price_of_agg

            return_time = strptime(date_to_process, output_time_format)
    if smallest_price == 9999999999:
        return -1, -1
    return smallest_price, str(return_time)

# if miss values at any time then setting default values
# def set_missing_values_after_premarket(after_premarket_volumes):
#     processing_format = "%Y-%m-%d %H:%M:%S%z"
#     return_volumes_after_premarket = []

#     defatul_at_931 = [-1, -1]
#     defatul_at_933 = [-1, -1]
#     defatul_at_935 = [-1, -1]
#     defatul_at_940 = [-1, -1]
#     defatul_at_10 = [-1, -1]
#     defatul_at_1030 = [-1, -1]
#     defatul_at_12 = [-1, -1]
#     defatul_at_14 = [-1, -1]

#     for premarket_agg in after_premarket_volumes:
#         date_to_process = str(convert_time_zone(convert_timestamp_to_datetime(premarket_agg[1] / 1000), 'US/Eastern'))
#         date_to_process = strptime_timestamp(str(date_to_process), processing_format)

#         if date_to_process.hour == 9 and date_to_process.minute == 31:
#             flag_at_931 = True
#         if date_to_process.hour == 9 and date_to_process.minute == 31:
#             flag_at_931 = True
#         if date_to_process.hour == 9 and date_to_process.minute == 31:
#             flag_at_931 = True
#         if date_to_process.hour == 9 and date_to_process.minute == 31:
#             flag_at_931 = True
#         if date_to_process.hour == 9 and date_to_process.minute == 31:
#             flag_at_931 = True
#         if date_to_process.hour == 9 and date_to_process.minute == 31:
#             flag_at_931 = True
#         if date_to_process.hour == 9 and date_to_process.minute == 31:
#             flag_at_931 = True
#         if date_to_process.hour == 9 and date_to_process.minute == 31:
#             flag_at_931 = True
            
#     return

def get_volumes_after_premarket(aggs):
    # preMarket_time = daily_agg.from
    processing_format = "%Y-%m-%d %H:%M:%S%z"
    return_volumes_after_premarket = []
    premarket_at_931 = [-1, -1]
    premarket_at_933 = [-1, -1]
    premarket_at_935 = [-1, -1]
    premarket_at_940 = [-1, -1]
    premarket_at_10 = [-1, -1]
    premarket_at_1030 = [-1, -1]
    premarket_at_12 = [-1, -1]
    premarket_at_14 = [-1, -1]
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
        # print (date_to_process.hour, date_to_process.minute)
        if date_to_process.hour == 9 and date_to_process.minute == 31:
            premarket_at_931 = [agg.volume, str(date_to_process)]
        if date_to_process.hour == 9 and date_to_process.minute == 33:
            premarket_at_933 = [agg.volume, str(date_to_process)]            
        if date_to_process.hour == 9 and date_to_process.minute == 35:
            premarket_at_935 = [agg.volume, str(date_to_process)]            
        if date_to_process.hour == 9 and date_to_process.minute == 40:
            premarket_at_940 = [agg.volume, str(date_to_process)]            
        if date_to_process.hour == 10 and date_to_process.minute == 0:
            premarket_at_10 = [agg.volume, str(date_to_process)]            
        if date_to_process.hour == 10 and date_to_process.minute == 30:
            premarket_at_1030 = [agg.volume, str(date_to_process)]            
        if date_to_process.hour == 12 and date_to_process.minute == 0:
            premarket_at_12 = [agg.volume, str(date_to_process)]            
        if date_to_process.hour == 14 and date_to_process.minute == 0:
            premarket_at_14 = [agg.volume, str(date_to_process)]            
            
    return_volumes_after_premarket = [premarket_at_931, premarket_at_933, premarket_at_935, premarket_at_940,\
                                        premarket_at_10, premarket_at_1030, premarket_at_12, premarket_at_14]
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
    output_time_format = "%H:%M:%S%"
    time_to_process = -1
    for agg in aggs:
        high_of_agg_string = str(agg.high)
        if high_of_day_string == high_of_agg_string:
            time_to_process = str(convert_time_zone(convert_timestamp_to_datetime(agg.timestamp / 1000), 'US/Eastern'))
            time_to_process = strptime_timestamp(str(time_to_process), output_time_format)
            
            return time_to_process
    return time_to_process

def get_low_time(aggs, daily_agg):
    high_of_day_string = str(get_low_of_day(daily_agg))
    output_time_format = "%H:%M:%S%"
    time_to_process = -1
    for agg in aggs:
        high_of_agg_string = str(agg.low)
        if high_of_day_string == high_of_agg_string:
            time_to_process = str(convert_time_zone(convert_timestamp_to_datetime(agg.timestamp / 1000), 'US/Eastern'))
            time_to_process = strptime_timestamp(str(time_to_process), output_time_format)
            
            return time_to_process
    return time_to_process

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
