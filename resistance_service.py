# from util

# Agg(open=162.25, high=162.34, low=156.72, close=156.8, volume=95595226.0, vwap=158.6074, timestamp=1650945600000,
# highest resistance date requirements ()
def get_highest_resitance_agg(one_year_aggs):
    max_price = -1
    return_agg  = one_year_aggs[0]
    for agg in one_year_aggs:
        volume = agg.volume
        if volume > 5000000:
            if max_price < agg.high:
                max_price = agg.high
                return_agg = agg
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
    for agg in one_year_aggs:
        volume = agg.volume
        if volume > 5000000:
            return_agg = agg
    return return_agg

# def get_resitance_date(aggs):
#     return

# def get_resitance_date(aggs):
#     return

# def get_resitance_date(aggs):
#     return
