import asyncio
from dataclasses import dataclass


async def get_connection_with_remote(host, port):
    class _Connection:
        async def send_data(self):
            print('Sending data...')
            await asyncio.sleep(2)
            print('Sending data completed')
        
        async def recv_data(self):
            print('Receiving data...')
            await asyncio.sleep(2)
            print('Receiving data completed')

        async def hangup(self):
            print('Closing the connection...')
            await asyncio.sleep(2)
            print('Connection closed')

    print('Establishing a connection...')
    await asyncio.sleep(2)
    print('Connection established')
    return _Connection()


@dataclass
class Connection:
    host: str
    port: int

    async def __aenter__(self):
        self.connection = await get_connection_with_remote(self.host, self.port)
        return self.connection
    
    async def __aexit__(self, type_, value, traceback):
        await self.connection.hangup()


async def main():
    async with Connection('localhost', 24815) as conn:
        send_task = asyncio.create_task(conn.send_data())
        recv_task = asyncio.create_task(conn.recv_data())

        await send_task
        await recv_task


if __name__ == '__main__':
    asyncio.run(main())
