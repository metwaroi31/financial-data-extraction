# from polygon import RESTClient
from util import convert_datetime_to_timestamp, convert_timestamp_to_datetime, \
                    read_file_csv, write_file_csv, get_day_of_week, add_time, convert_time_zone, \
                        strptime_timestamp
from polygon_client import get_aggs_stock, get_daily_open_close, get_previous_close_agg
from basic_service import get_low_after_entry_agg, get_open_price, get_close_price, \
                        get_volumes_after_premarket, get_high_of_day, get_low_of_day, \
                            get_high_time, get_low_time, get_premarket_value, get_volume_of_day, \
                                get_previous_close_high, get_previous_close_low, get_previous_close_volume, \
                                    get_weekday_string, get_premarket_volume, get_low_after_premarket

from resistance_service import get_highest_resitance_agg, get_recent_resitance_agg, get_highest_resitance_params, \
                            get_combined_resitance


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
    "day_of_the_week" : [],
    "highest_resistance_date" : [],
    "highest_resistance_price_open" : [],
    "highest_resistance_high_of_day" : [],
    "highest_resistance_low_of_day" : [],
    "highest_resistance_price_close" : [],
    "highest_resistance_volume" : [],
    "highest_resistance_vwap" : [],
    "recent_resistance_date" : [],
    "recent_resistance_price_open" : [],
    "recent_resistance_high_of_day" : [],
    "recent_resistance_low_of_day" : [],
    "recent_resistance_price_close" : [],
    "recent_resistance_volume" : [],
    "recent_resistance_vwap" : [],
    # "highest_date_resistance_date" : [],
    "combined_resistance_volume" : [],
    "resistance_count" : [],
    "highest_price_open_resistance" : [],
    "highest_high_of_day_resistance" : [],
    "highest_low_of_day_resistance" : [],
    "highest_price_close_resistance" : [],
    "highest_volume_resistance" : [],
    "highest_vwap_resistance" : []
    # "highest_resistance_vwap" : [],
    # "highest_resistance_date" : [],
    # "highest_resistance_date" : [],

}
for index, row in data.iterrows():
    datetime_input = row[0]
    ticker_input = row[1]
    entry_input = row[2]
    
    # timestamp processing
    # format datetime to process input
    input_format = "%H:%M:%S %m/%d/%Y"
    input_datetime = strptime_timestamp(datetime_input, input_format)
    timestamp = convert_datetime_to_timestamp(datetime_input, input_format)
    date_to_process = convert_timestamp_to_datetime(timestamp)
    date = str(date_to_process).split(' ')[0]
    # one year timestamp for resistance
    datetime_one_year = add_time(timestamp, days=-365)
    datetime_one_year = str(datetime_one_year).split(' ')[0]
    # exclude the day from input
    datetime_yesterday = add_time(timestamp, days=-1)
    datetime_yesterday = str(datetime_yesterday).split(' ')[0]
    params = {
        "ticker" : ticker_input,
        "multiplier" : 1,
        "timespan" : "minute",
        "from_time" : date,
        "to_time" : date
    }
    params_one_year = {
        "ticker" : ticker_input,
        "multiplier" : 1,
        "timespan" : "day",
        "from_time" : datetime_one_year,
        "to_time" : datetime_yesterday
    }
    params_daily = {
        "ticker" : ticker_input,
        "date" : date
    }
    params_previous = {
        "ticker" : ticker_input
    }
    # calling polygon API
    aggs = get_aggs_stock(**params)
    one_year_aggs = get_aggs_stock(**params_one_year)
    daily_agg = get_daily_open_close(**params_daily)
    previous_close_agg = get_previous_close_agg(**params_previous)
    output_df['datetime'].append(datetime_input)
    output_df['ticker'].append(ticker_input)
    output_df['entry'].append(entry_input)
    # for agg in aggs :
    #     print (str(convert_time_zone(convert_timestamp_to_datetime(agg.timestamp / 1000), 'US/Eastern'))) 

    # Basic service
    entry_agg = get_low_after_entry_agg(aggs, input_datetime)
    open_price = get_open_price(daily_agg)
    close_price = get_close_price(daily_agg)
    previous_close_high = get_previous_close_high(previous_close_agg[0])
    previous_close_low = get_previous_close_low(previous_close_agg[0])
    previous_close_volume = get_previous_close_volume(previous_close_agg[0])
    high_of_day = get_high_of_day(daily_agg)
    low_of_day = get_low_of_day(daily_agg)
    volume_of_day = get_volume_of_day(daily_agg)
    high_time = get_high_time(aggs, daily_agg)
    low_time = get_low_time(aggs, daily_agg)
    after_premarket_volumes = get_volumes_after_premarket(aggs)
    premarket_volume = get_premarket_value(daily_agg)
    day_of_week = get_day_of_week(date_to_process)
    day_of_week = get_weekday_string(day_of_week)
    premarket_volume = get_premarket_volume(aggs)

    # resistance
    date_format = "%m/%d/%Y"
    highest_resistance_agg = get_highest_resitance_agg(one_year_aggs)
    if highest_resistance_agg:
        highest_resistance_date = convert_time_zone((convert_timestamp_to_datetime(highest_resistance_agg.timestamp / 1000)), 'US/Eastern')
        highest_resistance_date = strptime(highest_resistance_date, date_format)
        highest_resistance_high_of_day = highest_resistance_agg.high
        highest_resistance_low_of_day = highest_resistance_agg.low
        highest_resistance_open_of_day = highest_resistance_agg.open
        highest_resistance_close_of_day = highest_resistance_agg.close
        highest_resistance_volume_of_day = highest_resistance_agg.volume
        highest_resistance_vwap_of_day = highest_resistance_agg.vwap
        recent_resistance_agg = get_recent_resitance_agg(one_year_aggs)
    else :
        highest_resistance_date = -1
        highest_resistance_high_of_day = -1
        highest_resistance_low_of_day = -1
        highest_resistance_open_of_day = -1
        highest_resistance_close_of_day = -1
        highest_resistance_volume_of_day = -1
        highest_resistance_vwap_of_day = -1
        recent_resistance_agg = -1

    if recent_resistance_agg:
        recent_resistance_date = convert_time_zone((convert_timestamp_to_datetime(recent_resistance_agg.timestamp / 1000)), 'US/Eastern')
        recent_resistance_date = strptime(recent_resistance_date, date_format)
        recent_resistance_high_of_day = recent_resistance_agg.high
        recent_resistance_low_of_day = recent_resistance_agg.low
        recent_resistance_open_of_day = recent_resistance_agg.open
        recent_resistance_close_of_day = recent_resistance_agg.close
        recent_resistance_volume_of_day = recent_resistance_agg.volume
        recent_resistance_vwap_of_day = recent_resistance_agg.vwap
    else :
        recent_resistance_date = -1
        recent_resistance_high_of_day = -1
        recent_resistance_low_of_day = -1
        recent_resistance_open_of_day = -1
        recent_resistance_close_of_day = -1
        recent_resistance_volume_of_day = -1
        recent_resistance_vwap_of_day = -1
    max_volume_resistance, max_high_resistance, max_low_resistance, max_open_resistance, max_close_resistance, max_vwap_resistance = get_highest_resitance_params(one_year_aggs)
    resitance_count, resitance_volume_sum = get_combined_resitance(one_year_aggs)
    premarket_low_after_high = get_low_after_premarket(aggs)

    output_df['low_after_entry'].append(entry_agg[0])
    output_df['low_time_after_entry'].append(entry_agg[1])
    output_df['open_price'].append(open_price)
    output_df['close_price'].append(close_price)
    output_df['previous_close_high'].append(previous_close_high)
    output_df['previous_close_low'].append(previous_close_low)
    output_df['previous_close_volume'].append(previous_close_volume)
    output_df['high_of_day'].append(high_of_day)
    output_df['low_of_day'].append(low_of_day)
    output_df['high_time'].append(low_of_day)
    output_df['low_time'].append(low_of_day)
    output_df['volume_of_day'].append(volume_of_day)
    # Missing output
    output_df['premarket_volume'].append(premarket_volume)
    output_df['premarket_high'].append(premarket_volume)

    output_df['premarket_low_after_high'].append(premarket_low_after_high)
    output_df['volume_at_931'].append(after_premarket_volumes[0][0])
    output_df['volume_at_933'].append(after_premarket_volumes[1][0])
    output_df['volume_at_935'].append(after_premarket_volumes[2][0])
    output_df['volume_at_940'].append(after_premarket_volumes[3][0])
    output_df['volume_at_1000'].append(after_premarket_volumes[4][0])
    output_df['volume_at_1030'].append(after_premarket_volumes[5][0])
    output_df['volume_at_1200'].append(after_premarket_volumes[6][0])
    output_df['volume_at_1400'].append(after_premarket_volumes[7][0])
    output_df['highest_resistance_date'].append(highest_resistance_date)
    output_df['highest_resistance_price_open'].append(highest_resistance_open_of_day)
    output_df['highest_resistance_price_close'].append(highest_resistance_close_of_day)
    output_df['highest_resistance_high_of_day'].append(highest_resistance_high_of_day)
    output_df['highest_resistance_low_of_day'].append(highest_resistance_low_of_day)
    output_df['highest_resistance_volume'].append(highest_resistance_volume_of_day)
    output_df['highest_resistance_vwap'].append(highest_resistance_vwap_of_day)
    # Wrong output
    # if resitance_count != 0:
    output_df['recent_resistance_date'].append(recent_resistance_date)
    output_df['recent_resistance_price_open'].append(recent_resistance_open_of_day)
    output_df['recent_resistance_price_close'].append(recent_resistance_close_of_day)
    output_df['recent_resistance_high_of_day'].append(recent_resistance_high_of_day)
    output_df['recent_resistance_low_of_day'].append(recent_resistance_low_of_day)
    output_df['recent_resistance_volume'].append(recent_resistance_volume_of_day)
    output_df['recent_resistance_vwap'].append(recent_resistance_vwap_of_day)
    output_df['combined_resistance_volume'].append(resitance_volume_sum)
    output_df['resistance_count'].append(resitance_count)
    output_df['highest_price_open_resistance'].append(max_open_resistance)
    output_df['highest_low_of_day_resistance'].append(max_low_resistance)
    output_df['highest_high_of_day_resistance'].append(max_high_resistance)
    output_df['highest_price_close_resistance'].append(max_close_resistance)
    output_df['highest_volume_resistance'].append(max_volume_resistance)
    output_df['highest_vwap_resistance'].append(max_vwap_resistance)
    output_df['day_of_the_week'].append(day_of_week)

print (output_df)
write_file_csv(output_df, './output.csv')
