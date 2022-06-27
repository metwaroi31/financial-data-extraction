# from polygon import RESTClient
from util import convert_datetime_to_timestamp, convert_timestamp_to_datetime, \
                    read_file_csv, write_file_csv, get_day_of_week, add_time
from polygon_client import get_aggs_stock, get_daily_open_close, get_previous_close_agg
from basic_service import get_low_after_entry_agg, get_open_price, get_close_price, \
                        get_volumes_after_premarket, get_high_of_day, get_low_of_day, \
                            get_high_time, get_low_time, get_premarket_volume, get_volume_of_day, \
                                get_previous_close_high, get_previous_close_low, get_previous_close_volume, get_weekday_string

from resistance_service import get_highest_resitance_agg


# data = read_file_csv("./input.csv")
# output_df = {
#     "datetime" : [],
#     "ticker" : [],
#     "entry" : [],
#     "low_after_entry" : [],
#     "low_time_after_entry" : [],
#     "previous_close_high" : [],
#     "previous_close_low" : [],
#     "previous_close_volume" : [],
#     "open_price" : [],
#     "high_of_day" : [],
#     "low_of_day" : [],
#     "close_price" : [],
#     "volume_of_day" : [],
#     "high_time" : [],
#     "low_time" : [],
#     # "premarket_volume" : [],
#     "premarket_high" : [],
#     # "premarket_low_after_high" : [],
#     "volume_at_931" : [],
#     "volume_at_933" : [],
#     "volume_at_935" : [],
#     "volume_at_940" : [],
#     "volume_at_1000" : [],
#     "volume_at_1030" : [],
#     "volume_at_1200" : [],
#     "volume_at_1400" : [],
#     "day_of_the_week" : [],
#     "highest_resistance_date" : [],
#     "highest_resistance_price_open" : [],
#     "highest_resistance_high_of_day" : [],
#     "highest_resistance_low_of_day" : [],
#     "highest_resistance_price_close" : [],
#     "highest_resistance_volume" : []
#     # "highest_resistance_vwap" : [],
#     # "highest_resistance_date" : [],
#     # "highest_resistance_date" : [],

# }
# for index, row in data.iterrows():
#     datetime_input = row[0]
#     ticker_input = row[1]
#     entry_input = row[2]
    
#     # timestamp processing
#     input_format = "%H:%M:%S %m/%d/%Y"
#     timestamp = convert_datetime_to_timestamp(datetime_input, input_format)
#     date_to_process = convert_timestamp_to_datetime(timestamp)
#     date = str(date_to_process).split(' ')[0]

#     one_year_timestamp = add_time(timestamp, days=365)
#     datetime_one_year = convert_timestamp_to_datetime(one_year_timestamp)
#     date_to_process_one_year = convert_timestamp_to_datetime(one_year_timestamp)
#     date_one_year = str(date_to_process_one_year).split(' ')[0]

#     params = {
#         "ticker" : ticker_input,
#         "multiplier" : 1,
#         "timespan" : "minute",
#         "from_time" : date,
#         "to_time" : date
#     }
#     params_one_year = {
#         "ticker" : ticker_input,
#         "multiplier" : 1,
#         "timespan" : "day",
#         "from_time" : date,
#         "to_time" : date_one_year
#     }
#     params_daily = {
#         "ticker" : ticker_input,
#         "date" : date
#     }
#     params_previous = {
#         "ticker" : ticker_input
#     }
#     aggs = get_aggs_stock(**params)
#     aggs_one_year = get_aggs_stock(**params_one_year)
#     daily_agg = get_daily_open_close(**params_daily)
#     previous_close_agg = get_previous_close_agg(**params_previous)
#     output_df['datetime'].append(datetime_input)
#     output_df['ticker'].append(ticker_input)
#     output_df['entry'].append(entry_input)
    
#     # Basic service
#     entry_agg = get_low_after_entry_agg(aggs, timestamp)
#     open_price = get_open_price(daily_agg)
#     close_price = get_close_price(daily_agg)
#     previous_close_high = get_previous_close_high(previous_close_agg[0])
#     previous_close_low = get_previous_close_low(previous_close_agg[0])
#     previous_close_volume = get_previous_close_volume(previous_close_agg[0])
#     high_of_day = get_high_of_day(daily_agg)
#     low_of_day = get_low_of_day(daily_agg)
#     volume_of_day = get_volume_of_day(daily_agg)
#     high_time = get_high_time(aggs, daily_agg)
#     low_time = get_low_time(aggs, daily_agg)
#     after_premarket_volumes = get_volumes_after_premarket(aggs, daily_agg)
#     premarket_volume = get_premarket_volume(daily_agg)
#     day_of_week = get_day_of_week(date_to_process)
#     highest_resistance_agg = get_highest_resitance_agg(one_year_aggs)

#     output_df['low_after_entry'].append(entry_agg[0])
#     output_df['low_time_after_entry'].append(entry_agg[1])
#     output_df['open_price'].append(open_price)
#     output_df['close_price'].append(close_price)
#     output_df['previous_close_high'].append(previous_close_high)
#     output_df['previous_close_low'].append(previous_close_low)
#     output_df['previous_close_volume'].append(previous_close_volume)
#     output_df['high_of_day'].append(high_of_day)
#     output_df['low_of_day'].append(low_of_day)
#     output_df['high_time'].append(low_of_day)
#     output_df['low_time'].append(low_of_day)
#     output_df['volume_of_day'].append(volume_of_day)
#     # output_df['premarket_volume'].append(premarket_volume)
#     output_df['premarket_high'].append(premarket_volume)

#     # output_df['premarket_low_after_high'].append(after_premarket_volumes[0])
#     output_df['volume_at_931'].append(after_premarket_volumes[0][0])
#     output_df['volume_at_933'].append(after_premarket_volumes[1][0])
#     output_df['volume_at_935'].append(after_premarket_volumes[2][0])
#     output_df['volume_at_940'].append(after_premarket_volumes[3][0])
#     output_df['volume_at_1000'].append(after_premarket_volumes[4][0])
#     output_df['volume_at_1030'].append(after_premarket_volumes[5][0])
#     output_df['volume_at_1200'].append(after_premarket_volumes[6][0])
#     output_df['volume_at_1400'].append(after_premarket_volumes[7][0])
#     output_df['day_of_the_week'].append(day_of_week)

# write_file_csv(output_df, './output.csv')
# params = {
#     "ticker" : "AAPL",
#     "multiplier" : 1,
#     "timespan" : "minute",
#     "from_time" : "2022-05-05",
#     "to_time" : "2022-05-05"
# }
# aggs = get_aggs_stock(**params)
# print (aggs[0])
#for agg in aggs:
#    print (convert_timestamp_to_datetime(agg.timestamp/1000))
# print (aggs)
# print (get_low_after_entry_agg(aggs, ))
# params_daily = {
#     "ticker" : "AAPL",
#     "date" : "2022-05-05"
# }
# daily_agg = get_daily_open_close(**params_daily)
# params_previous = {
#     "ticker" : "AAPL"
# }

params_one_year = {
        "ticker" : "AAPL",
        "multiplier" : 1,
        "timespan" : "day",
        "from_time" : "2021-05-05",
        "to_time" : "2022-05-05"
}
aggs = get_aggs_stock(**params_one_year)
for agg in aggs:
    print (agg)
# previous_close_agg = get_previous_close_agg(**params_previous)
# print (previous_close_agg)
# print (daily_agg)
# print (get_open_price(daily_agg))
# print (get_close_price(daily_agg))
