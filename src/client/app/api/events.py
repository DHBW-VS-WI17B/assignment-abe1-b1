import requests
import json
from app.classes.event import Event

class Events():
    @staticmethod
    def add_event(args):
        event = Event(args)
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events', json=event.__dict__)
        print(req)

    @staticmethod
    def get_events(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events')
        data = req.json()
        if data == []:
            print("No Events available!")
        else:
            Event.print_table(data)

    @staticmethod
    def get_event(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/' + args.event_id)
        data = req.json()
        if data == []:
            print("No Events available!")
        else:
            Event.print_table(data)

    @staticmethod
    def get_tickets(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/' + args.event_id + '/tickets')
        print(req.json())

    @staticmethod
    def purchase_tickets(args):
        headers = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        payload = {'quantity': args.quantity}
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events/' + args.event_id + '/purchase', params=payload, header=headers)
        print(req.json())
    
    @staticmethod
    def get_sales(args):
        events = Events.get_events(args)
        sales = {}
        for event in events:
            print(event)