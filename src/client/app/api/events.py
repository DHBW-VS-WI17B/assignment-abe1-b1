import requests
import json
from app.classes.event import Event
from app.classes.ticket import Ticket
from app.classes.response import Response_Helper

class Events():
    @staticmethod
    def add_event(args):
        event = Event(args)
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events', json=event.__dict__)
        if(req.status_code == 204):
            Response_Helper.successfull()
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])

    @staticmethod
    def get_events(args):
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events')
        if(req.status_code == 200):
            data = req.json()
            if data == []:
                print("No events were found!")
            else:
                Event.print_table(data)
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])
        

    @staticmethod
    def get_event(args):
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/' + args.event_id)
        if(req.status_code == 200):
            data = []
            data.append(req.json())
            if data == []:
                print("No matching event was found!")
            else:
                Event.print_table(data)
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])

    @staticmethod
    def get_tickets(args, event_id):
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/' + event_id + '/tickets')
        if(req.status_code == 204):
            return req.json()
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])
            exit

    @staticmethod
    def purchase_tickets(args):
        headers = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events/' + args.event_id + '/purchase', json={'quantity': args.quantity}, headers=headers)
        if(req.status_code == 204):
            Response_Helper.successfull()
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])
    
    @staticmethod
    def get_sales(args):
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events')
        if(req.status_code == 204):
            Response_Helper.successfull()
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])
            exit
        events = req.json()
        sales =  []
        for event in events:
            event_tickets = Events.get_tickets(args, str(event['id']))
            for ticket in event_tickets:
                sales.append(ticket)  
        Ticket.print_table(sales)
        