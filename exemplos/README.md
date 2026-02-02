# Leitura Básica

```
import asyncio
import json
import websockets
```

Importações importantes para o funcionamento do código, já que o protocolo funciona com chamadas assincronas e as leituras e envios são feitos em formato de *JSON*

```
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
```

Função responsável por realizar a requisição e definir os tipos de dados a serem recuperados. 

`REQ` --> Define que é uma requisição

`sub_1` --> Define o tipo de subscrição, 1 sendo notas públicas.

`'kinds': [1]` --> Define o tipo (kind) requisitado no filtro, 1 sendo notas públicas.

`'limit': 5` --> Limita a quantidade de posts recebidos para apenas 5.

```
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
```

`await ws.send(json.dumps(req))` --> Envia a requisição como *JSON*, muito importante pois é como o NOSTR trata os dados.

`msg = await ws.recv()` --> guarda o resultado da request em uma variável *msg*.

`data = json.loads(msg)` --> Transforma os dados recebidos em *JSON* para objetos *python*.


```
if data[0] == "EVENT":
                event = data[2]
                print("=" * 40)
                print("Chave pública:", event["pubkey"])
                print("conteúdo:", event["content"])

            elif data[0] == "EOSE":
                print("\nFim dos eventos armazenados.\n")
                break
```

Esse trecho de código faz a checagem do conteúdo a partir do que foi recebido. Eventos de um *relay* podem ser divididos em 3 partes, o primeiro é o tipo, após isso o subscription_id e por fim os dados armazenados nesse evento, o 'conteúdo'. 

Checando primeiramente se é um evento a partir da posição 0, ele pega o conteúdo guardado na posição junto da chave pública do remetente, exibindo no terminal.


`asyncio.run(leitor_eventos())` --> Roda a função. 👍