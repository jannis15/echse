import asyncio
import uvicorn

from api import app as app_fastapi
from scheduler import app as app_rocketry


class Server(uvicorn.Server):
    def handle_exit(self, sig: int, frame) -> None:
        app_rocketry.session.shut_down()
        return super().handle_exit(sig, frame)


async def main():
    server = Server(
        config=uvicorn.Config(app_fastapi, host='127.0.0.1', port=443, workers=1, loop="asyncio",))

    api = asyncio.create_task(server.serve())
    scheduler = asyncio.create_task(app_rocketry.serve())

    await asyncio.wait([scheduler, api])


if __name__ == "__main__":
    asyncio.run(main())
