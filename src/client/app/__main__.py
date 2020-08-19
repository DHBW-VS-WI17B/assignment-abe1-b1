"""Client CLI
Usage:
    client
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event list
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event info
    client [--ip=<ip>] [--port=<port>] customer <customer-id> ticket list [--order-date=<date>] [--event-date=<date>]
    client [--ip=<ip>] [--port=<port>] customer <customer-id> ticket purchase [--quantity=<number>]
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
    --location=<location>               The event location (e.g. "Staatsoper Stuttgart").
    --ticket-price=<number>             The ticket price in € (e.g. 5).
    --max-tickets=<number>              The maximum number of tickets (e.g. 100).
    --max-tickets-per-customer=<number> The maximum number of tickets per customer (e.g. 3).
    --sale-start-date=<date>            The sale start date (e.g. 01.01.2020).
    --sale-period=<number>              The sale period in days (e.g. 5).
    -h, --help                          Show this screen.
    -v, --version                       Show version.
"""

from docopt import docopt


def main(args):
    print('TODO')
    print(args)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0')
    main(arguments)
