# from util import convert_timestamp_to_datetime
from util import convert_datetime_to_timestamp, convert_timestamp_to_datetime, \
                    read_file_csv, write_file_csv, get_day_of_week, add_time, strptime_timestamp, convert_time_zone
from polygon_client import get_aggs_stock, get_daily_open_close, get_previous_close_agg
from basic_service import get_low_after_entry_agg, get_open_price, get_close_price, \
                        get_volumes_after_premarket, get_high_of_day, get_low_of_day, \
                            get_high_time, get_low_time, get_premarket_volume, get_volume_of_day, \
                                get_previous_close_high, get_previous_close_low, get_previous_close_volume, get_weekday_string

from resistance_service import get_highest_resitance_agg, get_recent_resitance_agg, get_highest_resitance_params, \
                            get_combined_resitance
# print (convert_timestamp_to_datetime(1651737600))
params = {
    "ticker" : "DPSI",
    "multiplier" : 1,
    "timespan" : "minute",
    "from_time" : "2022-05-18",
    "to_time" : "2022-05-19"
}

print (convert_time_zone(convert_timestamp_to_datetime(1652860800), 'US/Eastern'))
print (convert_time_zone(convert_timestamp_to_datetime(1652864400), 'US/Eastern'))

# print (convert_timestamp_to_datetime(1651737780000))
# print (convert_timestamp_to_datetime(1651737660000))
# print (convert_timestamp_to_datetime(1651737660000))
# print (convert_timestamp_to_datetime(1651737660000))
# print (convert_timestamp_to_datetime(1651737660000))
# print (convert_timestamp_to_datetime(1651737660000))
aggs = get_aggs_stock(**params)
# print (aggs[0])
input_format = "%Y-%m-%d %H:%M:%S%z"

for agg in aggs:
    print (agg)
    date_to_process = str(convert_time_zone(convert_timestamp_to_datetime(agg.timestamp / 1000), 'US/Eastern'))
    print (date_to_process)
    # # date_to_process = convert_timestamp_to_datetime(agg.timestamp/1000)
    # date_to_process = strptime_timestamp(str(date_to_process), input_format)
    # print (date_to_process.hour, date_to_process.minute, date_to_process.second)
    # print (convert_timestamp_to_datetime(agg.timestamp/1000))