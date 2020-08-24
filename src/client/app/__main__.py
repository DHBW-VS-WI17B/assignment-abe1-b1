"""Client CLI
Usage:
    client
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event list
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event <event-id> info
    client [--ip=<ip>] [--port=<port>] customer <customer-id> ticket list [--order-date=<date>] [--event-date=<date>]
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event <event-id> ticket purchase [--quantity=<number>]
    client [--ip=<ip>] [--port=<port>] customer <customer-id> budget
    client [--ip=<ip>] [--port=<port>] admin event list
    client [--ip=<ip>] [--port=<port>] admin event add --name=<name> --date=<date> --location=<location> --ticket-price=<number> --max-tickets=<number> --max-tickets-per-customer=<number> --sale-start-date=<date> --sale-period=<days>
    client [--ip=<ip>] [--port=<port>] admin event <event-id> info
    client [--ip=<ip>] [--port=<port>] admin event sales
    client [--ip=<ip>] [--port=<port>] admin customer add --name=<name> --budget=<budget> --address=<address>
    client -h|--help
    client -v|--version

Options:
    --ip=<ip>                           IP address of the server [default: 127.0.0.1].
    --port=<port>                       Port of the server [default: 8080].
    --order-date=<date>                 The order date of the ticket (e.g. 01.01.2020).
    --event-date=<date>                 The event date (e.g. 01.01.2020).
    --quantity=<number>                 The number of tickets.
    --name=<name>                       The name of the customer or event.
    --date=<date>                       The event date (e.g. 01.01.2020).
    --location=<location>               The event location (e.g. "Friedrich-Ebert-Straße 30 78054 Villingen-Schwenningen").
    --ticket-price=<number>             The ticket price in € (e.g. 5).
    --max-tickets=<number>              The maximum number of tickets (e.g. 100).
    --max-tickets-per-customer=<number> The maximum number of tickets per customer (e.g. 3).
    --sale-start-date=<date>            The sale start date (e.g. 01.01.2020).
    --sale-period=<number>              The sale period in days (e.g. 5).
    --budget=<budget>                   The customer budget in € (e.g. 100).
    --address=<address>                 The customer address (e.g. "Friedrich-Ebert-Straße 30 78054 Villingen-Schwenningen").
    -h, --help                          Show this screen.
    -v, --version                       Show version.
"""

from docopt import docopt
from app.classes.arguments import Arguments
from app.api.events import Events
from app.api.customers import Customers
from schema import Schema, And, Or, Use, SchemaError, Regex
from datetime import datetime

def main(args):
    if args.customer:
        if args.get_budget:
            Customers.get_budget(args)
        if args.ticket:
            if args.list:
                Customers.get_tickets(args)
                exit
        if args.event:
            if args.list:
                Events.get_events(args)
                exit
            if args.info:
                Events.get_event(args)
                exit
            if args.ticket:
                if args.purchase:
                    Events.purchase_tickets(args)
                    exit
    if args.admin:
        if args.customer:
            Customers.add_customer(args)
            exit
        if args.event:
            if args.add:
                Events.add_event(args)
                exit
            if args.list:
                Events.get_events(args)
                exit
            if args.info:
                Events.get_event(args)
                exit
            if args.sales:
                Events.get_sales(args)
                exit
            


if __name__ == '__main__':
    args = docopt(__doc__, version='1.0.0')
    schema = Schema({
        '--ip': And(str, Regex(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')),
        #'--port': And(And(Or(int, str), lambda x: x == 4)),
        '--date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$'))),
        '--order-date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$'))),
        '--event-date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$'))),
        '--quantity': Or(None, And(Use(int))),
        '--name': Or(None, And(str, Regex(r'^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$'))),
        '--location': Or(None, And(str, Regex(r'^([^0-9]+) ([0-9]+.*?) ([0-9]{5}) (.*)$'))),
        '--address': Or(None, And(str, Regex(r'^([^0-9]+) ([0-9]+.*?) ([0-9]{5}) (.*)$'))),
        '--ticket-price': Or(None, And(Use(int))),
        '--max-tickets': Or(None, And(Use(int))),
        '--max-tickets-per-customer': Or(None, And(Use(int))),
        '--sale-start-date': Or(None, And(str, Regex(r'^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$'))),
        '--sale-period': Or(None, And(Use(int))),
        '--budget': Or(None, And(Use(int))),
        })
    try:
        args = schema.validate(args)
    except SchemaError as e:
        exit(e)
    main(Arguments(args))
