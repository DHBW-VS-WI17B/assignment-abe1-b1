# Server

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