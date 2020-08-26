# Client

## Help

The client CLI ships with command documentation that is accessible with the `--help` flag.
```
$ client --help
```

## Commands Customer

### customer \<customer-id\> event list

```
$ client customer <customer-id> event list [options]
``` 

`client customer <customer-id> event list` displays a list with all available events.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
___

### customer \<customer-id\> event <event-id> info

```
$ client customer <customer-id> event <event-id> info [options]
``` 

`client customer <customer-id> event <event-id> info` displays information for customers about a specific event.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
___

### customer \<customer-id\> ticket list

```
$ client customer <customer-id> ticket list [options]
``` 

`client customer <customer-id> ticket list` displays a list with all tickets purchased by the customer.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
- `--order-date` The order date of the ticket (e.g. `01.01.2020`).
- `--event-date` The event date (e.g. `01.01.2020`).
___

### customer \<customer-id\> ticket purchase 

```
$ client customer <customer-id> ticket purchase [options]
``` 

`client customer <customer-id> ticket purchase` purchases a number of tickets for a particular event.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
- `--event-id` The id of the event.
- `--quantity` The number of tickets (Default: `1`).
___ 

### customer \<customer-id\> budget

```
$ client customer <customer-id> budget [options]
``` 

`client customer <customer-id> budget` returns the customer's budget in the desired year.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
- `--year` The year from which to request the budget (e.g. `2020`).
___

## Commands Admin

### admin event list

```
$ client admin event list [options]
``` 

`admin event list` returns a list with all available events.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
___

### admin event \<event-id\> info

```
$ client admin event <event-id> info [options]
``` 

`admin event list` returns a list with all available events.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
___

### admin add event

```
$ client admin add event [options]
``` 

`admin add event` creates an event

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
- `--name`                      The name of the event.
- `--date`                      The event date (e.g. 01.01.2020).
- `--location`                  The event location (e.g. "Friedrich-Ebert-Straße 30, 78054 Villingen-Schwenningen").
- `--ticket-price`              The ticket price in € (e.g. 5).
- `--max-tickets`               The maximum number of tickets (e.g. 100).
- `--max-tickets-per-customer`  The maximum number of tickets per customer (e.g. 3).
- `--sale-start-date`           The sale start date (e.g. 01.01.2020).
- `--sale-period`               The sale period in days (e.g. 5).
___

### admin customer add 

```
$ client admin customer add [options]
``` 

`admin customer add` creates a customer and returns the customer id.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
- `--name` The name of the customer.
- `--budget` The customer budget in € (e.g. 100).
- `--address` The customer address (e.g. "Friedrich-Ebert-Straße 30, 78054 Villingen-Schwenningen").
___

### admin event sales

```
$ client admin event sales [options]
``` 

`admin event sales` Returns the sales figures of all events.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
- `--year` The year from which to request the budget (e.g. 2020).
___
