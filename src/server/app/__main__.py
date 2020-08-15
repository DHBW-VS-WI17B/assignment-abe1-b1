import signal
import sys
from flask import Flask
from thespian.actors import ActorSystem
from gevent import pywsgi
from app.routes import events


def signal_handler(signal, frame):
    ActorSystem().shutdown()
    sys.exit(0)


def main(args):
    signal.signal(signal.SIGINT, signal_handler)
    app = Flask(__name__)
    app.register_blueprint(events.bp)
    ActorSystem('multiprocTCPBase')
    msg = "\033[92mServer is listening...\033[0m"
    print("\033[93mUse Ctrl+C to quit this process.\033[0m")
    server = pywsgi.WSGIServer(('', 8080)), app)
    server.serve_forever()


if __name__ == '__main__':
    main()
