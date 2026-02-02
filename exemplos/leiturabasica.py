import asyncio
import json
import websockets

async def leitor_eventos():
    uri = 'wss://relay.damus.io'
    async with websockets.connect(uri) as ws:
        req = [
            'REQ',
            'sub_1',
            {
                'kinds': [1],
                'limit': 5,
            }
        ]

        await ws.send(json.dumps(req))

        while True:
            msg = await ws.recv()
            data = json.loads(msg)

            if data[0] == "EVENT":
                event = data[2]
                print("=" * 40)
                print("Chave pública:", event["pubkey"])
                print("conteúdo:", event["content"])

            elif data[0] == "EOSE":
                print("\nFim dos eventos armazenados.\n")
                break

asyncio.run(leitor_eventos())
