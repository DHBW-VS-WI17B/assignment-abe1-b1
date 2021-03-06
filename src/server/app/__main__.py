"""Server CLI
Usage:
    server
    server start [--host=<ip>] [--port=<port>]
    server -h|--help
    server -v|--version

Options:
    --host=<ip>         IP address [default: 127.0.0.1].
    --port=<port>       Port [default: 8080].
    -h, --help          Show this screen.
    -v, --version       Show version.
"""

import signal
import sys
import os
from flask import Flask
from thespian.actors import ActorSystem
from docopt import docopt
from gevent import pywsgi
from peewee import SqliteDatabase
from app.config.config import Config


def signal_handler(signalnum, frame):
    """Signal handler for SIGINT."""
    # pylint: disable=unused-argument
    ActorSystem().shutdown()
    sys.exit(0)


def init_config(args):
    """Set configuration options."""
    Config.set('HOST', args.get('--host'))
    Config.set('PORT', int(args.get('--port')))


def init_db():
    """Initialize the database and create tables."""
    from app.models.customer import Customer
    from app.models.event import Event
    from app.models.ticket import Ticket
    print("Initializing database...")
    db = SqliteDatabase(Config.get('SQLITE_DATABASE'))
    db.connect()
    db.create_tables([Customer, Event, Ticket], safe=True)
    db.close()


def init_actor_system():
    print("Initializing actor system...")
    ActorSystem('multiprocTCPBase')


def init_web_server(host, port):
    """Initialize and start the web server."""
    from app.routes import customers
    from app.routes import events
    print("Initializing web server...")
    app = Flask(__name__)
    app.register_blueprint(customers.bp)
    app.register_blueprint(events.bp)
    server = pywsgi.WSGIServer(
        (host, port), app)
    msg = "\033[92mServer is listening on {}:{} ...\033[0m"
    print(msg.format(Config.get('HOST'), Config.get('PORT')))
    print("\033[93mUse Ctrl+C to quit this process.\033[0m")
    server.serve_forever()


def check_db_path(db_path):
    """Check if the database file exists at the specified path."""
    path_exists = os.path.exists(db_path)
    if not path_exists:
        print("Server CLI")
        print()
        print("\033[91mDatabase file not found.\033[0m")
        msg = "Please create a file named `{}` in the CLI directory."
        print(msg.format(Config.get('SQLITE_DATABASE')))
        sys.exit(0)


def main():
    print("Start server...")
    signal.signal(signal.SIGINT, signal_handler)
    init_db()
    init_actor_system()
    init_web_server(Config.get('HOST'), Config.get('PORT'))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0')
    init_config(arguments)
    if arguments.get('start') is True:
        check_db_path(Config.get('SQLITE_DATABASE'))
        main()
    else:
        print('Server CLI')
        print()
        print('No command provided.')
        print('Run `server --help` to access the command documentation.')
