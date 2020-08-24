import requests
import json
from app.classes.customer import Customer
from app.classes.ticket import Ticket

class Customers():
    @staticmethod
    def add_customer(args):
        customer = Customer(args)
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/customers', json=customer.__dict__)
        # return array of events
        print(req)

    @staticmethod
    def get_tickets(args):
        headers = {}
        params = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        if args.order_date is not None:
            params['order_date'] = args.order_date 
        if args.event_date is not None:
            params['event_date'] = args.event_date
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id + '/tickets', params=params, headers=headers)
        # return array of events
        data = req.json()
        if data == []:
            print("No Tickets available!")
        else:
            print(data)
            Ticket.print_table(req.json())

    @staticmethod
    def get_budget(args):
        headers = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id + '/budget', headers=headers)
        # return array of events
        data = []
        data.append(req.json())
        if data == []:
            print("No Tickets available!")
        else:
            Customer.print_table_budget(data)