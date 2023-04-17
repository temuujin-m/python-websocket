import asyncio
import websockets


connected = set()


async def consumer_handler(websocket):
    async for message in websocket:
        await consumer_handler(message)


async def producer_handler(websocket):
    while True:
        message = await consumer_handler()
        await websocket.send(message)

async def handle_client(websocket, message):

    connected.add(websocket)

    try:
        async for message in websocket:
            for other in connected:
                if other != websocket:
                    await other.send(message)
    finally:
        connected.remove(websocket)


async def main():
    async with websockets.serve(handle_client, "localhost", 8000):
        await asyncio.Future()


asyncio.run(main())