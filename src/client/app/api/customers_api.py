import requests
from app.classes.customer import Customer
from app.classes.ticket import Ticket
from app.classes.response import Response_Helper
from app.utils.date import DateHelper


class CustomersApi():
    @staticmethod
    def add_customer(args):
        """Creates a customer."""
        customer = Customer(args)
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.post(server_addr + '/api/customers',
                            json=customer.__dict__, timeout=5)
        if(req.status_code == 200):
            print("The customer was successfully created with ID: " +
                  str(req.json()['id']))
        else:
            Response_Helper.handle_exception(
                req.status_code, req.json()['error'])

    @staticmethod
    def get_tickets(args):
        """Get a list with all tickets purchased by the customer."""
        headers = {}
        params = {}
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        if args.order_date is not None:
            params['order_date'] = DateHelper.date_to_timestamp(
                args.order_date)
        if args.event_date is not None:
            params['event_date'] = DateHelper.date_to_timestamp(
                args.event_date)
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id +
                           '/tickets', params=params, headers=headers, timeout=5)
        if(req.status_code == 200):
            data = req.json()
            if data == []:
                print("No tickets were found!")
            else:
                Ticket.print_table(req.json())
        else:
            Response_Helper.handle_exception(
                req.status_code, req.json()['error'])

    @staticmethod
    def get_budget(args):
        """Get the customer's budget in the desired year."""
        headers = {}
        params = {}
        if args.year is not None:
            params['year'] = args.year
        if args.customer_id is not None:
            headers['Customer-ID'] = args.customer_id
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id +
                           '/budget', params=params, headers=headers, timeout=5)
        if(req.status_code == 200):
            data = []
            data.append(req.json())
            Customer.print_table_budget(data)
        else:
            Response_Helper.handle_exception(
                req.status_code, req.json()['error'])
