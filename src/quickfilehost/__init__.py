from flask import Flask, send_file, Response
import argparse
import os
import logging

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = Flask(__name__)

filename = ""
once = False

@app.route('/')
def hello_world():
    path = os.path.join(os.getcwd(), filename)
    with open(path, 'rb') as f:
        data = f.read()

    response = Response(data, mimetype='application/octet-stream')
    response.headers['Content-Disposition'] = f'attachment; filename="{os.path.basename(filename)}"'

    if once:
        print("doing the once quit")
        response.call_on_close(lambda: os._exit(0))

    return response

def main() -> None:
    global filename
    global once
    parser = argparse.ArgumentParser(prog="fast-host",description="Serves one file")
    parser.add_argument("filename")
    parser.add_argument("-p","--port",help="port on which to serve file, defaults to 50232",default=50232)
    parser.add_argument("-n","--network",action="store_true",help="whether the file is served on 127.0.0.1 or 0.0.0.0, defaults to 127.0.0.1",default=False)
    parser.add_argument("-o","--once",action="store_true",help="whether to stop server after one download, defaults to false",default=False)
    args = parser.parse_args()
    filename = args.filename
    once = args.once
    hostip = "127.0.0.1"
    print(once)
    print("serving on:")
    print(f"http://127.0.0.1:{args.port}")
    print(f"http://localhost:{args.port}")
    if args.network:
        hostip = "0.0.0.0"
    print("please don't use this where the you don't know the people downloading.")    
    app.run(host=hostip,port=args.port)
