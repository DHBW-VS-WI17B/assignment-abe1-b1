import requests
import json
from app.classes.event import Event
from app.classes.ticket import Ticket
from app.classes.response import Response_Helper
from app.classes.sales import Sales

class EventsApi():
    @staticmethod
    def add_event(args):
        """creates an event"""
        event = Event(args)
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/events', json=event.__dict__, timeout=5)
        if(req.status_code == 204):
            Response_Helper.successfull()
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])

    @staticmethod
    def get_events(args):
        """get a list with all available events"""
        headers = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events', timeout=5, headers=headers)
        if(req.status_code == 200):
            data = req.json()
            if data == []:
                print("No events were found!")
            else:
                if args.admin:
                    Event.print_table_admin(data)
                else:
                    Event.print_table_customer(data)
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])
        

    @staticmethod
    def get_event(args):
        """get information about a specific event."""
        headers = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/' + args.event_id, timeout=5, headers=headers)
        if(req.status_code == 200):
            data = []
            data.append(req.json())
            if data == []:
                print("No matching event was found!")
            else:
                if args.admin:
                    Event.print_table_admin(data)
                else:
                    Event.print_table_customer(data)
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])

    @staticmethod
    def purchase_tickets(args):
        """purchases a number of tickets for a particular event."""
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
        """get the sales figures of all events."""      
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/events/sales', timeout=5)
        if(req.status_code == 200):
            sales = req.json()
            if sales == []:
                print("No tickets have been sold yet!")
            else:
                Sales.print_table(sales)
        else:
            Response_Helper.handle_exception(req.status_code, req.json()['error'])
