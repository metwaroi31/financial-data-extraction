from datetime import datetime, timedelta
import pandas as pd

def convert_datetime_to_timestamp(datetime_string, input_format):
      return datetime.strptime(datetime_string, input_format).timestamp()

def convert_timestamp_to_datetime(timestamp):
      return datetime.fromtimestamp(timestamp)

def add_time(timestamp, days=0, hours=0, minutes=0, seconds=0):
      datetime_object = convert_timestamp_to_datetime(timestamp)
      time_change = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
      new_time = datetime_object + time_change
      return new_time

def write_file_csv(data, file_path):
      df = pd.DataFrame(data)
      df = df.to_csv(file_path, sep = ';')
      return df

def read_file_csv(file_path):
      df = pd.read_csv(file_path, sep = ';')
      return df

def get_day_of_week(datetime_input):
      return datetime_input.weekday()
