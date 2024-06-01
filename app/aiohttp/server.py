import asyncio
from aiohttp import web


async def handleCPUBound(request):
    print(f"received {request}")

    print("cpu bound task start")
    i = 0
    while i < 300000000:
        i += 1
    print("cpu bound task end")

    print("send response")

    return web.Response(text="Hello, aiohttp!")


async def handleIOBound(request):
    print(f"received {request}")

    print("io bound task start")
    await asyncio.sleep(10)
    print("io bound task end")

    print("send response")

    return web.Response(text="Hello, aiohttp!")

app = web.Application()
app.router.add_get('/cpu', handleCPUBound)
app.router.add_get('/io', handleIOBound)


async def start_app():
    # 手動でイベントのイテレーションを起動
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8000)
    await site.start()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_app())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
