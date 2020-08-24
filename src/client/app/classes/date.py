from datetime import datetime

class DateHelper():
    
    @staticmethod
    def date_to_timestamp(date):
        input_date = datetime.strptime(date, '%d.%m.%Y')
        timestamp = input_date.timestamp()
        return timestamp

    @staticmethod    
    def timestamp_to_date(timestamp):
        date = datetime.fromtimestamp(timestamp)
        return date.strftime('%d-%m-%y')
        