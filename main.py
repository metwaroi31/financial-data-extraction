from polygon import RESTClient
from util import convert_datetime_to_timestamp, convert_timestamp_to_datetime, \
                    read_file_csv, write_file_csv, get_day_of_week
from polygon_client import get_aggs_stock, get_daily_open_close, get_previous_close_agg
from service import get_low_after_entry_agg, get_open_price, get_close_price, \
                        get_volumes_after_premarket, get_high_of_day, get_low_of_day, \
                            get_high_time, get_low_time, get_premarket_volume, get_volume_of_day, \
                                get_previous_close_high, get_previous_close_low, get_previous_close_volume

data = read_file_csv("./input.csv")
output_df = {
    "datetime" : [],
    "ticker" : [],
    "entry" : [],
    "low_after_entry" : [],
    "low_time_after_entry" : [],
    "previous_close_high" : [],
    "previous_close_low" : [],
    "previous_close_volume" : [],
    "open_price" : [],
    "high_of_day" : [],
    "low_of_day" : [],
    "close_price" : [],
    "volume_of_day" : [],
    "high_time" : [],
    "low_time" : [],
    "premarket_volume" : [],
    "premarket_high" : [],
    "premarket_low_after_high" : [],
    "volume_at_931" : [],
    "volume_at_933" : [],
    "volume_at_935" : [],
    "volume_at_940" : [],
    "volume_at_1000" : [],
    "volume_at_1030" : [],
    "volume_at_1200" : [],
    "volume_at_1400" : [],
    "day_of_the_week" : []
}
for index, row in data.iterrows():
    datetime_input = row[0]
    ticker_input = row[1]

    # entry_input
    input_format = "%H:%M:%S %m/%d/%Y"
    timestamp = convert_datetime_to_timestamp(datetime_input, input_format)
    date = convert_timestamp_to_datetime(timestamp)
    date = str(date).split(' ')[0]
    params = {
        "ticker" : ticker_input,
        "multiplier" : 1,
        "timespan" : "minute",
        "from_time" : date,
        "to_time" : date
    }
    params_daily = {
        "ticker" : ticker_input,
        "date" : date
    }
    params_previous = {
        "ticker" : ticker_input
    }
    aggs = get_aggs_stock(**params)
    daily_agg = get_daily_open_close(**params_daily)
    previous_close_agg = get_previous_close_agg(**params_previous)
    output_df['datetime'].append(datetime_input)
    output_df['ticker'].append(ticker_input)
    output_df['entry'].append(entry_input)
    
    entry_agg = get_low_after_entry_agg(aggs, timestamp)
    open_price = get_open_price(daily_agg)
    close_price = get_close_price(daily_agg)
    previous_close_high = get_previous_close_high(previous_close_agg)
    previous_close_low = get_previous_close_low(previous_close_agg)
    previous_close_volume = get_previous_close_volume(previous_close_agg)
    high_of_day = get_high_of_day(daily_agg)
    low_of_day = get_low_of_day(daily_agg)
    after_premarket_volumes = get_volumes_after_premarket(aggs, daily_agg)
    premarket_volume = get_premarket_volume(daily_agg)
    # day_of_week

    output_df['low_after_entry'].append(entry_agg[0])
    output_df['low_time_after_entry'].append(entry_agg[1])
    output_df['open_price'].append(open_price)
    output_df['close_price'].append(close_price)
    output_df['previous_close_high'].append(previous_close_high)
    output_df['previous_close_low'].append(previous_close_low)
    output_df['previous_close_volume'].append(previous_close_volume)
    output_df['high_of_day'].append(high_of_day)
    output_df['close_price'].append(low_of_day)
    # output_df['premarket_volume'].append(premarket_volume)
    output_df['premarket_high'].append(premarket_volume)

    output_df['premarket_low_after_high'].append(after_premarket_volumes[0])
    output_df['volume_at_931'].append(after_premarket_volumes[1])
    output_df['volume_at_933'].append(after_premarket_volumes[2])
    output_df['volume_at_935'].append(after_premarket_volumes[3])
    output_df['volume_at_940'].append(after_premarket_volumes[4])
    output_df['volume_at_1000'].append(after_premarket_volumes[5])
    output_df['volume_at_1030'].append(after_premarket_volumes[6])
    output_df['volume_at_1200'].append(after_premarket_volumes[7])
    output_df['volume_at_1400'].append(after_premarket_volumes[8])
    # output_df['day_of_the_week'].append(get_close_price(daily_agg))

write_file_csv(output_df, './output.csv')
params = {
    "ticker" : "AAPL",
    "multiplier" : 1,
    "timespan" : "minute",
    "from_time" : "2022-05-05",
    "to_time" : "2022-05-05"
}
aggs = get_aggs_stock(**params)
print (aggs[0])
#for agg in aggs:
#    print (convert_timestamp_to_datetime(agg.timestamp/1000))
# print (aggs)
# print (get_low_after_entry_agg(aggs, ))
params_daily = {
    "ticker" : "AAPL",
    "date" : "2022-05-05"
}
daily_agg = get_daily_open_close(**params_daily)
params_previous = {
    "ticker" : "AAPL"
}
previous_close_agg = get_previous_close_agg(**params_previous)
print (previous_close_agg)
print (get_open_price(daily_agg))
print (get_close_price(daily_agg))
