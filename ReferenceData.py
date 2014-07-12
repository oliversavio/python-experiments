from datetime import datetime, date

class ReferenceData:

    def __init__(self, key, value, start_date="01/01/0001", end_date="12/31/9999"):
        self.key = key
        self.value = value
        self.data_list = []
        self.start_date = datetime.strptime(start_date, "%m/%d/%Y")
        self.end_date = datetime.strptime(end_date, "%m/%d/%Y")

    def insert_data_list_value(self, data_value):
        self.data_list.append(data_value)

    def is_active(self):
        today = datetime.today()
        return today > self.start_date and today < self.end_date
