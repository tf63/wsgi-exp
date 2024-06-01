# wsgiで遊ぶ
### aiohttp
- ノンブロッキングI/O

CPUバウンドな処理
```
    received <Request GET /cpu >
    cpu bound task start
    cpu bound task end
    send response
    received <Request GET /cpu >
    cpu bound task start
    cpu bound task end
    send response
```
IOバウンドな処理
```
    received <Request GET /io >
    io bound task start
    received <Request GET /io >
    io bound task start
    io bound task end
    send response
    io bound task end
    send response
```

### flask
- ノンブロッキングI/O?
- flaskの開発サーバーであるWerkzeugがスレッドプールを作成してリクエストを並行して処理するらしい

CPUバウンドな処理
```
   received request
    cpu bound task start
    received request
    cpu bound task start
    cpu bound task end
    send response
    172.22.0.1 - - [01/Jun/2024 17:45:02] "GET /cpu HTTP/1.1" 200 -
    cpu bound task end
    send response
    172.22.0.1 - - [01/Jun/2024 17:45:02] "GET /cpu HTTP/1.1" 200 -
```

IOバウンドな処理
```
    received request
    io bound task start
    received request
    io bound task start
    io bound task end
    send response
    172.22.0.1 - - [01/Jun/2024 17:43:52] "GET /io HTTP/1.1" 200 -
    io bound task end
    send response
```

### falcon
- ブロッキングI/O

CPUバウンドな処理
```
    received request
    cpu bound task start
    cpu bound task end
    send response
    /usr/local/lib/python3.8/wsgiref/handlers.py:137: DeprecatedWarning: Call to deprecated property body. Please use text instead.
    self.result = application(self.environ, self.start_response)
    172.22.0.1 - - [01/Jun/2024 17:45:54] "GET /cpu HTTP/1.1" 200 36
    received request
    cpu bound task start
    cpu bound task end
    send response
    172.22.0.1 - - [01/Jun/2024 17:46:02] "GET /cpu HTTP/1.1" 200 36
```

IOバウンドな処理
```
    received request
    io bound task start
    io bound task end
    send response
    172.22.0.1 - - [01/Jun/2024 17:46:35] "GET /io HTTP/1.1" 200 36
    received request
    io bound task start
    io bound task end
    send response
    172.22.0.1 - - [01/Jun/2024 17:46:45] "GET /io HTTP/1.1" 200 36
```
