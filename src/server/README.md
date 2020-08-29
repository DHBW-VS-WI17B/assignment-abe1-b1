# Server

## Usage

Follow these steps to start the server with the `--help` flag:
1. Make sure you have at least version `3.7` of Python installed: `python --version` 
2. Install all dependencies: `python -m pip install -r requirements.txt`
3. Start the server with the `--help` flag: `python -m app --help`

## Help

The server CLI ships with command documentation that is accessible with the `--help` flag.
```
$ server --help
```

## Commands

### start

```
$ server start [options]
``` 

`server start` starts the server including the web server and the actor system.

#### Options

- `--host` (Default: `127.0.0.1`)
- `--port` (Default: `8080`)