from polygon import RESTClient
from util import convert_datetime_to_timestamp, convert_timestamp_to_datetime, read_file_csv, write_file_csv
from polygon_client import get_aggs_stock, get_daily_open_close
from service import get_low_after_entry_agg, get_open_price, get_close_price

data = read_file_csv("./input.csv")
# print (data.head())
output_df = {
    "datetime" : [],
    "ticker" : [],
    "low_after_entry" : [],
    "low_time_after_entry" : [],
    "open_price" : [],
    "close_price" : []
    # "high_of_day" : [],
    # "low_of_day" : []
}
for index, row in data.iterrows():
    datetime_input = row[0]
    ticker_input = row[1]
    # entry_input
    input_format = "%H:%M:%S %m/%d/%Y"
    timestamp = convert_datetime_to_timestamp(datetime_input, input_format)
    date = convert_timestamp_to_datetime(timestamp)
    date = str(date).split(' ')[0]
    print (date)
    params = {
        "ticker" : ticker_input,
        "multiplier" : 1,
        "timespan" : "minute",
        "from_time" : date,
        "to_time" : "2022-08-06"
    }
    params_daily = {
        "ticker" : ticker_input,
        "date" : date
    }
    aggs = get_aggs_stock(**params)
    print (aggs)
    daily_agg = get_daily_open_close(**params_daily)
    output_df['datetime'].append(datetime_input)
    output_df['ticker'].append(ticker_input)
    output_df['entry']
    output_df['low_after_entry'].append(get_low_after_entry_agg(aggs, timestamp)[0])
    output_df['low_time_after_entry'].append(get_low_after_entry_agg(aggs, timestamp)[1])
    output_df['open_price'].append(get_open_price(daily_agg))
    output_df['close_price'].append(get_close_price(daily_agg))
    # output_df['low_after_entry'].append(get_low_after_entry_agg(aggs, timestamp))
write_file_csv(output_df, './output.csv')
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
