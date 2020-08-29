from schema import Schema, And, Or, Use, SchemaWrongKeyError, SchemaError, Regex
from app.utils.date import DateHelper


class Validate_Args():
    @staticmethod
    def validate_args(args):
        """Validate the input parameters."""
        schema = Schema({
            '--ip': And(str, Regex(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'), error="Invalid input for `--ip`. Please enter a valid IP address. Example: `127.0.0.1`."),
            '--port': And(Use(int), lambda x: 1024 <= x <= 65535, error="Invalid input for `--port`. Please enter a number between 1024 and 65535."),
            '--date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$')), error="Invalid input for `--date`. Please enter a valid date. Example: `01.01.2020`."),
            '--order-date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$')), error="Invalid input for `--order-date`. Please enter a valid date. Example: `01.01.2020`."),
            '--event-date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$')), error="Invalid input for `--event-date`. Please enter a valid date. Example: `01.01.2020`."),
            '--quantity': Or(None, And(Use(int)), error="Invalid input for `--quantity`. Please enter an integer number. Example: `3`."),
            '--name': Or(None, And(Use(str))),
            '--location': Or(None, And(str, Regex(r'^([^0-9]+) ([0-9]+.*?), ([0-9]{5}) (.*)$')), error="Invalid input for `--location`. Please enter a valid address. Example: `Friedrich Ebert Straße 30, 78054 Villingen-Schwenningen`."),
            '--address': Or(None, And(str, Regex(r'^([^0-9]+) ([0-9]+.*?), ([0-9]{5}) (.*)$')), error="Invalid input for `--address`. Please enter a valid address. Example: `Friedrich Ebert Straße 30, 78054 Villingen-Schwenningen`."),
            '--ticket-price': Or(None, And(Use(str), Regex(r'^\s*(?=.*[1-9])\d*(?:\.\d{1,2})?\s*$')), error="Invalid input for `--ticket-price`. Please enter a valid amount of money. Example: `5.60`."),
            '--max-tickets': Or(None, And(Use(int)), error="Invalid input for `--max-tickets`. Please enter an integer number. Example: `3`."),
            '--max-tickets-per-customer': Or(None, And(Use(int)), error="Invalid input for `--max-tickets-per-customer`. Please enter an integer number. Example: `3`."),
            '--sale-start-date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$')), error="Invalid input for `--sale-start-date`. Please enter a valid date. Example: `01.01.2020`."),
            '--sale-period': Or(None, And(Use(int)), error="Invalid input for `--sale-period`. Please enter the number of days as an integer number. Example: `3`."),
            '--budget': Or(None, And(Use(str), Regex(r'^\s*(?=.*[1-9])\d*(?:\.\d{1,2})?\s*$')), error="Invalid input for `--budget`. Please enter a valid amount of money. Example: `5.60`."),
            '<event-id>': Or(None, And(Use(int)), error="Invalid input for `<event-id>`. The event ID can only be an integer number. Example: `3`."),
            '<customer-id>': Or(None, And(Use(int)), error="Invalid input for `<customer-id>`. The customer ID can only be an integer number. Example: `3`."),
            '--year': Or(None, And(Use(int)), error="Invalid input for `--year`. Please enter an integer number. Example: `2020`.")
        })
        if args.get('--date') is not None and args.get('--sale-start-date') is not None:
            event_date = DateHelper.date_to_timestamp(args.get('--date'))
            sale_start_date = DateHelper.date_to_timestamp(
                args.get('--sale-start-date'))
            if sale_start_date > event_date:
                raise SchemaError(
                    None, errors="Invalid input for `--date` or `--sale-start-date`. The event date cannot be earlier than the start date of the sale. Please check your input.")
        try:
            schema.validate(args)
        except SchemaWrongKeyError as ex:
            pass
        except SchemaError as ex:
            exit(ex)
