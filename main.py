import asyncio
import websockets

async def echo(websocket, path):
    value = 0
    async for message in websocket:
        value += 1
        await websocket.send(f"by python {value}")
        print('Navegador => ' + message)


start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
