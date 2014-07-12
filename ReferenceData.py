from datetime import datetime

class ReferenceData:

    def __init__(self, key, value, start_date, end_date):
        self.key = key
        self.value = value
        self.data_list = []
        self.start_date = datetime.strptime(start_date, "%m/%d/%Y")
        self.end_date = datetime.strptime(end_date, "%m/%d/%Y")

    def insert_data_list_values(self, data_value):
        self.data_list.append(data_value)
