import requests


def get_events(args):
    headers = {}
    if args.get('<customer-id>') is not None:
        headers['Client-ID'] = args.get('<customer-id>')
    # server_addr = ip + port
    server_addr = args.get('--ip') + ":" + args.get('--port')
    req = requests.get(server_addr + '/api/events', headers=headers)
    # req.json() -> dataclass
    # return array of events
    print('TODO')
