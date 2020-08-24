import requests
import json
from app.classes.event import Event

class Events():
    def add_event(args):
        event = Event(args)
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events', json=event.__dict__)
        # req.json() -> dataclass
        # return array of events
        b = json.dumps(req.json()) 
        print(b)

    def get_events(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events')
        # req.json() -> dataclass
        # return array of events
        data = req.json()
        Event.get_table(data)

    def get_event(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/' + args.event_id)
        # req.json() -> dataclass
        # return array of events
        print(req.json())

    def get_tickets(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/' + args.event_id + '/tickets')
        # req.json() -> dataclass
        # return array of events
        print(req.json())

    def purchase_tickets(args):
        headers = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        payload = {'quantity': args.quantity}
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events/' + args.event_id + '/purchase', params=payload, header=headers)
        # req.json() -> dataclass
        # return array of events
        print(req.json())
    
    def get_sales(args):
        events = Events.get_events(args)
        sales = {}
        for event in events:
            print(event)