import asyncio
import websockets


connected = set()

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