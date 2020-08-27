from datetime import datetime

class DateHelper():
    
    @staticmethod
    def date_to_timestamp(date):
        """Converts date format `dd.mm.yyyy` to timestamp."""
        input_date = datetime.strptime(date, '%d.%m.%Y')
        timestamp = input_date.timestamp()
        return timestamp

    @staticmethod    
    def timestamp_to_date(timestamp):
        """Converts timestamp to date format `dd.mm.yyyy`."""
        date = datetime.fromtimestamp(timestamp)
        return date.strftime('%d.%m.%Y')
