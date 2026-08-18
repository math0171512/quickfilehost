# quickfilehost
simple tool to create a server to serve one file
# usage
run
```
$ quickfilehost --help
usage: fast-host [-h] [-p PORT] [-n] [-o] filename

Serves one file

positional arguments:
  filename

options:
  -h, --help       show this help message and exit
  -p, --port PORT  port on which to serve file, defaults to 50232
  -n, --network    whether the file is served on 127.0.0.1 or 0.0.0.0, defaults to 127.0.0.1
  -o, --once       whether to stop server after one download, defaults to false
```
or:

to serve file, locally, forever (ctrl + c to stop)
```
$ quickfilehost filename.whatever
```
to serve file, **on the entire network**, forever
```
$ quickfilehost filename.whatever --network
```
to serve file, locally, **accept one request then quit**
```
$ quickfilehost filename.whatever --once
```
to serve file, locally, forever, on port `49202`
```
$ quickfilehost filename.whatever --port 49202
```
# installation
with pip
```
$ pip install quickfilehost
```
with pipx
```
$ pipx install quickfilehost
```
