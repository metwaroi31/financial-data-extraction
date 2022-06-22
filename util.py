from datetime import datetime
import pandas as pd

def convert_datetime_to_timestamp(datetime_string, input_format):
      return datetime.strptime(datetime_string, input_format).timestamp()

def convert_timestamp_to_datetime(timestamp):
      return datetime.fromtimestamp(timestamp)

def write_file_csv(data, file_path):
      df = pd.DataFrame(data)
      df = df.to_csv(file_path, sep = ';')
      return df

def read_file_csv(file_path):
      df = pd.read_csv(file_path, sep = ';')
      return df