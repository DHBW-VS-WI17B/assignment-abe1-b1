from schema import Schema, And, Or, Use, SchemaWrongKeyError, SchemaError, Regex

class Validate_Args():
    @staticmethod
    def validate_args(args):
        """Validate the input parameters."""
        schema = Schema({
            '--ip': And(str, Regex(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'), error='The format of the IP address is wrong, please check the format. (e.g.: 127.0.0.1)'),
            '--port': And(Use(int), lambda x: 1024  <= x <= 65535, error='The port can only be a number between 1024 and 65535.'),
            '--date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$')), error='The format of the date is wrong, please use the following format e.g. 01.01.2020.'),
            '--order-date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$')), error='The format of the date is wrong, please use the following format e.g. 01.01.2020.'),
            '--event-date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$')), error='The format of the date is wrong, please use the following format e.g. 01.01.2020.'),
            '--quantity': Or(None, And(Use(int)), error='The quantity of tickets to be purchased can only be one number.'),
            '--name': Or(None, And(Use(str))),
            '--location': Or(None, And(str, Regex(r'^([^0-9]+) ([0-9]+.*?), ([0-9]{5}) (.*)$')), error='The format of the location is wrong, please use the following format for the entry: Friedrich Ebert Straße 30, 78054 Villingen-Schwenningen'),
            '--address': Or(None, And(str, Regex(r'^([^0-9]+) ([0-9]+.*?), ([0-9]{5}) (.*)$')), error='The format of the address is wrong, please use the following format for the entry: Friedrich Ebert Straße 30, 78054 Villingen-Schwenningen'),
            '--ticket-price': Or(None, And(Use(int)), error='The price of the tickets can only be a number. Please do not use currency symbols.'),
            '--max-tickets': Or(None, And(Use(int)), error='The maximum amount of tickets can only be a number.'),
            '--max-tickets-per-customer': Or(None, And(Use(int)), error='The maximum amount of tickets per customer can only be a number.'),
            '--sale-start-date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$')), error='The format of the date is wrong, please use the following format e.g. 01.01.2020.'),
            '--sale-period': Or(None, And(Use(int)), error='The sales period can only be given in the form of a number corresponding to the number of days.'),
            '--budget': Or(None, And(Use(int)), error='The customer budget can only be a number, please do not use currency symbols.'),
            '<event-id>': Or(None, And(Use(int)), error='The event id can only be a number. Please check your input.'),
            '<customer-id>': Or(None, And(Use(int)), error='The customer id can only be a number. Please check your input.'),
            '--year': Or(None, And(Use(int)))
        })
        try:
            schema.validate(args)
        except SchemaWrongKeyError as ex:
            pass
        except SchemaError as ex:
            exit(ex)
