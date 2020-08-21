import requests

class Customers():
      def get_customer(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id)
        # req.json() -> dataclass
        # return array of events
        print(req.json())

    def add_customer(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.event_id)
        # req.json() -> dataclass
        # return array of events
        print(req.json())

    def get_tickets(args):
        payload = {'order_date': args.order_date, 'event_date': args.event_date}
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id + '/tickets', params=payload)
        # req.json() -> dataclass
        # return array of events
        print(req.json())

    def get_budget(args):
        # server_addr = ip + port
        server_addr = 'http://' + args.ip + ":" + args.port
        req = requests.get(server_addr + '/api/customers/' + args.customer_id + '/budget', params=payload)
        # req.json() -> dataclass
        # return array of events
        print(req.json())