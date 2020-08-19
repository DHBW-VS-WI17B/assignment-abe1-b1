"""Server CLI
Usage:
    server
    server start [--host=<ip>] [--port=<port>]
    server -h|--help
    server -v|--version

Options:
    --host=<ip>     IP address [default: 0.0.0.0].
    --port=<port>   Port [default: 8080].
    -h, --help      Show this screen.
    -v, --version   Show version.
"""

import signal
import sys
from flask import Flask
from thespian.actors import ActorSystem
from docopt import docopt
from gevent import pywsgi
from app.routes import customers
from app.routes import events


def signal_handler(signalnum, frame):
    # pylint: disable=unused-argument
    ActorSystem().shutdown()
    sys.exit(0)


def main(args):
    signal.signal(signal.SIGINT, signal_handler)
    app = Flask(__name__)
    app.register_blueprint(customers.bp)
    app.register_blueprint(events.bp)
    ActorSystem('multiprocTCPBase')
    msg = "\033[92mServer is listening on {}:{} ...\033[0m"
    print(msg.format(args.get('--host'), args.get('--port')))
    print("\033[93mUse Ctrl+C to quit this process.\033[0m")
    server = pywsgi.WSGIServer(
        (args.get('--host'), int(args.get('--port'))), app)
    server.serve_forever()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0')
    if arguments.get('start') is True:
        main(arguments)
    else:
        print('Server CLI')
        print()
        print('No command provided.')
        print('Run `server --help` to access the command documentation.')
