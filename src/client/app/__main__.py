"""Client CLI
Usage:
    client
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event list
    client [--ip=<ip>] [--port=<port>] customer <customer-id> event info
    client [--ip=<ip>] [--port=<port>] customer <customer-id> ticket list [--order-date=<date>] [--event-date=<date>]
    client [--ip=<ip>] [--port=<port>] customer <customer-id> ticket purchase [--quantity=<quantity>]
    client [--ip=<ip>] [--port=<port>] customer <customer-id> budget
    client [--ip=<ip>] [--port=<port>] admin event list
    client [--ip=<ip>] [--port=<port>] admin event add
    client [--ip=<ip>] [--port=<port>] admin event <event-id> info
    client [--ip=<ip>] [--port=<port>] admin event sales
    client -h|--help
    client -v|--version

Options:
    --ip=<ip>               IP address of the server [default: 127.0.0.1].
    --port=<port>           Port of the server [default: 8080].
    --order-date=<date>     The order date of the ticket (e.g. 01.01.2020).
    --event-date=<date>     The event date (e.g. 01.01.2020).
    --quantity=<quantity>   The number of tickets.
    -h --help               Show this screen.
    -v --version            Show version.
"""

from docopt import docopt


def main(args):
    print('TODO')
    print(args)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0')
    main(arguments)
