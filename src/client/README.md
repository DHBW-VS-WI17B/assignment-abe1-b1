# Client

## Help

The client CLI ships with command documentation that is accessible with the `--help` flag.
```
$ client --help
```

## Commands

### customer \<customer-id\> event list

```
$ client customer <customer-id> event list [options]
``` 

`client customer <customer-id> event list` displays a list with all available events.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).

### customer \<customer-id\> event <event-id> info

```
$ client customer <customer-id> event <event-id> info [options]
``` 

`client customer <customer-id> event <event-id> info` displays information for customers about a specific event.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).

#### customer \<customer-id\> ticket list

```
$ client customer <customer-id> ticket list [options]
``` 

`client customer <customer-id> ticket list` displays a list with all tickets purchased by the customer.

#### Options

- `--ip` IP address of the server (Default: `127.0.0.1`).
- `--port` Port of the server (Default: `8080`).
- `--order-date` The order date of the ticket (e.g. `01.01.2020`).
- `--event-date` The event date (e.g. `01.01.2020`).
