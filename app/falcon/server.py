import time
import json
import falcon


class AppResource(object):

    def on_get(self, req, resp):

        msg = {
            "message": "Welcome to the Falcon"
        }
        resp.body = json.dumps(msg)


class AppCPUResource(object):

    def on_get(self, req, resp):

        print("received request")

        print("cpu bound task start")
        i = 0
        while i < 300000000:
            i += 1
        print("cpu bound task end")

        print("send response")
        msg = {
            "message": "Welcome to the Falcon"
        }
        resp.body = json.dumps(msg)


class AppIOResource(object):

    def on_get(self, req, resp):

        print("received request")

        print("io bound task start")
        time.sleep(10)
        print("io bound task end")

        print("send response")
        msg = {
            "message": "Welcome to the Falcon"
        }
        resp.body = json.dumps(msg)


app = falcon.App()
app.add_route("/", AppResource())
app.add_route("/cpu", AppCPUResource())
app.add_route("/io", AppIOResource())

if __name__ == "__main__":
    from wsgiref import simple_server

    print("Serving on http://0.0.0.0")
    httpd = simple_server.make_server("0.0.0.0", 8000, app)
    httpd.serve_forever()
