import requests
import json
from app.classes.event import Event
from app.classes.ticket import Ticket
from app.classes.response import Response_Helper
from app.classes.sales import Sales

class EventsApi():
    @staticmethod
    def add_event(args):
        event = Event(args)
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events', json=event.__dict__, timeout=5)
        if(req.status_code == 204):
            Response_Helper.successfull()
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])

    @staticmethod
    def get_events(args):
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events', timeout=5)
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
        req = requests.get(server_addr + '/api/events/' + args.event_id, timeout=5)
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
    def purchase_tickets(args):
        headers = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events/' + args.event_id + '/purchase', json={'quantity': args.quantity}, headers=headers, timeout=5)
        if(req.status_code == 204):
            Response_Helper.successfull()
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])
    
    @staticmethod
    def get_sales(args):        
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/sales', timeout=5)
        if(req.status_code == 200):
            sales =  []
            sales.append(req.json())
            if sales == []:
                print("No tickets have been sold yet!")
            else:
                Sales.print_table(sales)
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])
            exit
        
       
        