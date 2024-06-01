# Hello World な WSGI アプリケーションを書く
def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    body = 'hello, world'.encode('utf-8')
    start_response(status, headers)
    return [body]


# WSGI 仕様のリファレンス実装である wsgiref を利用する
from wsgiref import simple_server

if __name__ == '__main__':

    # WSGI HTTP サーバを起動
    host = ''
    port = 8000
    app = application  # WSGI アプリケーションを指定
    server = simple_server.make_server(host, port, app)
    server.serve_forever()
