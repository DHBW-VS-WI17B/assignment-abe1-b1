import requests
import json
from app.classes.event import Event
from app.classes.ticket import Ticket

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
        data = []
        data.append(req.json())
        if data == []:
            print("No Events available!")
        else:
            Event.print_table(data)

    @staticmethod
    def get_tickets(args, event_id):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/' + event_id + '/tickets')
        return req.json()

    @staticmethod
    def purchase_tickets(args):
        headers = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events/' + args.event_id + '/purchase', json={'quantity': args.quantity}, headers=headers)
        print(req.json())
    
    @staticmethod
    def get_sales(args):
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events')
        events = req.json()
        sales =  []
        for event in events:
            print(event['id'])
            event_tickets = Events.get_tickets(args, event['id'])
            sales.append(event_tickets)
        Ticket.print_table(sales)
        