# quickfilehost
simple tool to create a server to serve one file
# usage
run
```
$ quickfilehost --help
usage: fast-host [-h] [-p PORT] [-n] [-o] filename
fast-host: error: the following arguments are required: filename
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
not implemented yet
