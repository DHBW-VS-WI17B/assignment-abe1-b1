import requests
import json
from app.classes.customer import Customer

class Customers():
    @staticmethod
    def get_customer(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id) 
        # return array of events
        print(req.json())

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
        params = {'order_date': args.order_date, 'event_date': args.event_date}
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id + '/tickets', params=params)
        # return array of events
        print(req.json())

    @staticmethod
    def get_budget(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id + '/budget', params=payload)
        # return array of events
        print(req.json())