"""Client CLI
Usage:
    client
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event list
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event <event-id> info
    client [--ip=<ip>] [--port=<port>] customer <customer-id> ticket list [--order-date=<date>] [--event-date=<date>]
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event <event-id> ticket purchase --quantity=<number>
    client [--ip=<ip>] [--port=<port>] customer <customer-id> budget --year=<number>
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
    --year=<number>                     The year from which to request the budget (e.g. 2020).
    --address=<address>                 The customer address (e.g. "Friedrich-Ebert-Straße 30 78054 Villingen-Schwenningen").
    -h, --help                          Show this screen.
    -v, --version                       Show version.
"""

from docopt import docopt
from app.classes.arguments import Arguments
from app.api.events_api import EventsApi
from app.api.customers_api import CustomersApi
from app.utils.validate_args import Validate_Args

def main(args):
    if args.customer:
        if args.get_budget:
            CustomersApi.get_budget(args)
        elif args.ticket:
            if args.list:
                CustomersApi.get_tickets(args)
        elif args.event:
            if args.list:
                EventsApi.get_events(args)
            elif args.info:
                EventsApi.get_event(args)
            elif args.ticket:
                if args.purchase:
                    EventsApi.purchase_tickets(args)
    elif args.admin:
        if args.customer:
            CustomersApi.add_customer(args)
        elif args.event:
            if args.add:
                EventsApi.add_event(args)
            elif args.list:
                EventsApi.get_events(args)
            elif args.info:
                EventsApi.get_event(args)
            elif args.sales:
                EventsApi.get_sales(args)

if __name__ == '__main__':
    args = docopt(__doc__, version='1.0.0')
    try:
        Validate_Args.validate_args(args)
        main(Arguments(args))
    except Exception as ex:
        exit(ex)
