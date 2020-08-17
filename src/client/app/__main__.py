"""Server CLI
Usage:
    client
    client customer <customer-id> event list
    client customer <customer-id> event info
    client customer <customer-id> ticket list [--order-date=<date>] [--event-date=<date>]
    client customer <customer-id> ticket purchase [--quantity=<quantity>]
    client customer <customer-id> budget
    client admin event list
    client admin event add
    client admin event <event-id> info
    client admin event sales
    client -h|--help
    client -v|--version

Options:
    --host=<ip>     IP address [default: 0.0.0.0].
    --port=<port>   Port [default: 8080].
    -h --help       Show this screen.
    -v --version    Show version.
"""

from docopt import docopt


def main(args):
    print('TODO')
    print(args)


if __name__ == '__main__':
    args = docopt(__doc__, version='1.0.0')
    main(args)
