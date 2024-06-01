from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Flask!"


@app.route('/cpu')
def handleCPUBound():
    print("received request")

    print("cpu bound task start")
    i = 0
    while i < 300000000:
        i += 1
    print("cpu bound task end")

    print("send response")

    return "Hello Flask!"


@app.route('/io')
def handleIOBound():
    print("received request")

    print("io bound task start")
    time.sleep(10)
    print("io bound task end")

    print("send response")

    return "Hello Flask!"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
