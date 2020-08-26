# Client

## Help

The client CLI ships with command documentation that is accessible with the `--help` flag.
```
$ client --help
```

## Commands

### Usage Customer

```
$ client [--ip=<ip>] [--port=<port>] customer <customer-id>
``` 
- `event list` <br> Returns a list with all available events<br>
- `event <event-id> info` <br> Gives information about a specific event<br>
- `ticket list [--order-date=<date>] [--event-date=<date>]` <br> Returns all tickets purchased by the customer. These can be filtered by either order date or event date. <br>
- `ticket purchase --event-id=<event-id> [--quantity=<number>]` <br> The desired number of tickets for a particular event is purchased. <br>
- `budget --year=<number>` <br> Returns the customer's budget in the desired year. <br>

### Usage Admin

```
$ client [--ip=<ip>] [--port=<port>] admin
``` 
- `event list` <br> Returns a list with all available events<br>
- `event add --name=<name> --date=<date> --location=<location> --ticket-price=<number> --max-tickets=<number> --max-tickets-per-customer=<number> --sale-start-date=<date> - --sale-period=<days>` <br> Creates an event<br>
- `event <event-id> info` <br> Gives information about a specific event<br>
- `event sales` <br> Returns the sales figures of all events.<br>
- `customer add --name=<name> --budget=<budget> --address=<address>` <br> Creates a customer <br>

#### Options
- `--ip`                        IP address of the server (Default: 127.0.0.1)
- `--port`                      Port of the server [Default: 8080].
- `--order-date`                The order date of the ticket (e.g. 01.01.2020).
- `--event-dat`                 The event date (e.g. 01.01.2020).
- `--quantity`                  The number of tickets [Default: 1].
- `--name`                      The name of the customer or event.
- `--date`                      The event date (e.g. 01.01.2020).
- `--location`                  The event location (e.g. "Friedrich-Ebert-Straße 30, 78054 Villingen-Schwenningen").
- `--ticket-price`              The ticket price in € (e.g. 5).
- `--max-tickets`               The maximum number of tickets (e.g. 100).
- `--max-tickets-per-customer`  The maximum number of tickets per customer (e.g. 3).
- `--sale-start-date`           The sale start date (e.g. 01.01.2020).
- `--sale-period`               The sale period in days (e.g. 5).
- `--budget`                    The customer budget in € (e.g. 100).
- `--year`                      The year from which to request the budget (e.g. 2020).
- `--address`                   The customer address (e.g. "Friedrich-Ebert-Straße 30, 78054 Villingen-Schwenningen").

