from datetime import datetime
# curr_dt = datetime.now()
 
# print("Current datetime: ", curr_dt)
# timestamp = int(round(curr_dt.timestamp()))
 
# print("Integer timestamp of current datetime: ",
      # timestamp)

# input format in 
def convert_datetime_to_timestamp(datetime_string, input_format):
      return datetime.strptime(datetime_string, input_format).timestamp()

def convert_timestamp_to_datetime(timestamp):
      return datetime.fromtimestamp(timestamp)
