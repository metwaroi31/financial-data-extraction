# from util

# Agg(open=162.25, high=162.34, low=156.72, close=156.8, volume=95595226.0, vwap=158.6074, timestamp=1650945600000,
# highest resistance date requirements ()
def get_highest_resitance_agg(one_year_aggs):
    max_price = -1
    return_agg  = one_year_aggs[0]
    flag_found = False
    for agg in one_year_aggs:
        volume = agg.volume
        if volume > 5000000:
            if max_price < agg.high:
                max_price = agg.high
                return_agg = agg
    if flag_found == False:
        return False
    return return_agg

# # Price open at Resistance Date
# def get_resitance_price_open(aggs):

#     return

# # high_of_day at Resistance Date
# def get_resitance_high_of_day(aggs):
#     return

# # low_of_day at Resistance Date
# def get_resitance_low_of_day(aggs):
#     return

# # close_of_day at Resistance Date
# def get_resitance_close_of_day(aggs):
#     return

# # price close at Resistance Date
# def get_resitance_price_close(aggs):
#     return

def get_recent_resitance_agg(one_year_aggs):
    return_agg  = one_year_aggs[0]
    flag_found = False
    for agg in one_year_aggs:
        volume = agg.volume
        if volume > 5000000:
            return_agg = agg
            flag_found = True
    if flag_found == False:
        return False
    return return_agg

# def get_resitance_date(aggs):
#     return

# def get_resitance_date(aggs):
#     return

# def get_resitance_date(aggs):
#     return
# get sum of volumes resitances, count resitances 
def get_combined_resitance(one_year_aggs):
    volume_sum = 0
    resitance = 0
    for agg in one_year_aggs:
        volume = agg.volume
        if volume > 5000000:
            resitance = resitance + 1
            volume_sum = volume_sum + agg.volume
    return volume_sum, resitance

def get_highest_resitance_params(one_year_aggs):
    max_volume = -1
    max_high = -1
    max_low = -1
    max_open = -1
    max_close = -1
    max_vwap = -1

    for agg in one_year_aggs:
        volume = agg.volume
        if volume > 5000000:
            if max_volume < agg.volume:
                max_volume = volume
            if max_high < agg.high:
                max_high = agg.high
            if max_low < agg.low:
                max_low = agg.low
            if max_open < agg.open:
                max_open = agg.open
            if max_close < agg.close:
                max_close = agg.close
            if max_vwap < agg.vwap:
                max_vwap = agg.vwap
    return max_volume, max_high, max_low, max_open, max_close, max_vwap